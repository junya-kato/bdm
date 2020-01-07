from klass import Klass
import random

class Event:
    ALL_KLASS = Klass.create_all()
    def __init__(self, is_goal=False):
        event_seed = random.choice(EVENT_SEEDS)
        self.klass = random.choice(self.ALL_KLASS)
        self.score_delta = event_seed["score_delta"]
        self.reason = event_seed["reason"]
        self.is_goal = is_goal

EVENT_SEEDS = [
    {"score_delta": -10, "reason": "一限寝ぶっちした。"},
    {"score_delta": 20, "reason": "気に入られた。"},
    {"score_delta": -5, "reason": "遅刻した。"},
    {"score_delta": 5, "reason": "出席した。"},
]