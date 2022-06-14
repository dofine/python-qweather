from python_qweather import __version__
from python_qweather import QWeather
import aiohttp

import pytest
import os


def test_version():
    assert __version__ == "0.1.3"

@pytest.mark.asyncio
async def test_now_weather():
    async with aiohttp.ClientSession() as client_session:
        q = QWeather(api_key=os.environ['QWEATHER_APIKEY'], session=client_session, location_key='101010100')
        now_weather = await q.async_get_now_weather()
        assert now_weather['code'] == '200'
        # assert now_weather['now']['temp'] == '25'
        
