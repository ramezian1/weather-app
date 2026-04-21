import pytest
from main.weather_app import celsius_to_fahrenheit, fmt_temp, get_weather_emoji


# --- get_weather_emoji ---

@pytest.mark.parametrize("desc,expected", [
    ("Thunderstorm",        "⛈️"),
    ("Thunder nearby",      "⛈️"),
    ("Light Snow",          "❄️"),
    ("Sleet",               "❄️"),
    ("Blizzard",            "❄️"),
    ("Heavy Rain",          "🌧️"),
    ("Light Drizzle",       "🌧️"),
    ("Shower",              "🌧️"),
    ("Mist",                "🌫️"),
    ("Dense Fog",           "🌫️"),
    ("Haze",                "🌫️"),
    ("Partly Cloudy",       "☁️"),
    ("Overcast",            "☁️"),
    ("Sunny",               "☀️"),
    ("Clear",               "☀️"),
    ("Sunshine",            "☀️"),
    ("Weird weather",       "🌡️"),
])
def test_get_weather_emoji(desc, expected):
    assert get_weather_emoji(desc) == expected


def test_thunder_takes_priority_over_rain():
    # "thundery shower" contains both thunder and shower — thunder wins
    assert get_weather_emoji("Thundery Shower") == "⛈️"


# --- celsius_to_fahrenheit ---

def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32.0

def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212.0

def test_body_temperature():
    assert celsius_to_fahrenheit(37) == 98.6

def test_negative_temperature():
    assert celsius_to_fahrenheit(-40) == -40.0


# --- fmt_temp ---

def test_fmt_temp_celsius():
    assert fmt_temp("20", False, "°C") == "20°C"

def test_fmt_temp_fahrenheit():
    assert fmt_temp("0", True, "°F") == "32.0°F"

def test_fmt_temp_truncates_to_int_for_celsius():
    assert fmt_temp("22", False, "°C") == "22°C"
