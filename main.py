from game_controller import GameController
from flask import Flask, render_template
app = Flask(__name__)

game_controller = GameController()

@app.route("/")
def hello():
    return render_template("index.html", steps=0)#"Hello World!"

@app.route("/step/<int:steps>")
def step(steps):
    game_controller.step(steps)
    return render_template("index.html", steps=steps)#"move {} steps".format(steps)

@app.route("/round")
def rounding():
    game_controller.round()
    return "rounding"

@app.route("/move/<int:distance>")
def move(distance):
    game_controller.move(distance)
    return "move {}".format(distance)

if __name__ == "__main__":
    app.run("0.0.0.0")
