from typing import Literal, TypedDict

class ApiLocation(TypedDict):
    name: str
    region: str
    country: str
    lat: float
    lon: float
    tz_id: str
    localtime_epoch: int
    localtime: str

class ApiWeatherCondition(TypedDict):
    text: str
    icon: str
    code: int

class ApiCurrentWeather(TypedDict):
    last_updated_epoch: int
    last_updated: str
    temp_c: int
    temp_f: float
    is_day: Literal[0, 1]
    condition: ApiWeatherCondition
    wind_mph: float
    wind_kph: int
    wind_degree: int
    wind_dir: str # 16-points compass
    pressure_mb: int # millibars
    pressure_in: float
    precip_mm: int
    precip_in: float
    humidity: int # percent 0-100
    cloud: int # percent 0-100
    feelslike_c: float
    feelslike_f: float
    vis_km: int
    vis_miles: int
    uv: float
    gust_mph: float
    gust_kph: float

class ApiAnswer(TypedDict):
    location: ApiLocation
    current: ApiCurrentWeather
