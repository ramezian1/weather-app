import json
import os
from datetime import datetime

import pyfiglet
import requests
from colorama import Fore, Style, init

init(autoreset=True)

CONFIG_PATH = os.path.expanduser("~/.theweather.json")


def load_config():
    try:
        with open(CONFIG_PATH) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, IOError):
        return {}


def save_config(config):
    try:
        with open(CONFIG_PATH, "w") as f:
            json.dump(config, f)
    except IOError:
        pass


def detect_location():
    try:
        r = requests.get("https://ipinfo.io/json", timeout=5)
        r.raise_for_status()
        return r.json().get("city", "")
    except Exception:
        return ""


def get_weather_emoji(description):
    d = description.lower()
    if "thunder" in d:
        return "⛈️"
    if "snow" in d or "sleet" in d or "blizzard" in d:
        return "❄️"
    if "rain" in d or "drizzle" in d or "shower" in d:
        return "🌧️"
    if "mist" in d or "fog" in d or "haze" in d:
        return "🌫️"
    if "cloud" in d or "overcast" in d:
        return "☁️"
    if "sun" in d or "clear" in d or "sunny" in d:
        return "☀️"
    return "🌡️"


def celsius_to_fahrenheit(celsius):
    return round((int(celsius) * 9 / 5) + 32, 1)


def fmt_temp(temp_c, use_f, symbol):
    t = celsius_to_fahrenheit(temp_c) if use_f else int(temp_c)
    return f"{t}{symbol}"


_W = 52


def _div():
    print(Style.DIM + Fore.WHITE + "  " + "─" * _W)


def print_hourly(hourly, use_f, symbol):
    for idx, time_str in [(2, "06:00"), (4, "12:00"), (6, "18:00")]:
        if idx < len(hourly):
            h = hourly[idx]
            desc = h["weatherDesc"][0]["value"]
            emoji = get_weather_emoji(desc)
            temp = fmt_temp(h["tempC"], use_f, symbol)
            print(Style.DIM + Fore.WHITE + f"  {time_str}   " +
                  Style.NORMAL + Fore.WHITE + f"{emoji}   " +
                  Fore.YELLOW + f"{temp:<8}" +
                  Fore.WHITE + desc)


def get_weather(city, unit="C"):
    api_url = f"https://wttr.in/{city}?format=j1"
    use_f = unit.upper() == "F"
    symbol = "°F" if use_f else "°C"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data["current_condition"][0]
        desc = current["weatherDesc"][0]["value"]
        emoji = get_weather_emoji(desc)
        temp = fmt_temp(current["temp_C"], use_f, symbol)
        feels = fmt_temp(current["FeelsLikeC"], use_f, symbol)
        humidity = current.get("humidity", "N/A")
        wind = current.get("windspeedKmph", "N/A")

        print()
        print(Fore.CYAN + Style.BRIGHT + f"  {city.upper()}  " +
              Style.NORMAL + Fore.WHITE + f"{emoji}  {desc}  " +
              Fore.YELLOW + f"{temp}  " +
              Style.DIM + Fore.WHITE + f"(feels {feels})")
        print(Fore.BLUE + f"  💧 {humidity}%   💨 {wind} km/h")

        weather_days = data.get("weather", [])

        if weather_days:
            _div()
            print_hourly(weather_days[0].get("hourly", []), use_f, symbol)

        if len(weather_days) >= 2:
            _div()
            for day_data in weather_days[1:]:
                date_str = day_data.get("date", "")
                try:
                    date_label = datetime.strptime(date_str, "%Y-%m-%d").strftime("%a %b %d")
                except ValueError:
                    date_label = date_str
                min_t = fmt_temp(day_data["mintempC"], use_f, symbol)
                max_t = fmt_temp(day_data["maxtempC"], use_f, symbol)
                hourly = day_data.get("hourly", [])
                mid = hourly[4] if len(hourly) > 4 else (hourly[-1] if hourly else None)
                day_desc = mid["weatherDesc"][0]["value"] if mid else "N/A"
                day_emoji = get_weather_emoji(day_desc)
                print(Fore.WHITE + f"  {date_label:<12}  {day_emoji}   {day_desc:<22}" +
                      Fore.YELLOW + f"↓ {min_t}   ↑ {max_t}")

        _div()
        print()

    except requests.exceptions.Timeout:
        print(Fore.RED + "⚠️  Request timed out. Check your connection.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"⚠️  Network error: {e}")
    except (KeyError, IndexError, ValueError) as e:
        print(Fore.RED + f"⚠️  Unexpected API response — city may be invalid. ({e})")


def main():
    banner = pyfiglet.figlet_format("TheWeather", font="slant")
    print(Fore.CYAN + Style.BRIGHT + banner)

    config = load_config()

    # Auto-detect city from IP
    detected = detect_location()
    prompt = f"Enter city name [{detected}]: " if detected else "Enter city name: "
    city = input(prompt).strip()
    if not city:
        if detected:
            city = detected
        else:
            print(Fore.RED + "⚠️  No city entered. Exiting.")
            return

    # Unit preference — recall saved default
    saved_unit = config.get("unit", "")
    default_label = saved_unit if saved_unit in ("C", "F") else "C"
    unit = input(f"Units — (C)elsius or (F)ahrenheit [{default_label}]: ").strip().upper()
    if unit not in ("C", "F"):
        unit = default_label

    config["unit"] = unit
    save_config(config)

    get_weather(city, unit)


if __name__ == "__main__":
    main()
