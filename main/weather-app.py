import requests
from colorama import init, Fore, Style

init(autoreset=True)

def get_weather_emoji(description):
    description = description.lower()
    if "sun" in description or "clear" in description:
        return "☀️"
    elif "thunder" in description:
        return "⛈️"
    elif "rain" in description or "drizzle" in description:
        return "🌧️"
    elif "snow" in description or "sleet" in description:
        return "❄️"
    elif "mist" in description or "fog" in description:
        return "🌫️"
    elif "cloud" in description or "overcast" in description:
        return "☁️"
    else:
        return "🌡️"

def celsius_to_fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32, 1)

def get_weather(city, unit="C"):
    api_url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Current conditions
        current = data["current_condition"][0]
        desc = current["weatherDesc"][0]["value"]
        emoji = get_weather_emoji(desc)
        temp = int(current["temp_C"])
        feels_like = int(current["FeelsLikeC"])
        humidity = current.get("humidity", "N/A")
        wind_kmph = current.get("windspeedKmph", "N/A")

        # Tomorrow forecast — guard against short API responses
        weather_days = data.get("weather", [])
        if len(weather_days) < 2:
            print(Fore.YELLOW + "⚠️  Tomorrow's forecast is unavailable.")
            tomorrow_line = None
        else:
            hourly = weather_days[1].get("hourly", [])
            tomorrow = hourly[4] if len(hourly) > 4 else (hourly[-1] if hourly else None)
            if tomorrow:
                tomorrow_temp = int(tomorrow["tempC"])
                tomorrow_desc = tomorrow["weatherDesc"][0]["value"]
                tomorrow_emoji = get_weather_emoji(tomorrow_desc)
            else:
                tomorrow_line = None

        use_fahrenheit = unit.upper() == "F"
        unit_symbol = "°F" if use_fahrenheit else "°C"

        if use_fahrenheit:
            temp = celsius_to_fahrenheit(temp)
            feels_like = celsius_to_fahrenheit(feels_like)
            if tomorrow:
                tomorrow_temp = celsius_to_fahrenheit(tomorrow_temp)

        # Output
        print()
        print(Fore.CYAN + Style.BRIGHT + f"📍 Weather in {city.title()}")
        print(Fore.WHITE + f"   {emoji}  {desc}")
        print(Fore.YELLOW + f"   🌡️  {temp}{unit_symbol}  (feels like {feels_like}{unit_symbol})")
        print(Fore.BLUE + f"   💧 Humidity: {humidity}%   💨 Wind: {wind_kmph} km/h")

        if tomorrow:
            print()
            print(Fore.CYAN + Style.BRIGHT + "📅 Tomorrow's Forecast")
            print(Fore.WHITE + f"   {tomorrow_emoji}  {tomorrow_desc}")
            print(Fore.YELLOW + f"   🌡️  {tomorrow_temp}{unit_symbol}")

        print(Fore.WHITE + "\n" + "─" * 40)

    except requests.exceptions.Timeout:
        print(Fore.RED + "⚠️  Request timed out. Check your connection and try again.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"⚠️  Error fetching weather data: {e}")
    except (KeyError, IndexError, ValueError) as e:
        print(Fore.RED + f"⚠️  Unexpected API response — city may be invalid. ({e})")

def main():
    print(Fore.CYAN + Style.BRIGHT + "🌤️  TheWeather 🌤️")
    city = input("Enter city name: ").strip()
    if not city:
        print(Fore.RED + "⚠️  No city entered. Exiting.")
        return

    unit = input("Choose units — (C)elsius or (F)ahrenheit: ").strip().upper()
    if unit not in ("C", "F"):
        print(Fore.YELLOW + "⚠️  Invalid unit choice. Defaulting to Celsius.")
        unit = "C"

    get_weather(city, unit)

if __name__ == "__main__":
    main()
