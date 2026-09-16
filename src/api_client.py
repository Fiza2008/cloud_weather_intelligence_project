import requests

def fetch_weather(city, api_key):
    """Fetch current weather from OpenWeatherMap.
    Kept separate from the rest of the pipeline so the provider can be changed easily.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(
        url,
        params={"q": city, "appid": api_key, "units": "metric"},
        timeout=15,
    )
    response.raise_for_status()
    payload = response.json()

    return {
        "date": __import__("datetime").date.today().isoformat(),
        "city": payload["name"],
        "state": "",
        "temperature_c": payload["main"]["temp"],
        "humidity_pct": payload["main"]["humidity"],
        "wind_speed_kmh": round(payload["wind"]["speed"] * 3.6, 2),
        "precipitation_mm": 0.0,
        "condition": payload["weather"][0]["description"].title(),
    }
