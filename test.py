import time
from json import dumps

from gatherer import Gatherer


def main():
    gatherer = Gatherer()
    try:
        while True:
            print(dumps(gatherer.collect(), indent=2))
            time.sleep(1)
    except KeyboardInterrupt:
        print("Closing script")

if __name__ == "__main__":
    main()
