# WeatherForecaster

This project aims to collect weather-related data (ie. atmospheric pressure, temperature, humidity and rain presence) in order to provide a weather analysis.

This is a school project involving cloud computing, IoT and AI.


## Requirements:
- Raspberry Pi with Python 3.9+
- [BMP library](https://github.com/adafruit/Adafruit_Python_BMP)
- Python libraries listed in `requirements.txt`
- The [SunFounder Sensor Kit V2 for Raspberry Pi](https://docs.sunfounder.com/projects/sensorkit-v2-pi/en/latest/) with at least:
  - Humiture sensor
  - Barometer (BPM180)
  - Rain detector
- An API token at https://weatherapi.com
- Grafana may be used with the `data.csv` data file

You also need to create an `api_key.py` file containing your WeatherApi token as following:

```py
WEATHER_API_TOKEN = "your token"
```
