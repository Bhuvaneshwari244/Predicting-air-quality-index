import requests
from datetime import datetime

API_KEY = "cdaac453b63304c6cf6170c8c491ef57"  # 🔑 Replace with your API key


def get_air_quality(lat, lon):
    """Fetch live air quality data from OpenWeatherMap."""
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "list" not in data:
        raise ValueError("Failed to fetch data. Check your API key or coordinates.")

    entry = data["list"][0]
    pollution = entry["components"]
    aqi_level = entry["main"]["aqi"]

    return pollution, aqi_level


def interpret_aqi(aqi_level):
    """Interpret OpenWeatherMap AQI scale (1–5)."""
    categories = {
        1: "Good 😀",
        2: "Fair 🙂",
        3: "Moderate 😐",
        4: "Poor 😷",
        5: "Very Poor ☠️"
    }
    return categories.get(aqi_level, "Unknown")


def main():
    # Fixed location (Example: Miryalaguda, Telangana)
    lat, lon = 16.9947, 79.9750

    pollution, aqi_level = get_air_quality(lat, lon)

    print("\n📍 Location:", f"Lat {lat}, Lon {lon}")
    print("📅 Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("\n🌫️ Pollutant Concentrations (µg/m³):")
    for k, v in pollution.items():
        print(f"  {k.upper():6}: {v}")

    print("\n🌍 Air Quality Index (1–5):", aqi_level, "-", interpret_aqi(aqi_level))


if __name__ == "__main__":
    main()
