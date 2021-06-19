import pygame
import sys
import random
import math

pygame.init()

SIZE = WIDTH, HEIGHT = 1000, 800
BLACK = 0,0,0
WHITE = 255,255,255

CIRCLE_CENTER = WIDTH / 2, HEIGHT / 2
CIRCLE_RADIUS = 350

POINT_RADIUS =  3

def generate_point():
    POINT_INNER_MODIFIER = 0.8
    r = CIRCLE_RADIUS * math.sqrt(random.random()) * POINT_INNER_MODIFIER 
    angle = random.random() * 2 * math.pi
    return CIRCLE_CENTER[0] + r * math.cos(angle), CIRCLE_CENTER[1] + r * math.sin(angle)

MAX_SPEED = 1#0.1

def generate_velocity():
    angle = random.random() * 2 * math.pi
    speed = random.random() * MAX_SPEED
    return angle, speed

def update_point(point, velocity, dt=1):
    angle, speed = velocity
    X = point[0] + speed * math.cos(angle) * dt
    Y = point[1] + speed * math.sin(angle) * dt
    return X, Y

def check_collision(point):
    x = point[0]
    y = point[1]
    OFFSITE = 10
    if math.pow(x - CIRCLE_CENTER[0] , 2) + math.pow(y - CIRCLE_CENTER[1], 2) < CIRCLE_RADIUS*CIRCLE_RADIUS - OFFSITE:
        return False
    return True

NUMBER_OF_POINTS = 50

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
points = [generate_point() for i in range(NUMBER_OF_POINTS)]
velocites = [generate_velocity() for i in range(NUMBER_OF_POINTS)]
dt = 0
while True:
    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
     
    # LOGIC
    # update points
    for (i, velocity) in enumerate(velocites):
        points[i] = update_point(points[i], velocity, dt)
        if check_collision(points[i]):
            new_angle = velocites[i][0] + math.pi
            if new_angle >  2 * math.pi:
                new_angle -= 2 * math.pi
            velocites[i] = new_angle, velocites[i][1] 
    
    # DRAWING 
    screen.fill(BLACK)
    # master circle
    pygame.draw.circle(screen, WHITE, CIRCLE_CENTER, CIRCLE_RADIUS, width=2)
    #points
    for point in points:
        pygame.draw.circle(screen, WHITE, point, POINT_RADIUS)
    pygame.display.flip()
    dt = clock.tick(60)