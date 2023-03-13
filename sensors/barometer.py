import Adafruit_BMP.BMP085 as BMP085
import time


class BarometerSensor:
    def __init__(self):
        self.sensor = BMP085.BMP085(busnum=1)

    def read_temperature(self) -> float:
        "Returns the capted temperature in °C"
        return self.sensor.read_temperature()

    def read_pressure(self) -> float:
        "Returns the capted pressure in Pascals"
        return self.sensor.read_pressure()


if __name__ == '__main__':
    print('\n Barometer begins...')
    try:
        while True:
            sensor = BarometerSensor()
            temp = sensor.read_temperature()
            pressure = sensor.read_pressure()

            print('')
            print(f"\tTemperature = {temp:0.2f} °C")
            print(f"\tPressure = {pressure:0.2f} Pa")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Script stopped")
