import requests
from config import API_KEY, BASE_URL
import json
import os

CACHE_FILE = "history.json"

def get_weather_data(city, lang="de", units="metric"):
    cache = load_cache()
    if city in cache:
        return cache[city]

    params = {
        "q": city,
        "appid": API_KEY,
        "lang": lang,
        "units": units
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        weather_data = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind": data["wind"]["speed"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"]
        }

        cache[city] = weather_data
        save_cache(cache)
        return weather_data

    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP Error: {e.response.status_code}"}
    except requests.exceptions.RequestException:
        return {"error": "Netzwerkfehler beim Abrufen der Wetterdaten."}

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(data):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)
