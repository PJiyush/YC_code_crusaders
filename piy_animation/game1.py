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


# important information
vx = int(1460/120)
vy = int(750/120)

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
    
    # pyg.display.update()

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
    car0.draw()
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
    
    def movement(self,B,i):   # for movement in lane 1
        self.x =B[i][0]
        self.y =B[i][1]
        # self.velocity = velocity
        # self.y = self.y + self.velocity
        updatingGameWin()
        # print(A[i][0],A[i][1])
        # cordinates = tuple([self.x,self.y])
        # print(cordinates)
        # screen.blit(self.image,cordinates)

        

traffic_signal_images_left = [pyg.image.load('red_light.png'), pyg.image.load('green light.png')]
traffic_signal_images_up = [pyg.image.load('red_light up.png'), pyg.image.load('green light up.png')]
traffic_signal_images_right = [pyg.image.load('red_light right.png'), pyg.image.load('green light right.png')]
traffic_signal_images_down = [pyg.image.load('red_light down.png'), pyg.image.load('green light down.png')]

i = Intersection()
i.spawncars(5)
algo = SimpleCycle(i, period = 4)
algo.runsimulation(endtime = 100, record=True)
timeline = algo.getrecord(True)

B = []
for lights,cars_ in timeline:
    B.append(cars_[1]['position'])

# print(A)
for i in range(len(B)):
    B[i][0] =B[i][0]*vx
    B[i][0]-=68
    B[i][1] = B[i][1]*vy
    B[i][1]-=128
# print(A)
# print(A[-1])


clock = pyg.time.Clock()
car0 = cars(B[0][0],B[0][1],(0,1),0)
run =True
count =0
A = ['left','up','right','down']
# t1 = 1
# t2 = 2
# t3 = 3
# t4 = 4
maximum_timeline = len(timeline)
# while(run==True and count<t3 and count>=0):   # here I have to put condition on the basis of time
while(run==True and count<maximum_timeline):   # here I have to put condition on the basis of time
    for event in pyg.event.get():
        if(event.type == pyg.QUIT):
            run = False

    y=timeline[count][0]
    car0.movement(B,count)
    # car0.movement(timeline[0][1][0]['velocity'])
    updatingGameWin()
    count = count+1
    pyg.time.delay(500)
    Background(y)
    # pyg.display.update()

# 