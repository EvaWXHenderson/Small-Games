import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots(figsize = (5,5))
plt.title('Tic-Tac-Toe')
cmap = ListedColormap(["white","black", "blue", "red"])

grid_size = 60
turn = 0

"""Boxes"""
1_1 = None
2_1 = None
3_1 = None

1_2 = None
2_2= None
3_2 = None

1_3 = None
2_3 = None
3_3 = None

class player:
    def __innit__(self, name):
        if name == 'knots':
            self.name = name
            self.colour = 2

        if name == 'crosses':
            self.name = 'crosses'
            self.colour = 3

def create_players(player1 = 'knots', player2 = 'crosses'):
    global knots, crosses

    knots = player(player1)
    crosses = player(player2)

def grid(size = grid_size):
    Z = [[0 for x in range(size)] for x in range(size)]
    for axis in range(0, 60):
        Z[axis] [20] = 1  
        Z[axis] [40] = 1  
        Z[20] [axis] = 1 
        Z[40] [axis] = 1
    return Z

def select(event):
    iy, ix= round(event.xdata), round(event.ydata)
    Z_update(x = ix, y = iy, player = None)

def Z_update(x, y, player):
    if x<20:
        if y < 20:
            Z[10][10] = player #knots or crosses
            1_1 = player
        elif y < 40 and y > 20:
            Z[10][30] = player
            2_1 = player
        elif y < 60 and y > 40:
            Z[10][50] = player
            3_1 = player

    if x<40 and x>20:
        if y < 20:
            Z[30][10] = player #knots or crosses
            1_2 = player
        elif y < 40 and y > 20:
            Z[30][30] = player
            2_2 = player
        elif y < 60 and y > 40:
            Z[30][50] = player 
            3_2 = player      

    if x<60 and x>40:
        if y < 20:
            Z[50][10] = player #knots or crosses
            1_3 = player
        elif y < 40 and y > 20:
            Z[50][30] = player
            2_3 = player
        elif y < 60 and y > 40:
            Z[50][50] = player 
            3_3 = player 

def check_win():
    pass

fig.canvas.mpl_connect('button_press_event', select)

Z = grid()
ax.imshow(Z, origin = 'upper', cmap=cmap)
plt.show()