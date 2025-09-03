import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import time 
import random as rand

grid_size = 21
delt_t = 0.3

def O(centre, info):
    check_list_entry(centre)

    points_O = [centre, [centre[0]+1, centre[1]], [centre[0], centre[1]+1], [centre[0]+1, centre[1]+1]] #centre is bottom left cube
    colour = 1
    if info == 'points':
        return points_O
    if info == 'colour':
        return colour
def I(centre, info):
    check_list_entry(centre)

    points_I = [centre, [centre[0],centre[1]+1], [centre[0],centre[1]+2], [centre[0],centre[1]+3]] #centre is bottom tile
    colour = 2

    if info == 'points':
        return points_I
    if info == 'colour':
        return colour
def T(centre, info):
    check_list_entry(centre)

    points_T = [centre, [centre[0]-1, centre[1]], [centre[0]+1, centre[1]], [centre[0], centre[1]+1]] #centre is middle tile
    colour = 3

    if info == 'points':
        return points_T
    if info == 'colour':
        return colour
def L(centre, info):
    check_list_entry(centre)

    points_L = [centre, [centre[0]+1, centre[1]], [centre[0], centre[1]+1], [centre[0], centre[1]+2]] #centre is tile before bend
    colour = 4

    if info == 'points':
        return points_L
    if info == 'colour':
        return colour
def J(centre, info):
    check_list_entry(centre)

    points_J = [centre, [centre[0]-1, centre[1]], [centre[0], centre[1]+1], [centre[0], centre[1]+2]]
    colour = 5

    if info == 'points':
        return points_J
    if info == 'colour':
        return colour
def z(centre, info):
    check_list_entry(centre)

    points_Z = [centre, [centre[0], centre[1]-1], [centre[0]-1, centre[1]], [centre[0]-1, centre[1]+1]]
    colour = 6

    if info == 'points':
        return points_Z
    if info == 'colour':
        return colour
def S(centre, info):
    check_list_entry(centre)

    points_S = [centre, [centre[0], centre[1]-1], [centre[0]+1, centre[1]], [centre[0]+1, centre[1]+1]]
    colour = 7

    if info == 'points':
        return points_S
    if info == 'colour':
        return colour

def draw(centre_, shape, screen):

    if shape == O:
        points = O(centre_, info = 'points')
        colour = O(centre_, info = 'colour')

    elif shape == I:
        points = I(centre_,info = 'points')
        colour = I(centre_, info = 'colour')

    elif shape == T:
        points = T(centre_, info = 'points')  
        colour = T(centre_, info = 'colour')

    elif shape == L:
        points = L(centre_, info = 'points')
        colour = L(centre_, info = 'colour')

    elif shape == J:
        points = J(centre_, info = 'points')
        colour = J(centre_, info = 'colour')

    elif shape == z:
        points = z(centre_, info = 'points')
        colour = z(centre_, info = 'colour')

    elif shape == S:
        points = S(centre_, info = 'points')
        colour = S(centre_, info = 'colour')

    for coords in points: #points returns a list of lists (a list of tuples hopefully)
        print(points)
        screen[coords[1]][coords[0]] = colour


def check_list_entry(centre):
    if not isinstance(centre,list):
        print("items: " + str(len(centre)))
        raise RuntimeError("centre only takes lists")

def background(size = grid_size):
    Z = [[0 for x in range(size)] for x in range(size)]

    Z[0][1] = 1
    Z[0][2] = 2
    Z[0][3] = 3
    Z[0][4] = 4
    Z[0][5] = 5
    Z[0][6] = 6
    Z[0][7] = 7

    ax.set_xticks([])
    ax.set_yticks([])
    
    return Z

def keypress(event):
    if event.key == 'space':
        pass
        #instant placement
    if event.key == 'down':
        pass
        #speed up placement
    if event.key == 'up':
        pass
        #rotation

def line_break():
    pass
    #if whole line is filled/complete whole line erases

def Z_update(size = grid_size):
    Z = [[0 for x in range(size)] for x in range(size)]

    return Z

def run(x):
    ax.set_xticks([])
    ax.set_yticks([])

    Z = Z_update()
    image.set_data(Z)


fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","yellowgreen","powderblue","lemonchiffon","indianred","thistle","lightpink","orange"])

fig.canvas.mpl_connect('key_press_event', keypress)

image = ax.imshow(background(), origin = 'upper', cmap=cmap)

ani = FuncAnimation(fig, background(), frames = 100, interval = 10, blit = False)
plt.show()