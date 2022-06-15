"""
"""

from typing import Any, Optional
from attrs import define, field


@define
class WeatherInfo:
    # obs_time: str
    # temp: int
    # feels_like: int
    # icon: str
    # weather_text: str
    # wind_360: int
    # wind_dir: str
    # wind_scale: str
    humidity: int
    precip: int
    pressure: int
    vis: int
    cloud: int
    dew: int
    sources: str


@define
class WeatherDayForecastInfo(WeatherInfo):
    obs_time: str
    fx_date: str
    sun_rise: str
    sun_set: str
    moon_rise: str
    moon_set: str
    moon_phase: str
    moon_phase_icon: str
    temp_max: int = field(order=True)
    temp_min: int
    icon_day: str
    text_day: str
    icon_night: str
    text_night: str
    wind_360_day: int  # 白天风向360角
    wind_dir_day: str  # 白天风向
    wind_scale_day: str  # 白天风力等级
    wind_speed_day: int  # 白天风速，公里/小时
    wind_360_night: int
    wind_dir_night: str
    wind_scale_night: str
    wind_speed_night: int


    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "WeatherDayForecastInfo":
        return cls(fx_link=data["fxLink"], fx_date=data["daily"]["fxDate"])
    
    
