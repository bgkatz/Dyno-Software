
class roadLoad():
    def __init__(self, j, c1, c2):
        self.j = j
        self.c1 = c1
        self.c2 = c2
    def updateSpeed(torque, currentSpeed, dt):
        netTorque = torque - (currentSpeed/abs(currentSpeed))*self.c1 - currentSpeed*self.c2
        acceleration = netTorque/self.j
        nextSpeed = currentSpeed + acceleration*dt
        return nextSpeed