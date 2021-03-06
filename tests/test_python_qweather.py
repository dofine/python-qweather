from python_qweather import __version__
from python_qweather import QWeather
import aiohttp

import pytest
import os


def test_version():
    assert __version__ == '0.1.4'


@pytest.mark.asyncio
async def test_now_weather():
    async with aiohttp.ClientSession() as client_session:
        q = QWeather(
            api_key=os.environ['QWEATHER_APIKEY'],
            session=client_session,
            location_key='101010100',
        )
        now_weather = await q.async_get_now_weather()
        assert now_weather['code'] == '200'


@pytest.mark.asyncio
async def test_geoapi():
    async with aiohttp.ClientSession() as client_session:
        q = QWeather(
            api_key=os.environ['QWEATHER_APIKEY'],
            session=client_session,
            latitude=39.96583,
            longitude=116.328955,
        )
        location_key = await q.async_get_location()
        assert location_key == '101010200'


@pytest.mark.asyncio
async def test_hourly_forecast():
    async with aiohttp.ClientSession() as client_session:
        q = QWeather(
            api_key=os.environ['QWEATHER_APIKEY'],
            session=client_session,
            location_key='101010100',
        )
        hourly_forecast = await q.async_get_hourly_forecast()
        assert hourly_forecast['code'] == '200'
