from typing import TypedDict

from sensors.barometer import BarometerSensor
from sensors.humiture import HumitureSensor
from sensors.rain_detector import RainDetector

class DataDict(TypedDict):
    is_raining: bool
    temperature: float
    pressure: float


class Gatherer:
    def __init__(self):
        self.barometer = BarometerSensor()
        self.humiture = HumitureSensor()
        self.rain_detector = RainDetector()
    
    def collect(self) -> DataDict:
        if data := self.humiture.read_data():
            humidity = data[0]
        else:
            humidity = None
        return {
            "is_raining": self.rain_detector.is_raining(),
            "temperature": self.barometer.read_temperature(),
            "pressure": self.barometer.read_pressure(),
            "humidity": humidity,
        }
