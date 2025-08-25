import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import time 

grid_size = 61
delt_t = 0.1
barrier_s = []
barrier_t = []
barrier_b = []

bat_position = [[60,30],[60,29],[60,31]]

ball_position = [59,30]
ball_velocity = [-4, 2]


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

    if event.key == 'i':
        bat_position = [[60, bat_position[0][1] + 1], [60, bat_position[1][1] + 1], [60, bat_position[2][1] + 1]]
        print("i pressed - bat up")
    if event.key == 'k':
        bat_position = [[60, bat_position[0][1] - 1], [60, bat_position[1][1] - 1], [60, bat_position[2][1] - 1]]
        print("k pressed - bat down")
        
    print("new bat position: " + str(bat_position))

def ball_update():
    global ball_position, ball_velocity, delt_t

    new_x = ball_position[0] + ball_velocity[0]
    new_y = ball_position[1] + ball_velocity[1]
    
    ball_position = [new_x, new_y] #redefined position of ball
    
    if ball_position[0] >= 60:
        ball_position = [60, new_y]
    elif ball_position[0] < 0:
        ball_position = [0, new_y]
    
    if ball_position[1] >= 60:
        ball_position = [new_x, 60]
    elif ball_position[1] < 0:
        ball_position = [new_x, 0]   

    #print('new position: ' + str(ball_position))

def collision_check():
    global ball_position, ball_velocity, barrier_s, barrier_b, barrier_t
    
    if ball_position[1] == 60:
        ball_velocity = [ball_velocity[0],-ball_velocity[1]]
        #print('velocity change')
    if ball_position[1] == 0:
        ball_velocity = [ball_velocity[0],-ball_velocity[1]]
        #print('velocity change')

    if ball_velocity[0] == 0:
        ball_velocity = [-ball_velocity[0],ball_velocity[1]]
        #print('velocity change')
    if ball_velocity[0] == 60:
        ball_velocity = [-ball_velocity[0],ball_velocity[1]]
        #print('velocity change')
    
    #print('new velocity: ' + str(ball_velocity))

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

#plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","black","powderblue"])

fig.canvas.mpl_connect('key_press_event', keypress)

image = ax.imshow(background(), origin = 'upper', cmap=cmap)

ani = FuncAnimation(fig, run, frames = 100, interval = 10, blit = False)
plt.show()