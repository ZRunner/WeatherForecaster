from typing import TypedDict

from sensors.barometer import BarometerSensor
from sensors.rain_detector import RainDetector

class DataDict(TypedDict):
    is_raining: bool
    temperature: float
    pressure: float


class Gatherer:
    def __init__(self):
        self.barometer = BarometerSensor()
        self.rain_detector = RainDetector()
    
    def collect(self) -> DataDict:
        return {
            "is_raining": self.rain_detector.is_raining(),
            "temperature": self.barometer.read_temperature(),
            "pressure": self.barometer.read_pressure(),
        }
