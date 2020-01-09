#! /usr/bin/python3

from game_controller import GameController
from flask import Flask, render_template, request
from random import random
import threading
app = Flask(__name__)

game_controller = GameController()

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/step/<int:steps>")
def step(steps):
    game_controller.step_async(steps)
    return render_template("index.html", steps=steps)#"move {} steps".format(steps)

@app.route("/round")
def rounding():
    game_controller.round()
    return "rounding"

round_thread  = threading.Thread(target=game_controller.round)

@app.route("/admin")
def admin():
    global round_thread, game_controller
    if (request.args.get("forward") == "true"):
        game_controller.move(2)
    if (request.args.get("round") == "true"):
        if not round_thread.is_alive():
            round_thread.start()
    if (request.args.get("killround") == "true"):
        game_controller.can_round = False
        round_thread.join()
        game_controller.can_round = True
        round_thread  = threading.Thread(target=game_controller.round)
    if (request.args.get("reset") == "true"):
        game_controller = GameController()
    return render_template("admin.html")

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
