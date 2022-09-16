from libs import *
import pygame as pyg
pyg.init()

screen = pyg.display.set_mode((1460,750))

# for background
horizontal_track = {'yUpL': (0,307), 'yUpR': (1460,307), 'yDownL': (0,443), 'yDownR': (1460,443)}
vertical_track = {'xLeftU': (662,0), 'xLeftD': (662,750), 'xRightU': (798,0), 'xRightD': (798,750)}


# important information
vX = int(1460/120)
vY = int(750/120)

# cars
cars_images = [
    pyg.image.load('./cars/down/blue.png'),
    pyg.image.load('./cars/down/black.png'),
    pyg.image.load('./cars/down/red.png'),
    pyg.image.load('./cars/down/green.png')
]

def Background(x:dict):
    screen.fill((255,255,255))
    pyg.draw.line(screen, (0,0,0), horizontal_track['yUpL'], horizontal_track['yUpR'])
    pyg.draw.line(screen, (0,0,0), horizontal_track['yDownL'], horizontal_track['yDownR'])
    pyg.draw.line(screen, (0,0,0), vertical_track['xLeftU'], vertical_track['xLeftD'])
    pyg.draw.line(screen, (0,0,0), vertical_track['xRightU'], vertical_track['xRightD'])

    if(x['left']==1):
        screen.blit(traffic_signal_images_left[1],traffic_signal_coordinates['left'])
    elif(x['left']==0):
        screen.blit(traffic_signal_images_left[0],traffic_signal_coordinates['left'])
    
    if(x['up']==1):
        screen.blit(traffic_signal_images_up[1],traffic_signal_coordinates['up'])
    elif(x['up']==0):
        screen.blit(traffic_signal_images_up[0],traffic_signal_coordinates['up'])
    
    if(x['right']==1):
        screen.blit(traffic_signal_images_right[1],traffic_signal_coordinates['right'])
    elif(x['right']==0):
        screen.blit(traffic_signal_images_right[0],traffic_signal_coordinates['right'])
    
    if(x['down']==1):
        screen.blit(traffic_signal_images_down[1],traffic_signal_coordinates['down'])
    elif(x['down']==0):
        screen.blit(traffic_signal_images_down[0],traffic_signal_coordinates['down'])
    
    # pyg.display.update()

traffic_signal_coordinates = {
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
    
    def movement(self,positionArrayUp,i):   # for movement in lane 1
        self.x =positionArrayUp[i][0]
        self.y =positionArrayUp[i][1]
        # self.velocity = velocity
        # self.y = self.y + self.velocity
        updatingGameWin()
        # print(A[i][0],A[i][1])
        # cordinates = tuple([self.x,self.y])
        # print(cordinates)
        # screen.blit(self.image,cordinates)

        

traffic_signal_images_left = [pyg.image.load('./imagesUsed/red_light_left.png'), pyg.image.load('./imagesUsed/green_light_left.png')]
traffic_signal_images_up = [pyg.image.load('./imagesUsed/red_light_up.png'), pyg.image.load('./imagesUsed/green_light_up.png')]
traffic_signal_images_right = [pyg.image.load('./imagesUsed/red_light_right.png'), pyg.image.load('./imagesUsed/green_light_right.png')]
traffic_signal_images_down = [pyg.image.load('./imagesUsed/red_light_down.png'), pyg.image.load('./imagesUsed/green_light_down.png')]

i = Intersection()
i.spawncars(5)
algo = SimpleCycle(i, period = 4)
algo.runsimulation(endtime = 100, record=True)
records = algo.getrecord(True)

positionArrayUp = []
positionArrayDown = []
positionArrayLeft = []
positionArrayRight = []

exited_array = []
for lights,_cars_ in records:
    positionArrayUp.append(_cars_[1]['position'])
    exited_array.append(_cars_[1]['exited'])



# class vehicles:
    # def __init__(self, ):



# print(A)
for i in range(len(positionArrayUp)):
    if(exited_array[i] == False):
        positionArrayUp[i][0] = 730 - (1 + 32 + 2 + 32)
        positionArrayUp[i][1] = positionArrayUp[i][1]*vY
        positionArrayUp[i][1] -= (48*2 + 24)
    else:
        positionArrayUp[i][0] = 1800
        positionArrayUp[i][1] = 1800
# print(A)
# print(A[-1])


clock = pyg.time.Clock()
car0 = cars(positionArrayUp[0][0],positionArrayUp[0][1],(0,1),0)
run = True
count = 0
tf_orientations = ['left','up','right','down']
# t1 = 1
# t2 = 2
# t3 = 3
# t4 = 4
maximum_timeline = len(records)
# while(run==True and count<t3 and count>=0):   # here I have to put condition on the basis of time
while(run==True and count<maximum_timeline):   # here I have to put condition on the basis of time
    for event in pyg.event.get():
        if(event.type == pyg.QUIT):
            run = False

    y=records[count][0]
    car0.movement(positionArrayUp,count)
    # car0.movement(records[0][1][0]['velocity'])
    updatingGameWin()
    count = count+1
    pyg.time.delay(500)
    Background(y)
    # pyg.display.update()

