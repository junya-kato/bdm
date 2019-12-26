from RPi import GPIO
from enum import Enum

class PinNumbering(Enum):
    BCM = GPIO.BCM
    BOARD = GPIO.BOARD

class PinMode(Enum):
    OUT = GPIO.OUT
    IN = GPIO.IN

class Pin:
    @classmethod
    def setmode(cls, mode:PinNumbering):
        GPIO.setmode(GPIO.BCM)

    def __init__(self, number:int, mode:PinMode):
        self.number = number
        GPIO.setup(self.number, mode)
    
    def high(self):
        GPIO.output(self.number, GPIO.HIGH)
    
    def low(self):
        GPIO.output(self.number, GPIO.LOW)
