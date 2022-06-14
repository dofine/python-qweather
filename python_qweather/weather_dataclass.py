"""
"""
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class WeatherDayForecastInfo:
    fx_link: str
    fx_date: str
    sun_rise: str
    sun_set: str
    moon_rise: str
    moon_set: str
    moon_phase: str
    moon_phase_icon: str
    temp_max: int
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
    precip: float  # 总降水量，毫米
    uv_index: int  # 紫外线指数
    humidity: int  # 相对湿度，百分比数值
    press: int  # 大气压，百帕
    vis: int  # 能见度，公里
    cloud: int  # 云量，百分比数值
    sources: str  # 数据来源

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "WeatherDayForecastInfo":
        return cls(fx_link=data["fxLink"], fx_date=data["daily"]["fxDate"])
