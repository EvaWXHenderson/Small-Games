import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import tkinter as tk

grid_size = 60
turn = 0

"""Boxes"""
grid_boxes = [[0,0,0], 
              [0,0,0], 
              [0,0,0]]

grid_coords = [[(10,50),(30,50),(50,50)], 
              [(10,30),(30,30),(50,30)], 
              [(10,10),(30,10),(50,10)]]



def grid(size = grid_size):
    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(0, 60):
        Z[axis] [20] = 1  
        Z[axis] [40] = 1  
        Z[20] [axis] = 1 
        Z[40] [axis] = 1

        Z[50][41] = 2 #to introduce all cmap colours
        Z[30][38] = 3
    return Z

def grid_update(x, y):
    global grid_boxes, Z, turn

    if turn == 0:
        return Z
    
    if turn%2 == 0:
       colour = 2
    if turn%2 != 0 :
        colour = 3

    if x<20:
        if y < 20:
            grid_boxes[2][0] = colour
        elif y < 40 and y > 20:
            grid_boxes[2][1] = colour
        elif y < 60 and y > 40:
            grid_boxes[2][2] = colour

    if x<40 and x>20:
        if y < 20:
            grid_boxes[1][0] = colour
        elif y < 40 and y > 20:
            grid_boxes[1][1] = colour
        elif y < 60 and y > 40:
            grid_boxes[1][2] = colour

    if x<60 and x>40:
        if y < 20:
            grid_boxes[0][0] = colour
        elif y < 40 and y > 20:
            grid_boxes[0][1] = colour
        elif y < 60 and y > 40:
            grid_boxes[0][2] = colour

    return grid_boxes

def print_winner(player):
    root = tk(screenName=None, baseName=None, className='tk', useTk=1)

def check_win():
    twos = 0
    threes = 0

    for row in grid_boxes:
        if row[0]==3 and row[1]==3 and row[2]==3:
            print('PLAYER 1 - WIN!')
            quit()
        elif row[0]==2 and row[1]==2 and row[2]==2:
            print('PLAYER 2 - WIN!')
            print('faulty - 1')
            quit()
    
    for i in range(3):
        if grid_boxes[0][i]==3 and grid_boxes[0][i]==grid_boxes[1][i] and grid_boxes[1][i]==grid_boxes[2][i]:
            print('PLAYER 1 - WIN!')
            quit()
        if grid_boxes[0][i]==2 and grid_boxes[0][i]==grid_boxes[1][i] and grid_boxes[1][i]==grid_boxes[2][i]:
            print('PLAYER 2 - WIN!')
            print('faulty - 2')
            quit()
    
    if grid_boxes[0][0]==3 and grid_boxes[0][0]==grid_boxes[1][1] and grid_boxes[1][1]==grid_boxes[2][2]:
        print('PLAYER 1 - WIN!')
        quit()
    elif grid_boxes[0][0]==2 and grid_boxes[0][0]==grid_boxes[1][1] and grid_boxes[1][1]==grid_boxes[2][2]:
        print('PLAYER 2 - WIN!')
        print('faulty - 3')
        quit()


    if grid_boxes[0][2]==3 and grid_boxes[0][2]==grid_boxes[1][1] and grid_boxes[1][1] ==grid_boxes[2][0]:
        print('PLAYER 1 - WIN!')
        quit()
    elif grid_boxes[0][2]==2 and grid_boxes[0][2]==grid_boxes[1][1] and grid_boxes[1][1] ==grid_boxes[2][0]:
        print('PLAYER 2 - WIN!')
        print('faulty - 4')
        quit()

def Z_update(size = grid_size, grid = grid_boxes, coords = grid_coords):
    global Z_coords_1, Z_coords_2

    Z_coords_1 = []
    Z_coords_2 = []

    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(0, 60):
        Z[axis] [20] = 1  
        Z[axis] [40] = 1  
        Z[20] [axis] = 1 
        Z[40] [axis] = 1
    

    for row in range(len(grid)):
        for x in range(3):
            if grid[row][x] == 2:
                Z_coords_1.append(coords[row][x])
            elif grid[row][x] == 3:
                 Z_coords_2.append(coords[row][x])

    for coord in Z_coords_1:
        Z[coord[0]][coord[1]] = 2
    
    for coord in Z_coords_2:
        Z[coord[0]][coord[1]] = 3
        Z[coord[0]+1][coord[1]+1] = 3
        Z[coord[0]-1][coord[1]-1] = 3
        Z[coord[0]-1][coord[1]+1] = 3
        Z[coord[0]+1][coord[1]-1] = 3

    return Z

def anim_data(frame):  
    Z = Z_update()
    image.set_data(Z)
    check_win()
    return [image]

def select(event):
    global ix, iy, grid_boxes, turn

    turn += 1 #if turn odd => player1, if turn even => player2

    ix, iy= round(event.xdata), round(event.ydata)

    grid_boxes = grid_update(x = ix, y = iy)





plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","black","powderblue","yellowgreen"])

fig.canvas.mpl_connect('button_press_event', select)

image = ax.imshow(grid(), origin = 'upper', cmap=cmap)
image.set_data(Z_update())

ani = FuncAnimation(fig, anim_data, frames = 100, interval = 100, blit = False)
plt.show()

print(grid_boxes)