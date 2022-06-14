# Python API wrapper for [和风天气](https://qweather.com)


## Features
- [城市信息查询](https://dev.qweather.com/docs/api/geo/city-lookup/)
- [实时天气](https://dev.qweather.com/docs/api/weather/weather-now/)
- [逐天天气预报](https://dev.qweather.com/docs/api/weather/weather-daily-forecast/)
- [实时空气质量](https://dev.qweather.com/docs/api/air/air-now/)

## Usage
暂时只支持异步（async）调用，因为最初是为集成在 homeassistant 开发的 :)

### 实时天气
```python
import aiohttp
import asyncio
from python_qweather import QWeather

async def test_now_weather():
    async with aiohttp.ClientSession() as client_session:
        q = QWeather(api_key=os.environ['QWEATHER_APIKEY'], session=client_session, location_key='101010100')
        now_weather = await q.async_get_now_weather()
        print(now_weather)

asyncio.run(test_now_weather())
```

## TODO

## Credits and Thanks
- https://github.com/bieniu/accuweather
