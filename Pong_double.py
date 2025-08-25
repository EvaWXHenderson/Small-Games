import matplotlib as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import random as rand

grid_size = 60
delt_t = 0.1
barrier_t = []
barrier_b = []

bat_position1 = [(30,60),(29,60),(31,60)]
bat_position2 = [(30,0),(29,0),(31,0)]

ball_position = [(30,59)]
ball_velocity = [rand.randint(-4, 4), rand.randint(-4, 4)]

def background(size = grid_size):
    global barrier_m, barrier_t, barrier_b

    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(size):
        Z[axis][30] = 1
        barrier_t.append((axis,0)) #bottom
        barrier_b.append((axis,60)) #top
    
    Z[29][60] = 1
    Z[30][60] = 1
    Z[31][60] = 1

    Z[29][0] = 1
    Z[30][0] = 1
    Z[31][0] = 1

    Z[30][59] = 2
    Z[30][1] = 3
    
    return Z

def keypress(event):
    if event.key == 'w':
        pass
    if event.key == 's':
        pass

def ball_update(position = ball_position, velocity = ball_velocity, t = delt_t):
    new_x = position[0] + velocity[0] * t
    new_y = position[1] + velocity[1] * t
    
    position = (new_x, new_y) #redefined position of ball

def collision_check(bat1 = bat_position1, bat2 = bat_position2, position = ball_position, velocity = ball_velocity, top = barrier_t, bottom = barrier_b):    
    for point in top:
        if (position[0], position[1] + 1) == point:
            velocity[0] = -velocity[1]

    for point in bottom:
        if (position[0], position[1] - 1) == point:
            velocity[0] = -velocity[1]

    for point in bat1:
        if (position[0] + 1, position[1]) == point:
            velocity[0] = -velocity[0]     
    #testing collision with player 1 bat  

    for point in bat2:
        if (position[0] + 1, position[1]) == point:
            velocity[0] = -velocity[0] 
    #testing collision with player 1 bat

def loss_check():
    pass

def Z_update():
    pass

def run(x):
    image.set_data(Z_update())
    
    ax.set_xticks([])
    ax.set_yticks([])

plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","black","yellowgreen"])

fig.canvas.mpl_connect('key_press_event', keypress)

image = ax.imshow(background(), origin = 'upper', cmap=cmap)

ani = FuncAnimation(fig, run, frames = 100, interval = 10, blit = False)
plt.show()