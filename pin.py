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
        if mode == PinNumbering.BCM:
            GPIO.setmode(GPIO.BCM)
        else:
            GPIO.setmode(GPIO.BOARD)

    def __init__(self, number:int, mode:PinMode):
        self.number = number
        if mode == PinMode.OUT:
            GPIO.setup(self.number, GPIO.OUT)
        else:
            GPIO.setup(self.number, GPIO.IN)
    
    def high(self):
        GPIO.output(self.number, GPIO.HIGH)
    
    def low(self):
        GPIO.output(self.number, GPIO.LOW)
