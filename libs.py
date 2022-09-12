from random import randint


STOPPED = 0
MOVING = 1

GREEN = 1
RED = 0

class RoadMap:

    def __init__(self, nx : int = None, ny : int = None, rlength : int = 60):
        
        self.nx = nx
        self.ny = ny
        self.rlength = rlength

        self.intersections = []
        self.ips = []
        self.cars = []

        for each in range(nx):
            each += 1
            for i in range(ny):
                i += 1
                self.intersections.append({
                    'position' : [rlength * each, rlength * i],
                    'up' : GREEN,
                    'down' : GREEN,
                    'left' : GREEN,
                    'right' : GREEN,
                })
                self.ips.append([rlength * each, rlength * i])
        for x in self.intersections:
            print(x)
        for z in self.ips:
            print(z)
        
    def spawncars(self, n : int = 10) -> None:
        for x in range(n):
            vel = randint(1, 6)
            vel = [[vel, 0], [-vel, 0], [0, vel], [0, -vel]][randint(0, 3)]
            self.cars.append({
                'position' : [randint(1, self.nx) * self.rlength, randint(1, self.ny) * self.rlength],
                'velocity' : vel,
                'state' : STOPPED
            })
        print()
        for car in self.cars:
            print(car)
    
    def update(self) -> None:
        for car in self.cars:
            if car['position'] in self.ips:
                car['state'] = MOVING