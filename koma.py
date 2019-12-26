from belt import Belt
from course import Course

class Koma:
    def __init__(self, belt:Belt):
        self.belt = belt
        self.pos = 0

    def step(self, steps: int, course:Course):
        start = self.pos
        end = self.pos + steps
        distance = course.distance(start, end)
        self.belt.forward(distance)
        self.pos += steps
