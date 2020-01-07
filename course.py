class Course:
    # 最終マスはゴールマス。
    # STEPS = [45,60,80,60,60,40,50, 30, 80, 90, 50, 45]
    STEPS = [45,60,80,20,40,30,40]
    STEP_LEN = len(STEPS)

    def distance(self, start:int, end:int):
        return sum(self.STEPS[start:end])
