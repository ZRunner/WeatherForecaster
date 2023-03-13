#!/usr/bin/env python3
import time

from . import PCF8591 as ADC
import RPi.GPIO as GPIO


class RainDetector:
    def __init__(self, pin: int = 17):
        self.DO = pin
        GPIO.setmode(GPIO.BCM)
        ADC.setup(0x48)
        GPIO.setup(self.DO, GPIO.IN)
    
    def is_raining(self) -> bool:
        return not GPIO.input(self.DO)

if __name__ == '__main__':
    sensor = RainDetector()
    try:
        status = True
        while True:
            tmp = sensor.is_raining()
            if tmp != status:
                if tmp:
                    print("Raining!")
                else:
                    print("Not raining!")
                status = tmp

            time.sleep(0.2)
    except KeyboardInterrupt:
        pass