from operator import truediv
from tkinter import Y
from turtle import Screen
from typing_extensions import Self
from libs import *
import pygame as pyg
pyg.init()

screen = pyg.display.set_mode((1460,750))

# for background
horizontal_track = {'yUpL': (0,307), 'yUpR': (1460,307), 'yDownL': (0,443), 'yDownR': (1460,443)}
vertical_track = {'xLeftU': (662,0), 'xLeftD': (662,750), 'xRightU': (798,0), 'xRightD': (798,750)}


# cars
cars_images = [pyg.image.load('blue_car.png'),pyg.image.load('purple_car.png'),pyg.image.load('red_car.png'),pyg.image.load('yellow_car.png')]

def Background(x:dict):
    
    screen.fill((255,255,255))
    pyg.draw.line(screen, (0,0,0), horizontal_track['yUpL'], horizontal_track['yUpR'],5)
    pyg.draw.line(screen, (0,0,0), horizontal_track['yDownL'], horizontal_track['yDownR'],5)
    pyg.draw.line(screen, (0,0,0), vertical_track['xLeftU'], vertical_track['xLeftD'],5)
    pyg.draw.line(screen, (0,0,0), vertical_track['xRightU'], vertical_track['xRightD'],5)
    if(x['left']==1):
        screen.blit(traffic_signal_images_left[1],traffic_signal_cordinates['left'])
    elif(x['left']==0):
        screen.blit(traffic_signal_images_left[0],traffic_signal_cordinates['left'])
    
    if(x['up']==1):
        screen.blit(traffic_signal_images_up[1],traffic_signal_cordinates['up'])
    elif(x['up']==0):
        screen.blit(traffic_signal_images_up[0],traffic_signal_cordinates['up'])
    
    if(x['right']==1):
        screen.blit(traffic_signal_images_right[1],traffic_signal_cordinates['right'])
    elif(x['right']==0):
        screen.blit(traffic_signal_images_right[0],traffic_signal_cordinates['right'])
    
    if(x['down']==1):
        screen.blit(traffic_signal_images_down[1],traffic_signal_cordinates['down'])
    elif(x['down']==0):
        screen.blit(traffic_signal_images_down[0],traffic_signal_cordinates['down'])
    
    pyg.display.update()

traffic_signal_cordinates ={
    'left':(580,220),
    'up':(810,230),
    'right':(810, 450),
    'down': (580,450)
}

def updatingGameWin():
    # win.fill((0,0,0))
    # screen.blit(, (0,0))
    # clock1.tick(60)
    car1.draw(screen)
    # car2.draw(win)
    # car3.draw(win)
    # car4.draw(win)
    pyg.display.update()


class cars():
    def __init__(self,x,y,location,num): 
        self.x = x
        self.y = y
        self.velocity  = 10
        # self.state = state
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
            
    def draw(self):
            screen.blit(self.image,(self.x, self.y))
    
    def movement(self,end,state):   # for movement in lane 1
        self.state = state
        if(self.lane==1 and self.state==1):
            self.path = [self.x,end]
            if(self.x<end+self.velocity ):
                self.x+=(self.velocity)/2
        if(self.lane==2 and self.state==1):
            self.path = [self.y,end]
            if(self.y<end+self.velocity):
                self.y+=(self.velocity)/2
        if(self.lane==3 and self.state==1):
            self.path = [self.x,end]
            if(self.x>end+self.velocity):
                self.x -= (self.velocity)/2
        if(self.lane==4 and self.state==1):
            self.path = [self.y,end]
            if(self.y> end+ self.velocity):
                self.y -= (self.velocity)/2

traffic_signal_images_left = [pyg.image.load('red_light.png'), pyg.image.load('green light.png')]
traffic_signal_images_up = [pyg.image.load('red_light up.png'), pyg.image.load('green light up.png')]
traffic_signal_images_right = [pyg.image.load('red_light right.png'), pyg.image.load('green light right.png')]
traffic_signal_images_down = [pyg.image.load('red_light down.png'), pyg.image.load('green light down.png')]

# here we are going to operate traffic lights
hello = Intersection()
# x = hello.getlightstate()
# hello.green('left')
# x = hello.getlightstate()
# hello.red('left')
# hello.green('up')
# x = hello.getlightstate()

i = Intersection()
i.spawncars(5)
algo = SimpleCycle(i, period = 4)
algo.runsimulation(endtime = 100, record=True)
x = algo.getrecord(True)
# x= x[0]




clock = pyg.time.Clock()
car1 = cars(32,58,(1,0),0)
run =True
count =0
A = ['left','up','right','down']
t1 = 1
t2 = 2
t3 = 3
t4 = 4
# while(run==True and count<t3 and count>=0):   # here I have to put condition on the basis of time
while(run==True ):   # here I have to put condition on the basis of time
    y=x[count][0]
    # if(count<t1):
    #     # hello.green(A[0])   # left lane is going and others are being stopped
    #     # hello.red(A[1])
    #     # hello.red(A[2])
    #     # hello.red(A[3])
        
    #     # car1.movement()
    #     pyg.time.delay(1000)
    # elif(count>t1 and count<t2):
    #     # hello.green(A[1])
    #     # hello.red(A[2])
    #     # hello.red(A[3])
    #     # hello.red(A[0])
    #     pyg.time.delay(1000)

    # elif(count>t2 and count<t3):
    #     # hello.green(A[2])
    #     # hello.red(A[0])
    #     # hello.red(A[3])
    #     # hello.red(A[1])
    #     pyg.time.delay(1000)
    # else:
    #     pyg.time.delay(1000)
    #     # hello.green(A[3])
    #     # hello.red(A[0])
    #     # hello.red(A[2])
    #     # hello.red(A[1])
    # # x = hello.getlightstate()
    pyg.time.delay(100)
    Background(y)
    for event in pyg.event.get():
        if(event.type == pyg.QUIT):
            run = False
    count = count+1
    pyg.display.update()