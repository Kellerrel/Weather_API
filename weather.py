import requests
# requests on teek, mis võimaldab Pythonil interneti kaudu serverile päringuid saata.

url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60&lon=24.75"
# url kus parameetriteks on Tallinna laius ja pikkus ühikud ning comapct on API versioon, mis tagastab kompaktse ilmaennustuse.

headers = {
    "User-Agent": "MinuIlmarakendus/1.0 (kontakt@domain.com)"
}
# annan pringule päise, mis sisaldab kasutaja nime ja e-posti aadressi, et API saaks teada, kes päringu teeb.

response = requests.get(
    url,
    headers=headers
)
# saadan päringu API-le, kasutades requests.get meetodit, millele edastan URL-i ja päised.

response.raise_for_status() 
# kontrollin, kas päring õnnestus. Kui päring ebaõnnestub, viskab see erandi veateate.

data = response.json() # teisaldan JSON vastuse Pythoni struktuuri. 

# tabeli pealkirjad
print()
print(
    f"{'TIME':<20}"
    f"{'TEMP.':>8}  "
    f"{'HUMIDITY':>9}  "
    f"{'WIND':>9}  "
    f"{'CLOUDS':>10}  "
    f"{'PRECIPITATION':>9}  "
    f"{'WEATHER':>10}"
)
print("─" * 91)

for item in data["properties"]["timeseries"][:12]: # Töötlen andmeid läbi, võttes ainult esimesed 12 tundi.
    time = item["time"].replace("T", " ").replace("Z", "")

    d = item["data"]["instant"]["details"]
    weather = item["data"]["next_1_hours"]["summary"]["symbol_code"]
    rain = item["data"]["next_1_hours"]["details"]["precipitation_amount"]

    print(
        f"{time} | "
        f"{d['air_temperature']:5.1f} °C | "
        f"{d['relative_humidity']:5.1f} % | "
        f"{d['wind_speed']:4.1f} m/s | "
        f"{d['cloud_area_fraction']:5.1f} % | "
        f"{rain:4.1f} mm | "
        f"{weather}"
    )


