from motor import Motor
from belt import Belt
from koma import Koma
from pin import Pin, PinNumbering
from course import Course
import threading

class GameController:
    def __init__(self):
        Pin.setmode(PinNumbering.BCM)
        self.motor = Motor(A1=4, A2=17, B1=27, B2=22)
        self.belt = Belt(motor=self.motor)
        self.koma = Koma(belt=self.belt)
        self.course = Course()
    
    def round(self):
        while(True):
            self.motor.move(90, 1)

    def move_async(self, distance):
        threading.Thread(target=self.move, args=(distance, )).start()

    def move(self, distance):
        self.belt.forward(distance)

    def step_async(self, steps):
        threading.Thread(target=self.step, args=(steps, )).start()

    def step(self, steps):
        self.koma.step(steps, course=self.course)
