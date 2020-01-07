import random

class Klass:
    @classmethod
    def create_all(cls):
        return [
            Klass("ソフトウェア1","川原"),
            Klass("電子回路II","三田"),
            Klass("分散システム","落合"),
            Klass("ネットワーク工学","江崎"),
        ]

    def __init__(self, name, professor):
        self.name = name
        self.professor = professor

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
