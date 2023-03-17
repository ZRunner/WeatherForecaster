import datetime
import os
import csv
import requests

from api_key import WEATHER_API_TOKEN
from weather_api_typing import ApiAnswer, ApiCurrentWeather, ApiWeatherCondition

CITY = "45.485,-73.620"
FILE_NAME = os.path.dirname(__file__) + "/conditions.csv"


def get_data_from_api() -> ApiAnswer:
    url = "https://api.weatherapi.com/v1/current.json?"
    r = requests.get(url, params={
        "key": WEATHER_API_TOKEN,
        "q": CITY,
    })
    r.raise_for_status()
    return r.json()

def write_file_headers(datawriter):
    datawriter.writerow([
        "datetime",
        "condition-text",
        "condition-code",
        "precipitations",
        "is_day",
    ])

def register_into_csv(datawriter, last_updated: datetime.datetime, weather: ApiCurrentWeather):
    datawriter.writerow([
        last_updated.isoformat(),
        weather['condition']['text'],
        weather['condition']['code'],
        weather["precip_mm"],
        weather["is_day"] == 1,
        
    ])

def get_writer(file):
    return csv.writer(
        file,
        delimiter=',',
        quotechar='|',
        quoting=csv.QUOTE_MINIMAL
    )

def main():
    # write headers if new file
    if not os.path.isfile(FILE_NAME):
        print("Creating data file")
        with open(FILE_NAME, 'w', encoding="utf8") as csvfile:
            writer = get_writer(csvfile)
            write_file_headers(writer)
    # Collect API data
    print("Collecting data...")
    data = get_data_from_api()["current"]
    last_updated = datetime.datetime.fromtimestamp(data["last_updated_epoch"])
    # write it into the file
    with open(FILE_NAME, 'a', encoding="utf8") as csvfile:
        datawriter = get_writer(csvfile)
        register_into_csv(
            datawriter,
            last_updated=last_updated,
            weather=data
        )

if __name__ == "__main__":
    main()
    print("Script finished")