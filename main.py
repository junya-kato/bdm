from game_controller import GameController
from flask import Flask, render_template
from random import random
from professor import Professor
app = Flask(__name__)

game_controller = GameController()
professor = Professor()

@app.route("/")
def hello():
    return render_template("index.html", steps=0)#"Hello World!"

@app.route("/step/<int:steps>")
def step(steps):
    game_controller.step_async(steps)
    return render_template("index.html", steps=steps)#"move {} steps".format(steps)

@app.route("/round")
def rounding():
    game_controller.round()
    return "rounding"

@app.route("/random")
def randomstep():
    steps = int(1 + random()*6)
    game_controller.step_async(steps)
    teacher = professor.name()
    score = professor.score()
    grade = professor.grade(score)
    return render_template("index.html",steps=steps, teacher=teacher, score=score, grade=grade)

@app.route("/move/<int:distance>")
def move(distance):
    game_controller.move_async(distance)
    return "move {}".format(distance)

if __name__ == "__main__":
    app.run("0.0.0.0")
