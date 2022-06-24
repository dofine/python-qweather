"""Constants for QWeather library."""
from __future__ import annotations
from typing import Final

ATTR_CURRENT_CONDITIONS: str = 'weather_now'
ATTR_GEOPOSITION: str = 'geoapi'
ATTR_DAILY_FORECAST_3D: str = 'forecasts_3d'
ATTR_DAILY_FORECAST_7D: str = 'forecasts_7d'
ATTR_HOURLY_FORECAST: str = 'forecasts_24h'
ATTR_SUNSET: str = 'sunset'
ATTR_AIRNOW: str = 'air_now'

ENDPOINT: Final = 'https://api.qweather.com/v7/'
DEV_ENDPOINT: Final = 'https://devapi.qweather.com/v7/'
GEO_ENDPOINT: Final = 'https://geoapi.qweather.com/v2/city/lookup'

# status code https://dev.qweather.com/docs/resource/status-code/
HTTP_OK: Final = 200
HTTP_NO_DATA: Final = 204
HTTP_ERROR: Final = 400
HTTP_UNAUTHORIZED: Final = 401
HTTP_QUOTA: Final = 402
HTTP_NO_ACCESS: Final = 403
HTTP_NO_LOCATION: Final = 404
HTTP_QPM: Final = 429
HTTP_TIMEOUT: Final = 500
HTTP_HEADERS: dict[str, str] = {'Content-Encoding': 'gzip'}
REQUESTS_EXCEEDED: Final = 'The allowed number of requests has been exceeded.'

REMOVE_FROM_CURRENT_CONDITION: tuple[str, ...] = (
    'LocalObservationDateTime',
    'EpochTime',
    'WeatherText',
    'IsDayTime',
    'TemperatureSummary',
    'MobileLink',
    'Link',
)
REMOVE_FROM_FORECAST: tuple[str, ...] = (
    'Sun',
    'Moon',
    'Sources',
    'MobileLink',
    'Link',
)
TEMPERATURES: tuple[str, ...] = (
    'Temperature',
    'RealFeelTemperature',
    'RealFeelTemperatureShade',
)
URLS: dict[str, str] = {
    ATTR_GEOPOSITION: '?location={longitude},{latitude}&key={key}',
    ATTR_CURRENT_CONDITIONS: 'weather/now?location={location_key}&key={key}&unit={unit}',
    ATTR_DAILY_FORECAST_3D: 'weather/3d?location={location_key}&key={key}&unit={unit}',  # pylint: disable=line-too-long
    ATTR_DAILY_FORECAST_7D: 'weather/7d?location={location_key}&key={key}&unit={unit}',
    ATTR_SUNSET: 'astronomy/sun?location={location_key}&key={key}',
    ATTR_AIRNOW: 'air/now?location={location_key}&key={key}',
    ATTR_HOURLY_FORECAST: 'weather/24h?location={location_key}&key={key}&unit={unit}',
}
