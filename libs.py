from pickle import STOP
from random import randint
from typing import Tuple

STOPPED = 0
MOVING = 1

GREEN = 1
RED = 0


def mod(x) : return x if x >= 0 else -x
def sign(x) : return 1 if x > 0 else (-1 if x < 0 else 0)


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
                    'up' : RED,
                    'down' : RED,
                    'left' : RED,
                    'right' : RED,
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



class Intersection:

    def __init__(self, center : Tuple[int, int] = None, rlength : int = 60) -> None:
        
        self.lightstate = {
            'up' : RED,
            'down' : RED,
            'left' : RED,
            'right' : RED,
        }

        self.carstate = {
            'up' : [],
            'down' : [],
            'right' : [],
            'left' : []
        }

        self.mapping = {
            (1, 0) : 'left',
            (-1, 0) : 'right',
            (0, 1) : 'up',
            (0, -1) : 'down',
        }

        if center is None: center = (rlength, rlength)

        self.rlength = rlength
        self.center = center
        self.cars = []
        self.t = 0
    
    def categorisecar(self, car):

        [x, y] = car['position']
        
        if x > self.center[0]: self.carstate['right'].append(car)
        elif x < self.center[0]: self.carstate['left'].append(car)
        elif y < self.center[1]: self.carstate['up'].append(car)
        elif y > self.center[1]: self.carstate['down'].append(car)
        else: print("Something's not right I can feel it")
    
    def addcar(self, position : list[int, int], velocity : int,) -> None:
        
        [x, y] = position

        if mod(x - self.center[0]) > self.rlength: raise TypeError(f"Invalid x coordinate of car : {x}")
        if mod(y - self.center[1]) > self.rlength: raise TypeError(f"Invalid y coordinate of car : {y}")

        if x != self.center[0] and y != self.center[1]:
            raise TypeError(f"Car not on a valid road! Either x or y coordinate must be along center of intersection : {(x, y)}")

        direction = (sign(self.center[0] - x), sign(self.center[1] - y))

        car = {
            'position' : [x, y],
            'velocity' : velocity,
            'state' : MOVING,
            'direction' : direction
        }

        self.cars.append(car)
        self.categorisecar(car)
    
    def movecars(self) -> None:
        for car in self.cars:
            if car['state'] == MOVING:
                dir = car['direction']

                xmov, ymov = car['velocity'] * car['direction'][0], car['velocity'] * car['direction'][1]

                [x, y] = car['position']

                if x == self.center[0]:
                    if (mod(ymov) >= mod(y - self.center[1])) and (self.lightstate[self.mapping[dir]] == RED):
                        ymov = self.center[1] - y - car['direction'][1]
                        car['state'] = STOPPED
                else:
                    if (mod(xmov) >= mod(x - self.center[0])) and (self.lightstate[self.mapping[dir]] == RED):
                        xmov = self.center[0] - x - car['direction'][0]
                        car['state'] = STOPPED
                
                car['position'][0] += xmov
                car['position'][1] += ymov

    
    
    def printcars(self):
        print(f"At t = {self.t}")
        for each in self.carstate.keys():
            print(each,':')
            for x in (self.carstate[each]):
                print(x)
    
    def updateframe(self) -> None:
        self.t += 1
        self.movecars()

    def __repr__(self) -> str:
        string = ""

        string += f"Intersection at : {self.center}\n"

        string += f"At t = {self.t},\n"
        for x in self.lightstate.keys():
            string += f"{x} : {['RED', 'GREEN'][self.lightstate[x]]},  "
        string += "\nCars:\n"
        for x in self.carstate.keys():
            string += f"{x} : {len(self.carstate[x])},  "


        lb, lf, rb, rf, ub, uf, db, df = 0, 0, 0, 0, 0, 0, 0, 0


        for car in self.carstate['up']:
            if car['position'][1] == self.center[1] - 1: uf += 1
            elif car['position'][1] < self.center[1] : ub += 1
        
        for car in self.carstate['down']:
            if car['position'][1] == self.center[1] + 1: df += 1
            elif car['position'][1] > self.center[1] : db += 1
        
        for car in self.carstate['left']:
            if car['position'][0] == self.center[0] - 1: lf += 1
            elif car['position'][0] < self.center[0] : lb += 1
        
        for car in self.carstate['right']:
            if car['position'][0] == self.center[0] + 1: rf += 1
            elif car['position'][0] > self.center[0]: rb += 1
        
        syms = [lb, lf, rb, rf, ub, uf, db, df]
        for each in range(len(syms)):
            if syms[each] < 10: syms[each] = '0' + str(syms[each])
            syms[each] = str(syms[each])
        
        [lb, lf, rb, rf, ub, uf, db, df] = syms
        
        lights = [self.lightstate['left'], self.lightstate['right'], self.lightstate['up'], self.lightstate['down']]

        lights = list(map(lambda x: 'G' if x == GREEN else 'R', lights))

        [ll, rl, ul, dl] = lights

        string += f"""

At t = {self.t}
                      |          |
                      |          |
                      |  ┌────┐  |
                      |  | {ub} |  |  
                ┌───┐ |  └────┘  |┌──O──┐
                O {ll} | |  ┌────┐  ||  {ul}  |
                └───┘ |  | {uf} |  |└─────┘
──────────────────────┘  └────┘  └──────────────────────

           ┌────┐┌────┐         ┌────┐┌────┐
           | {lb} || {lf} |         | {rf} || {rb} |
           └────┘└────┘         └────┘└────┘

──────────────────────┐  ┌────┐  ┌──────────────────────
               ┌─────┐|  | {df} |  |┌───┐
               |  {dl}  ||  └────┘  || {rl} O
               └──O──┘|  ┌────┐  |└───┘
                      |  | {db} |  |
                      |  └────┘  |
                      |          |
                      |          |

"""


        return string