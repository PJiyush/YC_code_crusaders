import pygame
# import time
from libs import *

num_cars = 10
time_period = 30

# touseef = Intersection()
# touseef.spawncars(num_cars)

# algo = SimpleCycle(touseef, time_period)
# algo.runsimulation()
# records = algo.getrecord(listform=False)

pygame.init()
screen = pygame.display.set_mode((1460, 750))
pygame.display.set_caption('Simple Algo')

# icon = pygame.image.load('./')
# pygame.display.set_icon(icon)

#background
horizontal_track = {'yUpL': (0,307), 'yUpR': (1460,307), 'yDownL': (0,443), 'yDownR': (1460,443)}
vertical_track = {'xLeftU': (662,0), 'xLeftD': (662,750), 'xRightU': (798,0), 'xRightD': (798,750)}

carImagesLeft = {'blue':'./cars/left/blue.png', 'black':'./cars/left/black.png', 'green':'./cars/left/green.png', 'orange':'./cars/left/orange.png',
'red':'./cars/left/red.png'}
carImagesRight = {'blue':'./cars/right/blue.png', 'black':'./cars/right/black.png', 'green':'./cars/right/green.png', 'orange':'./cars/right/orange.png',
'red':'./cars/right/red.png'}
carImagesUp = {'blue':'./cars/up/blue.png', 'black':'./cars/up/black.png', 'green':'./cars/up/green.png', 'orange':'./cars/up/orange.png',
'red':'./cars/up/red.png'}
carImagesDown = {'blue':'./cars/down/blue.png', 'black':'./cars/down/black.png', 'green':'./cars/down/green.png', 'orange':'./cars/down/orange.png',
'red':'./cars/down/red.png'}

carImages = {
    'left': {'blue':'./cars/left/blue.png', 'black':'./cars/left/black.png', 'green':'./cars/left/green.png', 'orange':'./cars/left/orange.png', 'red':'./cars/left/red.png'},
    'right': {'blue':'./cars/right/blue.png', 'black':'./cars/right/black.png', 'green':'./cars/right/green.png', 'orange':'./cars/right/orange.png', 'red':'./cars/right/red.png'},
    'up': {'blue':'./cars/up/blue.png', 'black':'./cars/up/black.png', 'green':'./cars/up/green.png', 'orange':'./cars/up/orange.png', 'red':'./cars/up/red.png'},
    'down': {'blue':'./cars/down/blue.png', 'black':'./cars/down/black.png', 'green':'./cars/down/green.png', 'orange':'./cars/down/orange.png', 'red':'./cars/down/red.png'}
}

#velocities
vX = int(1460/120)
vY = int(750/120)

'''
index varies from 0 to (num_cars - 1)
'''

#car object
class carObject:
    def __init__(self, x, y, lane, img):
        self.x = x
        self.y = y
        self.lane = lane
        if self.lane == 'left':
            self.img = pygame.image.load(carImagesLeft[img])
        elif self.lane == 'right':
            self.img = pygame.image.load(carImagesRight[img])
        elif self.lane == 'up':
            self.img = pygame.image.load(carImagesUp[img])
        elif self.lane == 'down':
            self.img = pygame.image.load(carImagesDown[img])

    def draw_car(self):
        screen.blit(self.img, (self.x, self.y))

dist_tf = 30
dist_car = 10

#traffic lights
class traffic_lights:
    def __init__(self, x, y, state, orientation):
        # x and y are coordinates of centre of traffic light
        self.x = x
        self.y = y
        self.width = 80
        self.height = 200
        self.radius = 35
        self.state =  state
        self.orientation = orientation

    def draw_traffic_lights(self):
        if self.orientation == 'horizontal':
            pygame.draw.rect(screen, (0, 0, 0), (self.x - 100, self.y - 40, self.height, self.width))
            if self.state == 0:
                pygame.draw.circle(screen, (10, 28, 12), (self.x - 50, self.y), self.radius)
                pygame.draw.circle(screen, (255, 0, 0), (self.x + 50, self.y), self.radius)
            else:
                pygame.draw.circle(screen, (0, 255, 0), (self.x - 50, self.y), self.radius)
                pygame.draw.circle(screen, (32, 12, 12), (self.x + 50, self.y), self.radius)
        if self.orientation == 'vertical':
            pygame.draw.rect(screen, (0, 0, 0), (self.x - 40, self.y - 100, self.width, self.height))
            if self.state == 0:
                pygame.draw.circle(screen, (10, 28, 12), (self.x, self.y - 50), self.radius)
                pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y + 50), self.radius)
            else:
                pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y - 50), self.radius)
                pygame.draw.circle(screen, (32, 12, 12), (self.x, self.y + 50), self.radius)


# traffic lights using the coordinates of their centres
tfLU = traffic_lights(662-(40+dist_tf), 307-(100+dist_tf), 1, 'vertical')
tfRD = traffic_lights(798+(40+dist_tf), 443+(100+dist_tf), 0, 'vertical')
tfLD = traffic_lights(662-(100+dist_tf), 443+(40+dist_tf), 0, 'horizontal')
tfRU = traffic_lights(798+(100+dist_tf), 307-(40+dist_tf), 0, 'horizontal')

'''
#left lane using coordinates of corners of the cars
carL1 = carObject(662 - 48 - dist_car, 375 - (1 + 32 + 2 + 32), 'left', 'red')
carL2 = carObject(662 - 48 - dist_car, 375 - (1 + 32), 'left', 'green')
carL3 = carObject(662 - 48 - dist_car, 375 + (1), 'left', 'orange')
carL4 = carObject(662 - 48 - dist_car, 375 + (1 + 32 + 1), 'left', 'blue')

#right lane using coordinates of corners of the cars
carR1 = carObject(798 + dist_car, 375 - (1 + 32 + 2 + 32), 'right','blue')
carR2 = carObject(798 + dist_car, 375 - (1 + 32), 'right','green')
carR3 = carObject(798 + dist_car, 375 + (1), 'right','red')
carR4 = carObject(798 + dist_car, 375 + (1 + 32 + 1), 'right','black')

#up lane using coordinates of corners of cars
carU1 = carObject(730 - (1 + 32 + 2 + 32), 307 - 48 - dist_car, 'up', 'blue')
carU2 = carObject(730 - (1 + 32), 307 - 48 - dist_car, 'up', 'black')
carU3 = carObject(730 + (1), 307 - 48 - dist_car, 'up', 'green')
carU4 = carObject(730 + (1 + 32 + 1), 307 - 48 - dist_car, 'up', 'red')

#down lane using coordinates of corners of cars
carD1 = carObject(730 - (1 + 32 + 2 + 32), 443 + dist_car, 'down', 'blue')
carD2 = carObject(730 - (1 + 32), 443 + dist_car, 'down', 'green')
carD3 = carObject(730 + (1), 443 + dist_car, 'down', 'orange')
carD4 = carObject(730 + (1 + 32 + 1), 443 + dist_car, 'down', 'red')
'''

img = pygame.image.load(carImages['left']['blue'])
x = 5 * vX
y = 60 * vY
def car_temp():
    screen.blit(img, (x,y))

run = True
#while run and x <= 730:
while run:
    pygame.time.delay(100)
    screen.fill((255, 255, 255))
    #screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    #tracks
    pygame.draw.line(screen, (0,0,0), horizontal_track['yUpL'], horizontal_track['yUpR'])
    pygame.draw.line(screen, (0,0,0), horizontal_track['yDownL'], horizontal_track['yDownR'])

    pygame.draw.line(screen, (0,0,0), vertical_track['xLeftU'], vertical_track['xLeftD'])
    pygame.draw.line(screen, (0,0,0), vertical_track['xRightU'], vertical_track['xRightD'])
    
    tfLU.draw_traffic_lights()
    tfRU.draw_traffic_lights()
    tfLD.draw_traffic_lights()
    tfRD.draw_traffic_lights()

    if(x < 662 - 48 - dist_car - vX):
        x += vX
    car_temp()

    pygame.display.update()

pygame.quit()