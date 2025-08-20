import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

grid_size = 60
turn = 0

"""Boxes"""
grid_boxes = [[0,0,0], 
              [0,0,0], 
              [0,0,0]]

grid_coords = [[(10,50),(30,50),(50,50)], 
              [(10,30),(30,30),(50,30)], 
              [(10,10),(30,10),(50,10)]]



class player:
    def __innit__(self, name):
        if name == 'knots':
            self.name = name
            self.colour = 2

        if name == 'crosses':
            self.name = name
            self.colour = 3

def create_players(player1 = 'knots', player2 = 'crosses'):
    global knots, crosses

    knots = player(player1)
    crosses = player(player2)



"""def grid(size = grid_size):
    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(0, 60):
        Z[axis] [20] = 1  
        Z[axis] [40] = 1  
        Z[20] [axis] = 1 
        Z[40] [axis] = 1
    return Z"""

def grid_update(x, y):
    global grid_boxes, Z

    if x<20:
        if y < 20:
            grid_boxes[2][0] = 2
        elif y < 40 and y > 20:
            grid_boxes[2][1] = 2
        elif y < 60 and y > 40:
            grid_boxes[2][2] = 2

    if x<40 and x>20:
        if y < 20:
            grid_boxes[1][0] = 2
        elif y < 40 and y > 20:
            grid_boxes[1][1] = 2
        elif y < 60 and y > 40:
            grid_boxes[1][2] = 2

    if x<60 and x>40:
        if y < 20:
            grid_boxes[0][0] = 2
        elif y < 40 and y > 20:
            grid_boxes[0][1] = 2
        elif y < 60 and y > 40:
            grid_boxes[0][2] = 2

    return grid_boxes

def Z_update(size = grid_size, grid = grid_boxes, coords = grid_coords):
    Z_coords = []

    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(0, 60):
        Z[axis] [20] = 1  
        Z[axis] [40] = 1  
        Z[20] [axis] = 1 
        Z[40] [axis] = 1

    for row in range(len(grid)):
        for x in range(3):
            if grid[row][x] == 2:
                Z_coords.append(coords[row][x])

    for coord in Z_coords:
        Z[coord[0]][coord[1]] = 1
    
    return Z

def anim_data(frame):    
    Z = Z_update()
    image.set_data(Z)
    return [image]

def select(event):
    global ix, iy, grid_boxes, turn

    turn += 1 #if turn odd => player1, if turn even => player2

    ix, iy= round(event.xdata), round(event.ydata)

    grid_boxes = grid_update(x = ix, y = iy)
    anim_data()

def check_win():
    pass






print("Crosses go first :3. ")

plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","black"])

fig.canvas.mpl_connect('button_press_event', select)

image = ax.imshow(Z_update(), origin = 'upper', cmap=cmap)
ani = FuncAnimation(fig, anim_data, frames = 100, interval = 200, blit = False)
plt.show()

print(grid_boxes)