import matplotlib as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import random as rand

grid_size = 60
delt_t = 0.1
barrier_s = []
barrier_t = []
barrier_b = []

bat_position = [(30,60),(29,60),(31,60)]

ball_position = [(30,59)]
ball_velocity = [rand.randint(-4, 4), rand.randint(-4, 4)]


"""class bat:
    def __init__(self):
        global player
        self.position = [(30,60)] #initial position (as well as [30-1][60], [30+1][60])

        bat_position.append(self.position)"""


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

    for position in bat_position:
        if event.key == 'w':
            new_bat_1 = (position[0][0] + 1, 60)
            new_bat_2 = (position[0][1] + 1, 60)
            new_bat_3 = (position[0][2] + 1, 60)
        if event.key == 's':
            new_bat_1 = (position[0][0] - 1, 60)
            new_bat_2 = (position[0][1] - 1, 60)
            new_bat_3 = (position[0][2] - 1, 60)
        
        bat_position = [new_bat_1, new_bat_2, new_bat_3]

def ball_update(position = ball_position, velocity = ball_velocity, t = delt_t):
    new_x = position[0] + velocity[0] * t
    new_y = position[1] + velocity[1] * t
    
    position = (new_x, new_y) #redefined position of ball

def collision_check(position = ball_position, velocity = ball_velocity, side = barrier_s, top = barrier_t, bottom = barrier_b):
    for point in side:
        if (position[0] - 1, position[1]) == point:
            velocity[0] = -velocity[0] #inverse x position upon collisions
    #testing collision with left pannel

    for point in top:
        if (position[0], position[1] + 1) == point:
            velocity[0] = -velocity[1]
    #testing collision with top pannel

    for point in bottom:
        if (position[0], position[1] - 1) == point:
            velocity[0] = -velocity[1]
    #testing collision with bottom pannel

    for point in bat_position:
        if (position[0] + 1, position[1]) == point:
            velocity[0] = -velocity[0]     
    #testing collision with players bat  


def loss_check():
    pass

def Z_update():
    for player in player:
        player.position

def anim_data():
    pass

#bat()

plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","black","powderblue"])

fig.canvas.mpl_connect('key_press_event', keypress)

image = ax.imshow(background(), origin = 'upper', cmap=cmap)
image.set_data(Z_update())

ani = FuncAnimation(fig, anim_data, frames = 100, interval = 10, blit = False)
plt.show()