import random

MEMBERS = ["ソフトウェア1　川原", "電子回路II　三田", "分散システム　落合", "ネットワーク工学　江崎"]

class Professor:
    def name(self):
        n = random.randint(0, len(MEMBERS)-1)
        return MEMBERS[n]

    def score(self):
        return random.randint(0, 100)

    def grade(self, score):
        if(score >= 90):
            return "優上"
        elif(score >= 80):
            return "優"
        elif(score >= 65):
            return "良"
        elif(score >= 50):
            return "可"
        else:
            return "不可"
