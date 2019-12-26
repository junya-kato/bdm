from game_controller import GameController
from flask import Flask
app = Flask(__name__)

game_controller = GameController()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/step/<int:steps>")
def step(steps):
    game_controller.step(steps)
    return "move {} steps".format(steps)

if __name__ == "__main__":
    app.run()
