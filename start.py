import time
from datetime import datetime
from gatherer import Gatherer
import csv

def register_into_csv(gatherer: Gatherer, datawriter):
    data = gatherer.collect()
    datawriter.writerow([
        datetime.now().isoformat(),
        data['pressure'],
        data['temperature'],
        data['is_raining'],
    ])


def main():
    gatherer = Gatherer()
    with open("data.csv", 'a', encoding="utf8") as csvfile:
        datawriter = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='|',
            quoting=csv.QUOTE_MINIMAL
        )
        while True:
            print("collecting")
            register_into_csv(gatherer, datawriter)
            time.sleep(30)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nClosing script")
