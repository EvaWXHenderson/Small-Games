import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import time 
import random as rand

"""Z coordinate system inverted, when indexing Z array, always done so: Z[y][x]"""

grid_size = 61
delt_t = 0.2
barrier_s = []
barrier_g = []

bat_position = [[60,30],[60,28],[60,29],[60,31],[60,32]]

ball_position = [59,30]
ball_velocity = [-rand.randint(2,4), rand.randint(2,4)]

speed_change = False


def background(size = grid_size):
    global barrier_s, barrier_g

    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(size):
        Z[axis][0] = 1
        Z[0][axis] = 1
        Z[60][axis] = 1
        barrier_s.append((0,axis))
        
    Z[29][60] = 1
    Z[30][60] = 1
    Z[31][60] = 1

    Z[30][59] = 2

    ax.set_xticks([])
    ax.set_yticks([])
    
    return Z

def keypress(event):
    global bat_position, barrier_g
    
    overlap_top = False
    overlap_bottom = False

    for point in barrier_g:
        if bat_position[4][1] == point[1]:
            overlap_top = True
        elif bat_position[1][1] == point[1]:
            overlap_bottom = True
    
    if event.key == 'down':
        if overlap_top == False: 
            bat_position = [[60, bat_position[0][1] + 2], [60, bat_position[1][1] + 2], [60, bat_position[2][1] + 2], [60, bat_position[3][1] + 2], [60, bat_position[4][1] + 2]]
        elif overlap_top == True:
            bat_position = [[60, 43], [60, 41], [60, 42], [60, 44], [60, 45]]

    if event.key == 'up':
        if overlap_bottom == False:
            bat_position = [[60, bat_position[0][1] - 2], [60, bat_position[1][1] - 2], [60, bat_position[2][1] - 2], [60, bat_position[3][1] - 2], [60, bat_position[4][1] - 2]]
        elif overlap_bottom == True:
            bat_position = [[60, 18], [60, 16], [60, 17], [60, 19], [60, 20]]

def ball_update():
    global ball_position, ball_velocity, delt_t

    new_x = ball_position[0] + ball_velocity[0] * delt_t
    new_y = ball_position[1] + ball_velocity[1] * delt_t

    if new_x > 60:
        new_x = 60
    elif new_x < 0:
        new_x = 0
    
    if new_y > 60:
        new_y = 60
    elif new_y < 0:
        new_y = 0  

    ball_position = [new_x, new_y] #redefined position of ball

def collision_check():
    global ball_position, ball_velocity, bat_position, speed_change, loss

    rounded_ball = [round(ball_position[0]), round(ball_position[1])]
    bat_collision = False
    
    if ball_position[0] <= 0:
        ball_velocity = [-ball_velocity[0], ball_velocity[1]]  

    elif ball_position[1] >= 60:
        ball_velocity = [ball_velocity[0], -ball_velocity[1]]   
    elif ball_position[1] <= 0:
        ball_velocity = [ball_velocity[0], -ball_velocity[1]]


    for point in bat_position:
        if rounded_ball[0]==point[0] and rounded_ball[1]==point[1]:
            ball_velocity = [-ball_velocity[0], ball_velocity[1]]
            bat_collision = True

    if bat_collision == True:
        speed_change = True
    if bat_collision == False:
        speed_change = False

def speed():
    global speed_change, delt_t

    if speed_change == True:
        delt_t = 0.5

def speed_decay():
    global delt_t

    if delt_t > 0.2:
        delt_t -= 0.0025

def loss_check():
    global ball_position, barrier_g, bat_position, Z

    rounded_ball = [round(ball_position[0]), round(ball_position[1])]
    loss = True

    for point in bat_position:
        if rounded_ball[1] == point[1]:
            loss = False
            
        
    if loss == True and rounded_ball[0] >= 60:
        image.set_data(Z)
        print('You lose! \n Womp. Womp.')
        time.sleep(2)
        quit()

def Z_update(size = grid_size):
    global barrier, Z

    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(size):
        Z[axis][0] = 1
        Z[0][axis] = 1
        Z[60][axis] = 1
    
    for point in bat_position:
        Z[point[1]][point[0]] = 1
    
    Z[round(ball_position[1])][round(ball_position[0])] = 2

    return Z

def run(x):
    global delt_t
    
    ball_update()
    collision_check()
    speed()
    loss_check()

    speed_decay()
        
    ax.set_xticks([])
    ax.set_yticks([])

    Z = Z_update()
    image.set_data(Z)





fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","black","powderblue"])

fig.canvas.mpl_connect('key_press_event', keypress)

image = ax.imshow(background(), origin = 'upper', cmap=cmap)

ani = FuncAnimation(fig, run, frames = 100, interval = 10, blit = False)
plt.show()