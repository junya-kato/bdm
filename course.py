class Course:
    STEPS = [30,30,30,30,30,30,30]

    def distance(self, start:int, end:int):
        return sum(self.STEPS[start:end])
