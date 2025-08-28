import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import time 
import random as rand

"""Z coordinate system inverted, when indexing Z array, always done so: Z[y][x]"""

grid_size = 61
delt_t = 0.5
barrier_s = []
barrier_g = []

bat_position = [[60,30],[60,28],[60,29],[60,31],[60,32]]

ball_position = [59,30]
ball_velocity = [-rand.randint(1,4), rand.randint(1,4)]


def background(size = grid_size):
    global barrier_s, barrier_g

    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(size):
        Z[axis][0] = 1
        barrier_s.append((0,axis))
    for axis in range(45,size):
        Z[axis][60] = 1
        barrier_g.append((60,axis))
    for axis in range(0,15):
        Z[axis][60] = 1
        barrier_g.append((60,axis))
    
    Z[29][60] = 1
    Z[30][60] = 1
    Z[31][60] = 1

    Z[30][59] = 2
    
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
    global ball_position, ball_velocity, bat_position, loss
    
    #if ball_position[0] >= 60:
        #ball_velocity = [-ball_velocity[0], ball_velocity[1]]
    
    if ball_position[0] <= 0:
        ball_velocity = [-ball_velocity[0], ball_velocity[1]]
    
    elif ball_position[0] >= 60:
        for point in barrier_g:
            if ball_position[1] == point[1]:
                ball_velocity = [-ball_velocity[0], ball_velocity[1]]

    elif ball_position[1] >= 60:
        ball_velocity = [ball_velocity[0], -ball_velocity[1]]
    
    elif ball_position[1] <= 0:
        ball_velocity = [ball_velocity[0], -ball_velocity[1]]

    for point in bat_position:
        if ball_position[0]==point[0] and ball_position[1]==point[1]:
            ball_velocity = [-ball_velocity[0], ball_velocity[1]]
            print('hit bat')

def loss_check():
    loss = True

    for point in barrier_g:
        if ball_position[1] == point[1]:
            loss = False
        
    if loss == True and ball_position[0] >= 60:
        image.set_data(Z)
        print('You lose! \n Womp. Womp.')
        time.sleep(2)
        quit()

def Z_update(size = grid_size):
    global barrier, Z

    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(size):
        Z[axis][0] = 1
    for axis in range(45,size):
        Z[axis][60] = 1
    for axis in range(0,15):
        Z[axis][60] = 1
    
    for point in bat_position:
        Z[point[1]][point[0]] = 1
    
    Z[round(ball_position[1])][round(ball_position[0])] = 2

    return Z

def run(x):
    ball_update()
    collision_check()
    loss_check()
        
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