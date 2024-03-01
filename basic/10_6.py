class Laser():
    def does(self):
        return 'distintegrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self):
        self.laser=Laser()
        self.claw=Claw()
        self.smartphone=SmartPhone()
    def does(self):
        return (f'Laser {self.laser.does()} , Claw {self.claw.does()} , SmartPhone {self.smartphone.does()}')
robot=Robot()
print(robot.does())