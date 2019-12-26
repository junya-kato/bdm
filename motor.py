from pin import Pin, PinMode, PinNumbering
from time import sleep

class Motor:
    def __init__(self, A1:int, A2:int, B1:int, B2:int, speed = 1):
        self.pinA1 = Pin(A1, PinMode.OUT)
        self.pinA2 = Pin(A2, PinMode.OUT)
        self.pinB1 = Pin(B1, PinMode.OUT)
        self.pinB2 = Pin(B2, PinMode.OUT)

    def move(self, deg: float, duration: float):
        """
        move counter clockwise
        """
        if deg == 0:
            sleep(duration)
            return

        steps = int(deg*100/360)
        step_duration = duration / steps

        if(steps < 0):
            stepper = self.__step_cw
        else:
            stepper = self.__step_ccw

        for _ in range(abs(steps)):
            stepper(step_duration)
    
    def __step_ccw(self, duration:float):
        wait_time = duration / 4
        if not (0.01 <= wait_time <= 0.5):
            raise "not suitable duration for this moter"
        self.pinB1.high()
        sleep(wait_time)
        self.pinA1.high()
        sleep(wait_time)
        self.pinB1.low()
        sleep(wait_time)
        self.pinA1.low()
        sleep(wait_time)

    def __step_cw(self, duration:float):
        wait_time = duration / 4
        if not (0.01 < wait_time < 0.5):
            raise "not suitable duration for this moter"
        self.pinA1.high()
        sleep(wait_time)
        self.pinB1.high()
        sleep(wait_time)
        self.pinA1.low()
        sleep(wait_time)
        self.pinB1.low()
        sleep(wait_time)
