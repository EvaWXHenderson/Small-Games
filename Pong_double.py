import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import time
import random as rand

"""Z coordinate system inverted, when indexing Z array, always done so: Z[y][x]"""

grid_size = 61
delt_t = 0.2
barrier_t = []
barrier_b = []

bat_position1 = [[60,30],[60,28],[60,29],[60,31],[60,32]]
bat_position2 = [[0,30],[0,28],[0,29],[0,31],[0,32]]

ball_position = [59,30]
ball_velocity = [-rand.randint(2,4), rand.randint(2,4)]

speed_change = False


def background(size = grid_size):
    global barrier_m, barrier_t, barrier_b

    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(size):
        Z[0][axis] = 1
        Z[60][axis] = 1
    
    Z[28][60] = 1
    Z[29][60] = 1
    Z[30][60] = 1
    Z[31][60] = 1
    Z[32][60] = 1

    Z[28][0] = 1
    Z[29][0] = 1
    Z[30][0] = 1
    Z[31][0] = 1
    Z[32][0] = 1

    Z[30][59] = 2

    ax.set_xticks([])
    ax.set_yticks([])
    
    return Z

def keypress(event):
    global bat_position1, bat_position2

    if event.key == 'down':
        bat_position1 = [[60, bat_position1[0][1] + 2], [60, bat_position1[1][1] + 2], [60, bat_position1[2][1] + 2], [60, bat_position1[3][1] + 2], [60, bat_position1[4][1] + 2]]
    if event.key == 'up':
        bat_position1 = [[60, bat_position1[0][1] - 2], [60, bat_position1[1][1] - 2], [60, bat_position1[2][1] - 2], [60, bat_position1[3][1] - 2], [60, bat_position1[4][1] - 2]]

    if event.key == 's':
        bat_position2 = [[0, bat_position2[0][1] + 2], [0, bat_position2[1][1] + 2], [0, bat_position2[2][1] + 2], [0, bat_position2[3][1] + 2], [0, bat_position2[4][1] + 2]]
    if event.key == 'w':
        bat_position2 = [[0, bat_position2[0][1] - 2], [0, bat_position2[1][1] - 2], [0, bat_position2[2][1] - 2], [0, bat_position2[3][1] - 2], [0, bat_position2[4][1] - 2]]

def ball_update(position = ball_position, velocity = ball_velocity, t = delt_t):
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
    global ball_position, ball_velocity, bat_position, loss, speed_change

    rounded_ball = [round(ball_position[0]), round(ball_position[1])]
    bat_collision = False

#for testing without ending/losing game:
    #if ball_position[0] >= 60:
        #print('hit RHS')
        #ball_velocity = [-ball_velocity[0],ball_velocity[1]]
    #if ball_position[1] <= 0:
        #print('hit LHS')
        #ball_velocity = [-ball_velocity[0],ball_velocity[1]]
###
    
    if ball_position[1] >= 60: #hits top
        ball_velocity = [ball_velocity[0],-ball_velocity[1]]

    if ball_position[1] <= 0: #hits bottom
        ball_velocity = [ball_velocity[0],-ball_velocity[1]]

    for point in bat_position1: #hits bat of RHP - player1
        if rounded_ball[0]==point[0] and rounded_ball[1]==point[1]:
            ball_velocity = [-ball_velocity[0], ball_velocity[1]]
            bat_collision = True

    for point in bat_position2: #hits bat of LHP - player2
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
        delt_t = 0.4

def speed_decay():
    global delt_t

    if delt_t > 0.2:
        delt_t -= 0.005
        print(delt_t)

def loss_check():
    global ball_position, bat_position2, bat_position1, Z

    loss = True

    for point in bat_position1:
        if ball_position[1] == point[1]:
            loss = False
    
    for point in bat_position2:
        if ball_position[1] == point[1]:
            loss = False

    if ball_position[0] >= 60 and loss == True:
        print('Player 2 loses! \n Womp. Womp.') #LHS player
        #print(ball_position)
        #print(bat_position1)
        image.set_data(Z)
        time.sleep(2)
        quit()
    
    if ball_position[0] <= 0 and loss == True:
        print('Player 1 loses! \n Womp. Womp.') #RHS player
        #print(ball_position)
        #print(bat_position2)
        image.set_data(Z)
        time.sleep(2)
        quit()

def Z_update(size = grid_size):
    global barrier, Z

    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(size):
        Z[0][axis] = 1
        Z[60][axis] = 1
    
    for point in bat_position1:
        Z[point[1]][point[0]] = 1
    for point in bat_position2:
        Z[point[1]][point[0]] = 1
    
    Z[round(ball_position[1])][round(ball_position[0])] = 2

    return Z

def run(x):
    ball_update()
    collision_check()
    speed()
    loss_check()

    speed_decay()
        
    ax.set_xticks([])
    ax.set_yticks([])

    Z = Z_update()
    image.set_data(Z)






plt.rcParams['keymap.save'].remove('s')
fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","black","yellowgreen"])

fig.canvas.mpl_connect('key_press_event', keypress)

image = ax.imshow(background(), origin = 'upper', cmap=cmap)

ani = FuncAnimation(fig, run, frames = 100, interval = 10, blit = False)
plt.show()