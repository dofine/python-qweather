"""
Python wrapper for getting weather data from https://qweather.com
"""
from __future__ import annotations

import json
import logging
from typing import Any, Dict, cast
import hashlib
from aiohttp import ClientSession


from .const import (
    ATTR_AIRNOW,
    ATTR_CURRENT_CONDITIONS,
    ATTR_DAILY_FORCAST_3D,
    ATTR_DAILY_FORCAST_7D,
    ATTR_GEOPOSITION,
    ATTR_SUNSET,
    ENDPOINT,
    GEO_ENDPOINT,
    HTTP_HEADERS,
    HTTP_OK,
    HTTP_UNAUTHORIZED,
    REMOVE_FROM_CURRENT_CONDITION,
    REMOVE_FROM_FORECAST,
    TEMPERATURES,
    URLS,
    DEV_ENDPOINT,
)

_LOGGER = logging.getLogger(__name__)


class QWeather:
    """Main class to perform qweather API requests"""

    def __init__(
        self,
        api_key: str,
        session: ClientSession,
        latitude: float | None = None,
        longitude: float | None = None,
        location_key: str | None = None,
        is_dev: bool = True,
        unit: str = "m",
    ):
        """Initialize."""
        if not self._valid_api_key(api_key):
            raise InvalidApiKeyError(
                "Your API Key must be a 32-character hexadecimal string"
            )

        if not location_key:
            if not self._valid_coordinates(latitude, longitude):
                raise InvalidCoordinatesError("Your coordinates are invalid")

        self.latitude = latitude
        self.longitude = longitude
        self._api_key = api_key
        self._session = session
        self._location_key = location_key
        self._is_dev = is_dev
        self._unit = unit

    @staticmethod
    def _valid_coordinates(
        latitude: float | int | None, longitude: float | int | None
    ) -> bool:
        """Return True if coordinates are valid."""
        try:
            assert isinstance(latitude, (int, float)) and isinstance(
                longitude, (int, float)
            )
            assert abs(latitude) <= 90 and abs(longitude) <= 180
        except (AssertionError, TypeError):
            return False
        return True

    @staticmethod
    def _valid_api_key(api_key: str) -> bool:
        """TODO: Return True if API key is valid."""
        return True

    def _construct_url(self, arg: str, **kwargs: str) -> str:
        """Construct API URL."""
        if arg == ATTR_GEOPOSITION:
            url = GEO_ENDPOINT + URLS[arg].format(**kwargs)
        else:
         url = (DEV_ENDPOINT if self._is_dev else ENDPOINT) + URLS[arg].format(**kwargs)

        return url

    @staticmethod
    def _clean_current_condition(
        data: dict[str, Any], to_remove: tuple[str, ...]
    ) -> dict[str, Any]:
        """Clean current condition API response."""
        return {key: data[key] for key in data if key not in to_remove}

    @staticmethod
    def _parse_forecast(data: dict, to_remove: tuple) -> list:
        """Parse and clean forecast API response."""
        parsed_data = [
            {key: value for key, value in item.items() if key not in to_remove}
            for item in data["daily"]
        ]

        return parsed_data

    @staticmethod
    def _get_signature(params: Dict, api_key: str) -> Dict:
        sorted_params = sorted(
            [
                "{}={}".format(k, v)
                for k, v in params.items()
                if v != "" and k != "sign"
            ],
            key=lambda x: x[0],
        )
        s = "&".join(sorted_params)
        s += api_key
        md5_s = hashlib.md5(s.encode("utf-8")).hexdigest()
        return md5_s

    async def _async_get_data(self, url: str) -> dict[str, Any]:
        """Retreive data from qweather API."""

        async with self._session.get(url, headers=HTTP_HEADERS) as resp:
            data = await resp.json()
            if int(data["code"]) == HTTP_UNAUTHORIZED:
                raise InvalidApiKeyError("Invalid API key")
            if resp.status != HTTP_OK:
                raise ApiError(f"Invalid response from QWeather API: {data['code']}")
            _LOGGER.debug("Data retrieved from %s, status: %s", url, data["code"])

        # pylint: disable=deprecated-typing-alias
        return cast(Dict[str, Any], data if isinstance(data, dict) else data[0])

    async def async_get_location(self) -> None:
        """TODO Retreive location data from QWeather.
        If `location_key` is not provided, try to lookup it by lat/lon
        """
        url = self._construct_url(
            ATTR_GEOPOSITION,
            key=self._api_key,
            latitude=str(self.latitude),
            longitude=str(self.longitude),
        )
        data = await self._async_get_data(url)
        # return the first item from list.
        self._location_key = data["location"][0]["id"]
        return self._location_key


    async def async_get_daily_forecast(self) -> list[dict[str, Any]]:
        """Retreive forecast data from QWeather."""
        if not self._location_key:
            await self.async_get_location()
            
        assert self._location_key is not None
        url = self._construct_url(
            ATTR_DAILY_FORCAST_7D if self._is_dev else ATTR_DAILY_FORCAST_3D,
            key=self._api_key,
            location_key=self._location_key,
            unit=self._unit,
        )
        data = await self._async_get_data(url)
        return self._parse_forecast(data, REMOVE_FROM_FORECAST)

    async def async_get_now_weather(self) -> Dict[str, Any]:
        url = self._construct_url(
            ATTR_CURRENT_CONDITIONS,
            key=self._api_key,
            location_key=self._location_key,
            unit=self._unit,
        )
        data = await self._async_get_data(url)
        return self._clean_current_condition(data, REMOVE_FROM_CURRENT_CONDITION)

    async def async_get_sunrise(self) -> Dict[str, Any]:
        url = self._construct_url(
            ATTR_SUNSET, key=self._api_key, location_key=self._location_key
        )
        data = await self._async_get_data(url)
        return data

    async def async_get_airnow(self) -> Dict[str, Any]:
        url = self._construct_url(
            ATTR_AIRNOW, key=self._api_key, location_key=self._location_key
        )
        data = await self._async_get_data(url)
        return data["now"]

    @property
    def location_name(self) -> str | None:
        """Return location name."""
        return self._location_name

    @property
    def location_key(self) -> str | None:
        """Return location key."""
        return self._location_key



class ApiError(Exception):
    """Raised when QWeather API request ended in error."""

    def __init__(self, status: str):
        """Initialize."""
        super().__init__(status)
        self.status = status


class InvalidApiKeyError(Exception):
    """Raised when API Key format is invalid."""

    def __init__(self, status: str):
        """Initialize."""
        super().__init__(status)
        self.status = status


class InvalidCoordinatesError(Exception):
    """Raised when coordinates are invalid."""

    def __init__(self, status: str):
        """Initialize."""
        super().__init__(status)
        self.status = status


class RequestsExceededError(Exception):
    """Raised when allowed number of requests has been exceeded."""

    def __init__(self, status: str):
        """Initialize."""
        super().__init__(status)
        self.status = status
