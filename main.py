from motor import Motor
from time import sleep

if __name__ == "__main__":
    Pin.setmode(PinNumbering.BCM)
    motor = Motor(A1=4, A2=17, B1=27, B2=22)
    while True:
        sleep(1)
        motor.move(90, 1)
