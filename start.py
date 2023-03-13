import time
from gatherer import Gatherer
import csv

def register_into_csv(gatherer: Gatherer, datawriter: csv._writer):
    data = gatherer.collect()
    datawriter.writerow([
        time.time(),
        data['pressure'],
        data['temperature'],
        data['is_raining'],
    ])


def main():
    gatherer = Gatherer()
    with open("data.csv", 'wa', encoding="utf8") as csvfile:
        datawriter = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='|',
            quoting=csv.QUOTE_MINIMAL
        )
        while True:
            register_into_csv(gatherer, datawriter)
            time.sleep(10)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nClosing script")
