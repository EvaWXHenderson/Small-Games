import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import time 

"""Z coordinate system inverted, when indexing Z array, always done so: Z[y][x]"""

grid_size = 61
delt_t = 1
barrier_s = []
barrier_t = []
barrier_b = []

bat_position = [[60,30],[60,28],[60,29],[60,31],[60,32]]

ball_position = [59,30]
ball_velocity = [-3, 1]


def background(size = grid_size):
    global barrier_s, barrier_t, barrier_b

    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(size):
        Z[axis][0] = 1
        barrier_s.append((0,axis)) #side barrier
        barrier_t.append((axis,0)) #bottom
        barrier_b.append((axis,60)) #top
    
    Z[29][60] = 1
    Z[30][60] = 1
    Z[31][60] = 1

    Z[30][59] = 2
    
    return Z

def keypress(event):
    global bat_position

    if event.key == 'down':
        bat_position = [[60, bat_position[0][1] + 1], [60, bat_position[1][1] + 1], [60, bat_position[2][1] + 1], [60, bat_position[3][1] + 1], [60, bat_position[4][1] + 1]]
    if event.key == 'up':
        bat_position = [[60, bat_position[0][1] - 1], [60, bat_position[1][1] - 1], [60, bat_position[2][1] - 1], [60, bat_position[3][1] - 1], [60, bat_position[4][1] - 1]]

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
    global ball_position, ball_velocity, barrier_s, barrier_b, barrier_t
    
    if ball_position[0] >= 60:
        ball_velocity = [-ball_velocity[0],ball_velocity[1]]
    elif ball_position[0] <= 0:
        ball_velocity = [-ball_velocity[0],ball_velocity[1]]

    elif ball_position[1] >= 60:
        ball_velocity = [ball_velocity[0],-ball_velocity[1]]
    elif ball_position[1] <= 0:
        ball_velocity = [ball_velocity[0],-ball_velocity[1]]

    for point in bat_position:
        pass

def loss_check():
    if ball_position[0] > 60:
        print('You lose! \n Womp. Womp.')
        time.sleep(2)
        quit()

def Z_update(size = grid_size):
    global barrier, Z

    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(size):
        Z[axis][0] = 1
    
    for point in bat_position:
        Z[point[1]][point[0]] = 1
    
    Z[round(ball_position[1])][round(ball_position[0])] = 2

    return Z

def run(x):
    ball_update()
    collision_check()
    #loss_check()
        
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