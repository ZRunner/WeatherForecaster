import csv
import os
import time
from datetime import datetime

from gatherer import Gatherer

FILE_NAME = os.path.dirname(__file__) + "/data.csv"


def write_file_headers(datawriter):
    datawriter.writerow([
        "datetime",
        "pressure",
        "temperature",
        "humidity",
        "is_raining",
    ])

def register_into_csv(gatherer: Gatherer, datawriter):
    data = gatherer.collect()
    datawriter.writerow([
        datetime.now().isoformat(),
        data['pressure'],
        data['temperature'],
        data['humidity'],
        data['is_raining'],
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
    # start collecting data
    gatherer = Gatherer()
    while True:
        print("collecting")
        with open(FILE_NAME, 'a', encoding="utf8") as csvfile:
            datawriter = get_writer(csvfile)
            register_into_csv(gatherer, datawriter)
        time.sleep(30)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nClosing script")
