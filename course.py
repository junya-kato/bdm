class Course:
    STEPS = [45,60,80,60,60,40,50, 30, 80, 90, 50, 45]

    def distance(self, start:int, end:int):
        return sum(self.STEPS[start:end])
