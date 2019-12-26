from motor import Motor

class Belt:
    SPEED = 90 # deg/sec
    def __init__(self, motor:Motor):
        self.motor = motor
    
    def forward(self, distance: float): # distance[mm]
        deg = self.__deg_from(distance)
        duration = self.__duration_from(deg)
        self.motor.move(deg=deg, duration=duration)
    
    def __deg_from(self, distance:int): # distance[mm]
        return distance*4.42913385 # 360/12/5.08 (360/歯数/ピッチ長)
    
    def __duration_from(self, deg:int):
        return deg/self.SPEED
