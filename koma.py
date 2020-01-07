from belt import Belt
from course import Course
import threading

class Koma:
    def __init__(self, belt:Belt):
        self.belt = belt
        self.pos = 0

    def step_async(self, steps: int, course: Course):
        threading.Thread(target=self.step, args=(steps,course)).start()

    def step(self, steps: int, course:Course):
        start = self.pos
        end = self.pos + steps
        distance = course.distance(start, end)
        self.belt.forward(distance)
        self.pos += steps
