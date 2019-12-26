from motor import Motor
from belt import Belt
from koma import Koma
from course import Course

class GameController:
    def __init__(self):
        Pin.setmode(PinNumbering.BCM)
        motor = Motor(A1=4, A2=17, B1=27, B2=22)
        belt = Belt(motor=motor)
        self.koma = Koma(belt=belt)
        self.course = Course()

    def step(self, steps):
        self.koma.step(steps, course=self.course)
