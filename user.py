import random
from event import Event
from course import Course

class User:
    def __init__(self, koma):
        self.pos = 0
        self.score = 0
        self.koma = koma
    
    def step(self, steps, course):
        self.koma.step_async(steps, course=course)
        if self.will_goal(steps):
            event = Event(is_goal=True)
        else:
            event = Event()
            self.__update_user(steps=steps, event=event)
        return event
    
    def __update_user(self, steps, event):
        self.pos += steps
        self.score += event.score_delta

    def will_goal(self, steps):
        return (steps + self.pos) >= Course.STEP_LEN