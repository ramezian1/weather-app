# 🌤️ TheWeather

A clean, fast terminal weather app built in Python. Get current conditions, today's hourly breakdown, and a multi-day forecast for any city — no API key required.

## Features

- 📍 Real-time weather for any city
- ⏱️ Morning / midday / evening breakdown for today
- 📅 Multi-day forecast with min/max temps
- 🌡️ Celsius and Fahrenheit support (preference saved automatically)
- 📡 Auto-detects your city from IP on startup
- 🌈 Color-coded terminal output with emoji descriptions
- ⚠️ Graceful error handling (timeout, bad city, network issues)

## Getting Started

### Option A — run directly

```bash
pip install -r main/requirements.txt
python main/weather_app.py
```

### Option B — install as a CLI tool

```bash
pip install .
theweather
```

Your unit preference (C/F) is saved to `~/.theweather.json` after the first run.

## Demo

```
  _____ _    __   _    __         _   _
 |_   _| |__/ /__| |  / /__ ___ _| |_| |_  ___ _ _
   | | | ' \/ -_) | / // -_) _` |  _| ' \/ -_) '_|
   |_| |_||_\___|_|/_/ \___\__,_|\__|_||_\___|_|

Enter city name [New York]:
Units — (C)elsius or (F)ahrenheit [C]:

  📍 New York — Now
     ☁️  Partly Cloudy
     🌡️  18°C  (feels like 16°C)
     💧 Humidity: 58%   💨 Wind: 22 km/h

  ⏱️  Today
     Morning  (06:00)  🌧️  14°C  —  Light Rain
     Midday   (12:00)  ☁️  18°C  —  Partly Cloudy
     Evening  (18:00)  ☀️  17°C  —  Clear

  📅 Forecast
     Wednesday, Apr 22     ☁️  Overcast
                              ↓ 13°C  ↑ 21°C
     Thursday, Apr 23      🌧️  Light Rain Shower
                              ↓ 11°C  ↑ 18°C

  ──────────────────────────────────────
```

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

## Future Improvements

- 🌍 Hourly forecast for tomorrow
- 🗂️ Export forecast to text or CSV

## Contributing

Contributions are welcome! Fork this repo and submit a pull request, or open an issue for suggestions.

---

Created & Owned by [Robert Mezian](https://github.com/ramezian1). All rights reserved as of 2025.
