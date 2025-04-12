import requests

# ---------------------------
# Weather emoji helper
# ---------------------------
def get_weather_emoji(description):
    description = description.lower()
    if "sun" in description:
        return "☀️"
    elif "cloud" in description:
        return "☁️"
    elif "rain" in description:
        return "🌧️"
    elif "snow" in description:
        return "❄️"
    elif "thunder" in description:
        return "⛈️"
    elif "mist" in description or "fog" in description:
        return "🌫️"
    else:
        return "🌡️"

# ---------------------------
# Temperature converter
# ---------------------------
def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 1)

# ---------------------------
# Main weather fetcher
# ---------------------------
def get_weather(city, unit="C"):
    api_url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        # Current conditions
        current = data['current_condition'][0]
        desc = current['weatherDesc'][0]['value']
        emoji = get_weather_emoji(desc)

        temp = int(current['temp_C'])
        feels_like = int(current['FeelsLikeC'])

        # Tomorrow forecast
        tomorrow = data['weather'][1]['hourly'][4]  # Approx midday forecast
        tomorrow_temp = int(tomorrow['tempC'])
        tomorrow_desc = tomorrow['weatherDesc'][0]['value']
        tomorrow_emoji = get_weather_emoji(tomorrow_desc)

        if unit.upper() == "F":
            temp = celsius_to_fahrenheit(temp)
            feels_like = celsius_to_fahrenheit(feels_like)
            tomorrow_temp = celsius_to_fahrenheit(tomorrow_temp)
            unit_symbol = "°F"
        else:
            unit_symbol = "°C"

        # Print weather
        print(f"\n📍 Weather in {city.capitalize()}")
        print(f"Now: {emoji} {desc}")
        print(f"Temperature: {temp}{unit_symbol} (Feels like {feels_like}{unit_symbol})")
        print(f"\n📅 Tomorrow: {tomorrow_emoji} {tomorrow_desc}")
        print(f"Expected Temp: {tomorrow_temp}{unit_symbol}")
        print("-" * 40)

    except requests.RequestException as e:
        print(f"⚠️ Error fetching weather data: {e}")
    except KeyError:
        print("⚠️ Invalid city name or API limit reached.")

# ---------------------------
# App runner
# ---------------------------
def main():
    print("🌤️ Welcome to Bobby's Weather App 🌤️")
    city = input("Enter city name: ")
    unit = input("Choose units - (C)elsius or (F)ahrenheit: ").strip().upper()

    if unit not in ["C", "F"]:
        print("⚠️ Invalid unit choice. Defaulting to Celsius.")
        unit = "C"

    get_weather(city, unit)

if __name__ == "__main__":
    main()