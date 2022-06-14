"""Constants for QWeather library."""
from __future__ import annotations

ATTR_CURRENT_CONDITIONS: str = "weather_now"
ATTR_GEOPOSITION: str = "geoapi"
ATTR_DAILY_FORCAST_3D: str = "forecasts_3d"
ATTR_DAILY_FORCAST_7D: str = "forecasts_7d"
ATTR_SUNSET: str = 'sunset'
ATTR_AIRNOW: str = 'air_now'

ENDPOINT: str = "https://api.qweather.com/v7/"
DEV_ENDPOINT: str = "https://devapi.qweather.com/v7/"
GEO_ENDPOINT: str = "https://geoapi.qweather.com/v2/city/lookup"
HTTP_OK: int = 200
HTTP_UNAUTHORIZED: int = 401
HTTP_PAYMENT: int =402
HTTP_HEADERS: dict[str, str] = {"Content-Encoding": "gzip"}
REQUESTS_EXCEEDED: str = "The allowed number of requests has been exceeded."

REMOVE_FROM_CURRENT_CONDITION: tuple[str, ...] = (
    "LocalObservationDateTime",
    "EpochTime",
    "WeatherText",
    "IsDayTime",
    "TemperatureSummary",
    "MobileLink",
    "Link",
)
REMOVE_FROM_FORECAST: tuple[str, ...] = ("Sun", "Moon", "Sources", "MobileLink", "Link")
TEMPERATURES: tuple[str, ...] = (
    "Temperature",
    "RealFeelTemperature",
    "RealFeelTemperatureShade",
)
URLS: dict[str, str] = {
    ATTR_GEOPOSITION: "?location={longitude},{latitude}&key={key}",
    ATTR_CURRENT_CONDITIONS: "weather/now?location={location_key}&key={key}&unit={unit}",
    ATTR_DAILY_FORCAST_3D: "weather/3d?location={location_key}&key={key}&unit={unit}",  # pylint: disable=line-too-long
    ATTR_DAILY_FORCAST_7D: "weather/7d?location={location_key}&key={key}&unit={unit}",
    ATTR_SUNSET: "astronomy/sun?location={location_key}&key={key}",
    ATTR_AIRNOW: "air/now?location={location_key}&key={key}"

}