"""
"""

from typing import Any, Dict, Optional
from attrs import define, field


@define
class WeatherInfo:
    update_time: str
    humidity: int
    precip: int
    pressure: int
    vis: int
    cloud: int
    sources: str
    uv_index: int


@define
class WeatherDayForecastInfo(WeatherInfo):
    update_time: str
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
    def from_dict(cls, data: Dict[str, Any]) -> "WeatherDayForecastInfo":
        d = data["daily"]
        return cls(
            update_time=data["updateTime"],
            fx_link=data["fxLink"],
            fx_date=d["fxDate"],
            sun_rise=d["sunrise"],
            sun_set=d["sunset"],
            moon_rise=d["moonrise"],
            moon_set=d["moonset"],
            moon_phase=d["moonPhase"],
            moon_phase_icon=d["moonPhaseIcon"],
            temp_max=d["tempMax"],
            temp_min=d["tempMin"],
            icon_day=d["iconDay"],
            text_day=d["textDay"],
            wind_360_day=d["wind360Day"],
            wind_dir_day=d["windDirDay"],
            wind_scale_day=d["windScaleDay"],
            wind_speed_day=d["windSpeedDay"],
            wind_360_night=d["wind360Night"],
            wind_dir_night=d["windDirNight"],
            wind_scale_night=d["windScaleNight"],
            wind_speed_night=d["windSpeedNight"],
            precip=int(d["precip"]),
            humidity=int(d["humidity"]),
            pressure=int(d["pressure"]),
            vis=int(d["vis"]),
            cloud=int(d["cloud"]),
            sources=data["refer"]["sources"],
        )


@define
class WeatherNow(WeatherInfo):
    obs_time: str
    temp: int
    feels_like: int
    icon: str
    text: str
    wind_360: int
    wind_dir: str
    wind_scale: str
    wind_speed: int
    dew: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "WeatherNow":
        d = data["now"]
        return cls(
            obs_time=d["obsTime"],
            temp=int(d["temp"]),
            feels_like=int(d["feelsLike"]),
            icon=d["icon"],
            text=d["text"],
            wind_360=d["wind360"],
            wind_dir=d["windDir"],
            wind_scale=d["windScale"],
            wind_speed=d["windSpeed"],
            humidity=int(d["humidity"]),
            precip=int(d["precip"]),
            pressure=int(d["pressure"]),
            vis=int(d["vis"]),
            cloud=int(d["cloud"]),
            dew=int(d["dew"]),
            resources=data["refer"]["sources"]
        )
