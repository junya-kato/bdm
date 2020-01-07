from game_controller import GameController
from flask import Flask, render_template
from random import random
app = Flask(__name__)

game_controller = GameController()

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
    event = game_controller.step(steps)
    user = game_controller.user
    return render_template("index.html",event=event, user=user, steps=steps)

@app.route("/move/<int:distance>")
def move(distance):
    game_controller.move_async(distance)
    return "move {}".format(distance)

if __name__ == "__main__":
    app.run("0.0.0.0")
