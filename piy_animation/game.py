
import pygame as pyg
pyg.init()

# suppose 4 cars are in lane1-->(1,0)
alpha = (1,0)
beta = (0,1)
gamma = (-1,0)
delta = (0,-1)

A = []
n_alpha = 3
n_beta = 4
for i in range(n_alpha):
    A.append(alpha)
for i in range(n_beta):
    A.append(beta)

win = pyg.display.set_mode((1460,750))
bg = pyg.image.load('bg.png')
pyg.display.set_caption("Cars_sim")
run =True

cars_images = [pyg.image.load('blue_car.png'),pyg.image.load('purple_car.png'),]

class cars():
    def __init__(self,x,y,location,num): # position, location-->(), state, velocity --> thinking to omit state and thinking to make velocity constant
        self.x = x
        self.y = y
        self.velocity  = 10
        self.state = 1
        self.image = cars_images[num]
        first = location[0]
        second = location[1]
        if(first==1 and second==0):
            self.lane = 1
            self.image = pyg.transform.rotate(self.image,270)
            
        elif(first==0 and second==1):
            self.lane = 2
            self.image = pyg.transform.rotate(self.image,180)
            
        elif(first==-1 and second==0):
            self.lane = 3
            self.image = pyg.transform.rotate(self.image,90)
            
            
        else:
            self.lane = 4
            self.image = self.image
            
    def draw(self,win):
            win.blit(self.image,(self.x, self.y))
    
    def movement(self,end):   # for movement in lane 1
        if(self.lane==1):
            self.path = [self.x,end]
            if(self.x<end+self.velocity):
                self.x+=self.velocity
        if(self.lane==2):
            self.path = [self.y,end]
            if(self.y<end+self.velocity):
                self.y+=self.velocity
        if(self.lane==3):
            self.path = [self.x,end]
            if(self.x>end+self.velocity):
                self.x -= self.velocity
        if(self.lane==4):
            self.path = [self.y,end]
            if(self.y> end+ self.velocity):
                self.y -= self.velocity


# here remeber that the velocity is nothing but the distance



def updatingGameWin():
    # win.fill((0,0,0))
    win.blit(bg, (0,0))
    car1.draw(win)
    car2.draw(win)
    car3.draw(win)
    car4.draw(win)
    pyg.display.update()

car1 = cars(12,319,alpha,0)
car2 = cars(748,16,beta,0)
car3 = cars(1440,340,gamma,1)
car4 = cars(707,725,delta,1)

while(run==True):
    pyg.time.delay(100)
    for event in pyg.event.get():
        if(event.type == pyg.QUIT):
            run = False

    car1.movement(358)
    car2.movement(303)
    car3.movement(600)
    car4.movement(500)

    updatingGameWin()
