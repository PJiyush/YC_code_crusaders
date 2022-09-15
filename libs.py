from random import randint
from typing import Tuple
from copy import deepcopy

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
    
    def getlightstate(self) -> dict:
        return deepcopy(self.lightstate)
    
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
            'direction' : direction,
            'exited' : False,
            'atintersection' : False,
        }

        self.cars.append(car)
        self.categorisecar(car)
    
    def movecars(self) -> None:
        for car in self.cars:
            if (car['state'] == MOVING) and not car['exited']:
                dir = car['direction']

                xmov, ymov = car['velocity'] * car['direction'][0], car['velocity'] * car['direction'][1]

                [x, y] = car['position']

                if x == self.center[0]:
                    if (mod(ymov) >= mod(y - self.center[1])) and (self.lightstate[self.mapping[dir]] == RED):
                        ymov = self.center[1] - y - car['direction'][1]
                        car['state'] = STOPPED
                        car['atintersection'] = True
                else:
                    if (mod(xmov) >= mod(x - self.center[0])) and (self.lightstate[self.mapping[dir]] == RED):
                        xmov = self.center[0] - x - car['direction'][0]
                        car['state'] = STOPPED
                        car['atintersection'] = True
                
                car['position'][0] += xmov
                car['position'][1] += ymov
    
    def updateexits(self):
        for car in self.cars:
            dir = car['direction']
            [x, y] = car['position']

            if dir == (1, 0):
                if x >= self.center[0]:
                    car['exited'] = True
                    car['atintersection'] = False
            elif dir == (-1, 0):
                if x <= self.center[0]:
                    car['exited'] = True
                    car['atintersection'] = False
            elif dir == (0, 1):
                if y >= self.center[1]:
                    car['exited'] = True
                    car['atintersection'] = False
            elif dir == (0, -1):
                if y <= self.center[1]:
                    car['exited'] = True
                    car['atintersection'] = False

    
    
    def printcars(self):
        print(f"At t = {self.t}")
        for each in self.carstate.keys():
            print(each,':')
            for x in (self.carstate[each]):
                print(x)
    
    def updateframe(self, t : int = None) -> None:
        if t is None:
            self.t += 1
            self.movecars()
        else:
            for each in range(t): self.movecars()
            self.t += t
        self.updateexits()

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

           ┌────┐┌────┐          ┌────┐┌────┐
           | {lb} || {lf} |          | {rf} || {rb} |
           └────┘└────┘          └────┘└────┘

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
    
    def getcars(self) -> dict:
        return deepcopy(self.carstate)
    
    def getstoppedcars(self) -> dict:
        sc = deepcopy(self.carstate)
        for x in sc.keys():
            sc[x] = list(filter(lambda y: y['state'] == STOPPED, sc[x]))
        return sc
    
    def getcarsatintersection(self) -> dict:
        cai = deepcopy(self.carstate)
        for each in cai.keys():
            cai[each] = list(filter(lambda x: x['atintersection'] == True, cai[each]))
        return cai
    
    def getcarsthatare(self, condition) -> dict:
        cts = deepcopy(self.carstate)

        for each in cts.keys():
            cts[each] = list(filter(condition, cts[each]))

        return cts
    
    def getcarsinlane(self, lane : str, onlyatintersection : bool = False) -> list:
        cars = deepcopy(self.carstate[lane])

        cars = list(filter(lambda x: (x['exited'] == False) and (x['atintersection'] if onlyatintersection else True), cars))

        return cars

    
    def setlight(self, light : str, state : GREEN | RED):
        self.lightstate[light] = state
        # for car in self.carstate[light]:
        #     if not car['exited']:
        #         car['state'] = state
        #         car['atintersection'] = bool(state)
        cai = self.carstate[light].copy()
        cai = list(filter(lambda x: x['atintersection'] == True, cai))
        for car in cai:
            car['state'] = state
    
    def green(self, light : str):
        self.setlight(light, GREEN)
    
    def red(self, light : str):
        self.setlight(light, RED)
    
    #note this is only for testing purposes
    def spawncars(self, n : int = 5):
        for i in range(n):
            self.addcar(
                position = [4 * randint(1, 4) , self.center[1]],
                velocity = randint(1, 6)
            )
            self.addcar(
                position = [(2 * self.center[0]) - (4 * randint(1, 4)) , self.center[1]],
                velocity = randint(1, 6)
            )
            self.addcar(
                position = [self.center[0], 4 * randint(1, 4)],
                velocity = randint(1, 6)
            )
            self.addcar(
                position = [self.center[0], (2 * self.center[1]) - (4 * randint(1, 4))],
                velocity = randint(1, 6)
            )


class SimpleCycle:

    def __init__(self, inter : Intersection, period : int = 10, clockwise : bool = True) -> None:
        self.inter = inter
        self.period = period
        self.clockwise = True
        self.order = ['up', 'right', 'down', 'left']
        if not clockwise: self.order = self.order[::-1]

        self.record = []
    
    def getrecord(self) -> list:
        return self.record
    
    def runsimulation(self, endtime : int = 100, verbose : bool = False, debug : bool = False) -> float:
        self.record = []
        waitedtime = 0

        pointer = 0

        self.inter.green(self.order[0])

        for each in range(endtime):
            if debug: print(f"each = {each}, t = {self.inter.t}")

            self.record.append(deepcopy(self.inter.getcars()))

            if ((each % self.period) == 0) and (each != 0):
                self.inter.red(self.order[pointer % 4])
                pointer += 1
                self.inter.green(self.order[pointer % 4])
                if verbose: print(self.inter)

            if debug:
                print(self.inter)
                self.inter.printcars()
                print(f"Stopped cars : {len(self.inter.getstoppedcars())}")
                wait = input("Enter to move forward: ")
                print()
                print()

            waitedtime += len(self.inter.getstoppedcars())
            self.inter.updateframe()
        
        average = waitedtime/len(self.inter.getcars())
        return average


class NetworkAlgorithm:

    def __init__(self, inter : Intersection, onlyatintersection : bool = True, thresh : int = 10) -> None:
        
        self.inter = inter
        self.onlywaiting = onlyatintersection
        self.record = []
        self.thresh = thresh
    
    def getpriority(cars : dict, onlyatintersection : bool = True) -> list:
        p = list(map(
            lambda x: (x, len(
                list(filter(
                    lambda y: (y['exited'] == False) and (y['atintersection'] if onlyatintersection else True),
                    cars[x]
                ))
            )),
            cars.keys()))
        p.sort(key=lambda x: x[1], reverse = True)
        p = list(map(lambda x: x[0], p))
        return p
    
    def getrecord(self, listform : bool = False) -> list:
        if listform:
            record = []
            for each in self.record:
                record.append(
                    each['up'] + each['down'] + each['left'] + each['right']
                )
            return record
        return self.record

    

    def runsimulation(self, endtime : int = 100, debug : bool = False, record : bool = True) -> float:
        if record : self.record = []
        waitedtime = 0

        done = []

        lastopenlane = 'up'
        self.inter.green('up')
        pointer = 0

        for i in range(endtime):

            if record: self.record.append(deepcopy(self.inter.getcars()))
            
            if debug: print(f"i = {i}, t = {self.inter.t}, {done}")

            if (i - pointer >= self.thresh) or (self.inter.getcarsatintersection()[lastopenlane] == []):
                if debug: print(f"triggered at {self.inter.t}\n")
                
                if len(done) == 3: done = []
                

                # try: self.inter.red(lastlaneopen)
                # except KeyError: pass

                self.inter.red(lastopenlane)

                priority = NetworkAlgorithm.getpriority(self.inter.getcars(), self.onlywaiting)

                priority = list(filter(lambda x: x not in done, priority))

                self.inter.green(priority[0])

                lastopenlane = priority[0]

                done.append(priority[0])
                
                pointer = i

            waitedtime += len(self.inter.getstoppedcars())
            self.inter.updateframe()

            if debug:
                print(self.inter)
                self.inter.printcars()
                print(f"Stopped cars : {len(self.inter.getstoppedcars())}")
                wait = input("Enter to move forward: ")
                print()
                print()

        
        avg = waitedtime/len(self.inter.getcars())
        return avg