import pygame
import sys
import random
import math
import math_stuff

pygame.init()

SIZE = WIDTH, HEIGHT = 1000, 800
BLACK = 0,0,0
WHITE = 255,255,255

POINT_RADIUS =  4
MAX_SPEED = 0.2#0.9
NUMBER_OF_POINTS = 200
IGNORE_POINT_COL_N = MAX_SPEED * 50

CIRCLE_CENTER = WIDTH / 2, HEIGHT / 2
CIRCLE_RADIUS = 350
CIRCLE_BORDER_WIDTH = 8
CIRCLE_RADIUS_FOR_COLLISION = CIRCLE_RADIUS - 2 * POINT_RADIUS




def gen_random_color():
    return random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)

def generate_point():
    POINT_INNER_MODIFIER = 0.8
    r = CIRCLE_RADIUS * math.sqrt(random.random()) * POINT_INNER_MODIFIER 
    angle = random.random() * 2 * math.pi
    return CIRCLE_CENTER[0] + r * math.cos(angle), CIRCLE_CENTER[1] + r * math.sin(angle)

def generate_velocity():
    vx = random.uniform(-1,1)
    vy = math.sqrt(1 - vx**2) * random.choice([1,-1])
    speed = MAX_SPEED #random.random() * MAX_SPEED
    vx *= speed
    vy *= speed
    return vx, vy

def update_point(point, velocity, dt=1):
    X = point[0] + velocity[0] * dt
    Y = point[1] + velocity[1] * dt
    return X, Y

def check_collision(point):
    x = point[0]
    y = point[1]
    if math.pow(x - CIRCLE_CENTER[0] , 2) + math.pow(y - CIRCLE_CENTER[1], 2) < math.pow(CIRCLE_RADIUS_FOR_COLLISION,2):
        return False
    return True

def get_reflection_vector(org_vect, normal_vect):
    x1, y1 = org_vect
    nx, ny = math_stuff.normalize(normal_vect)
    dot_product = x1 * nx + y1 * ny
    return x1 - 2*dot_product*nx, y1 - 2*dot_product*ny

def do_collision(point, velocity):
    inter1, inter2 = math_stuff.inter_line_circle(point, velocity, CIRCLE_CENTER, CIRCLE_RADIUS_FOR_COLLISION)
    dist1 = math_stuff.distance(inter1, point)
    dist2 = math_stuff.distance(inter2, point)
    intersection = inter2
    if dist2 > dist1:
        intersection = inter1
    normal_vector_on_circle = math_stuff.normal_vector_line_on_point_circle(point, CIRCLE_CENTER)
    new_vector = get_reflection_vector(velocity, normal_vector_on_circle)
    return intersection, new_vector 

def check_collision_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if math.fabs(x1 - x2) < POINT_RADIUS*2 and math.fabs(y1 - y2) < POINT_RADIUS*2:
        return True
    return False

def do_collision_points(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return (-x1, -y1), (-x2, -y2)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
points = [generate_point() for i in range(NUMBER_OF_POINTS)]
velocites = [generate_velocity() for i in range(NUMBER_OF_POINTS)]
colors = [gen_random_color() for i in range(NUMBER_OF_POINTS)]
ignore_col = [[0 for j in range(NUMBER_OF_POINTS)] for i in range(NUMBER_OF_POINTS)]
dt = 0
while True:
    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
     
    # LOGIC
    for (i, velocity) in enumerate(velocites):
        points[i] = update_point(points[i], velocity, dt)
        # collisions with circle
        if check_collision(points[i]):
            points[i], velocites[i] = do_collision(points[i], velocity)
        # collisions between points
        for j in range(i+1, len(points)):
            if ignore_col[i][j] == 0 and check_collision_points(points[i], points[j]):
                velocites[i], velocites[j] = do_collision_points(velocites[i], velocites[j])
                ignore_col[i][j] = IGNORE_POINT_COL_N
            ignore_col[i][j] = 0 if ignore_col[i][j] <= 0 else ignore_col[i][j] - 1


    # DRAWING 
    screen.fill(BLACK)
    # master circlescrim during the m
    pygame.draw.circle(screen, WHITE, CIRCLE_CENTER, CIRCLE_RADIUS, width=CIRCLE_BORDER_WIDTH)
    #points
    for i, point in enumerate(points):
        pygame.draw.circle(screen, colors[i], point, POINT_RADIUS)
    pygame.display.flip()
    dt = clock.tick(60)