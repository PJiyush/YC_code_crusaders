
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
    pyg.draw.line(screen, (0,0,0), horizontal_track['yUpL'], horizontal_track['yUpR'],2)
    pyg.draw.line(screen, (0,0,0), horizontal_track['yDownL'], horizontal_track['yDownR'],2)
    pyg.draw.line(screen, (0,0,0), vertical_track['xLeftU'], vertical_track['xLeftD'],2)
    pyg.draw.line(screen, (0,0,0), vertical_track['xRightU'], vertical_track['xRightD'],2)
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

def update_cars(A):
    for i in A:
        i.draw()

def updatingGameWin(dict1):
    for i in dict1:
        i.draw()
    # here draw each object
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
            self.image = pyg.transform.scale(self.image,(32,32))
            
            screen.blit(self.image,(self.x,self.y))
    
    # def movement(self,B,i):   
    def movement(self,position,exit,intersection,state):
        if(state==1):
            if(exit==False):
                x_cordinate =position[0]
                y_cordinate =position[1]
                self.x = (x_cordinate)*vx
                self.y = (y_cordinate)*vy
                if(self.lane ==1):
                    self.x = self.x - 150
                elif(self.lane==2):
                    self.y = self.y - 150
                elif(self.lane==3):
                    self.x = self.x + 150
                else:
                    self.y = self.y + 150
                # self.draw()
            # else:
                # self.x
            if(exit==True):
                self.x = 1460
                self.y = 750

        elif(state==0 and exit==False):
            self.x = position[0]
            self.y = position[1]
            self.x = (self.x)*vx
            self.y = (self.y)*vy
            if(self.lane ==1):
                self.x = self.x - 200
            elif(self.lane==2):
                self.y = self.y - 200
            elif(self.lane==3):
                self.x = self.x + 200
            else:
                self.y = self.y + 200
            # self.draw()
        
    




        

traffic_signal_images_left = [pyg.image.load('red_light.png'), pyg.image.load('green light.png')]
traffic_signal_images_up = [pyg.image.load('red_light up.png'), pyg.image.load('green light up.png')]
traffic_signal_images_right = [pyg.image.load('red_light right.png'), pyg.image.load('green light right.png')]
traffic_signal_images_down = [pyg.image.load('red_light down.png'), pyg.image.load('green light down.png')]


t = 100
i = Intersection()
no_of_cars_in_a_lane = 5
i.spawncars(no_of_cars_in_a_lane)
algo = NetworkAlgorithm(i, thresh = 30)
algo.runsimulation(endtime = t, record=True)
timeline = algo.getrecord(True) # now this algo contains information of no of cars
car_object_list = []
for i in range((no_of_cars_in_a_lane)*4):
    car_object_list.append(cars(timeline[0][1][i]['position'][0],timeline[0][1][i]['position'][1],timeline[0][1][i]['direction'],i%4))
# print(car_object_list)

position_of_each_car_at_that_time = []
exit_of_each_car_at_that_time = []
Intersection = []
state_of_cars = []
for i in range(t):
    position_of_each_car_at_that_time.append([])
    exit_of_each_car_at_that_time.append([])
    Intersection.append([])
    state_of_cars.append([])
    for j in range(len(car_object_list)):
        position_of_each_car_at_that_time[i].append(timeline[i][1][j]['position'])
        exit_of_each_car_at_that_time[i].append(timeline[i][1][j]['exited'])
        Intersection[i].append(timeline[i][1][j]['atintersection'])
        state_of_cars[i].append(timeline[i][1][j]['state'])

print(len(position_of_each_car_at_that_time))
print(len(exit_of_each_car_at_that_time))

# through this I got timeline as well as car_object_list

# B = []
# exit_status = []
# for lights,cars_ in timeline:
#     B.append(cars_[1]['position'])
#     exit_status.append(cars_[1]['exited'])


# print(A)
# for i in range(len(B)):
#     if(exit_status[i]==False):
#         B[i][0] =B[i][0]*vx
#         B[i][0]-=(1+32+16)
#         B[i][1] = B[i][1]*vy
#         B[i][1]-=120
#     if(exit_status[i]==True):
#         B[i][0] = 1800
#         B[i][1] = 1800
# print(A)
# print(A[-1])


clock = pyg.time.Clock()
run =True
count =0
A = ['left','up','right','down']


# car0 = cars(0,0,(0,1),0)
# car1 = cars()
# B = car0.the_Simplealgo()
maximum_timeline = len(timeline)
# while(run==True and count<t3 and count>=0):   # here I have to put condition on the basis of time
while(run==True and count<maximum_timeline):   # here I have to put condition on the basis of time
    for event in pyg.event.get():
        if(event.type == pyg.QUIT):
            run = False

    y=timeline[count][0]
    for i in range(len(car_object_list)):
        (car_object_list[i]).movement(position_of_each_car_at_that_time[count][i],exit_of_each_car_at_that_time[count][i],Intersection[count][i],state_of_cars[count][i])
        # (car_object_list[i]).draw()
        updatingGameWin(car_object_list)
    # car0.movement(B,count)
    # car0.movement(timeline[0][1][0]['velocity'])
    # update_cars(car_object_list)
    # updatingGameWin(car_object_list)
    count = count+1
    pyg.time.delay(500)
    Background(y)
    # pyg.display.update()

# 