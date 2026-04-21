# 🌤️ TheWeather

A minimal terminal weather app built in Python. Current conditions, today's hourly breakdown, and a multi-day forecast for any city — no API key required.

## Features

- Real-time weather for any city via [wttr.in](https://wttr.in)
- Morning / midday / evening hourly breakdown for today
- Multi-day forecast with min/max temps
- Celsius and Fahrenheit — choice saved automatically between runs
- Auto-detects your city from IP on startup (press Enter to accept)
- Color-coded output with emoji condition descriptions
- Graceful error handling for bad city names, timeouts, and network issues

## Setup

### Prerequisites

- Python 3.9 or higher
- pip

### Option A — run directly (no install)

```bash
# 1. Clone the repo
git clone https://github.com/ramezian1/weather-app.git
cd weather-app

# 2. Install dependencies
pip install -r main/requirements.txt

# 3. Run
python main/weather_app.py
```

### Option B — install as a global CLI tool

```bash
# 1. Clone the repo
git clone https://github.com/ramezian1/weather-app.git
cd weather-app

# 2. Install (adds `theweather` command to your PATH)
pip install .

# 3. Run from anywhere
theweather
```

### Recommended: use a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r main/requirements.txt
python main/weather_app.py
```

## Usage

```
Enter city name [New York]:       # detected from IP — press Enter to accept
Units — (C)elsius or (F)ahrenheit [C]:
```

Your unit preference is saved to `~/.theweather.json` after the first run and pre-filled on the next.

## Demo

```
  _____ _    __   _    __         _   _
 |_   _| |__/ /__| |  / /__ ___ _| |_| |_  ___ _ _
   | | | ' \/ -_) | / // -_) _` |  _| ' \/ -_) '_|
   |_| |_||_\___|_|/_/ \___\__,_|\__|_||_\___|_|

Enter city name [New York]:
Units — (C)elsius or (F)ahrenheit [C]:

  NEW YORK  ☁️  Partly Cloudy  18°C  (feels 16°C)
  💧 58%   💨 22 km/h
  ────────────────────────────────────────────────────
  06:00   🌧️   14°C    Light Rain
  12:00   ☁️   18°C    Partly Cloudy
  18:00   ☀️   17°C    Clear
  ────────────────────────────────────────────────────
  Wed Apr 22   ☁️   Overcast               ↓ 13°C   ↑ 21°C
  Thu Apr 23   🌧️   Light Rain Shower      ↓ 11°C   ↑ 18°C
  ────────────────────────────────────────────────────
```

## Dependencies

| Package | Purpose |
|---|---|
| `requests` | Fetch weather data from wttr.in and detect location via ipinfo.io |
| `colorama` | Cross-platform terminal colors |
| `pyfiglet` | ASCII art banner |

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

25 tests covering emoji mapping, temperature conversion, and formatting.

## Project Structure

```
weather-app/
├── main/
│   ├── weather_app.py     # main app
│   └── requirements.txt   # dependencies
├── tests/
│   └── test_weather_app.py
└── pyproject.toml         # packaging config (for pip install .)
```

## Contributing

Fork the repo and open a pull request, or file an issue for suggestions.

---

Created & owned by [Robert Mezian](https://github.com/ramezian1). All rights reserved.
