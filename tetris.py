import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import random as rand

grid_size = 21
delt_t = 0.3

filled_tiles = []
screen_shapes = []

class Shape:
    def __init__(self, type):
        if type == 'O':
            self.centre = [10,10]

            self.conformations = [[self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0], self.centre[1]+1], [self.centre[0]+1, self.centre[1]+1]]]
            self.colour = 1
        
            screen_shapes.append(self)

        if type == 'I':
            self.centre = [10,10]

            self.conformations =[[self.centre, [self.centre[0],self.centre[1]+1], [self.centre[0],self.centre[1]+2], [self.centre[0],self.centre[1]+3]],
                                 [self.centre, [self.centre[0]+1,self.centre[1]], [self.centre[0]+2,self.centre[1]], [self.centre[0]+3,self.centre[1]]]]
            self.colour = 2

            screen_shapes.append(self)

        if type == 'T':
            self.centre = [10,10]

            self.conformations = [[self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]], [self.centre[0], self.centre[1]+1]],
                                  [self.centre,[self.centre[0], self.centre[1]+1], [self.centre[0], self.centre[1]-1], [self.centre[0]+1, self.centre[1]]],
                                  [self.centre,[self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]], [self.centre[0], self.centre[1]-1]],
                                  [self.centre,[self.centre[0]-1, self.centre[1]], [self.centre[0], self.centre[1]-1], [self.centre[0], self.centre[1]+1]]]
            self.colour = 3

            screen_shapes.append(self)

        if type == 'L':
            self.centre = [10,10]

            self.conformations = [[self.centre, [self.centre[0], self.centre[1]-1], [self.centre[0], self.centre[1]+1], [self.centre[0]-1, self.centre[1]-1]],
                                  [self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]], [self.centre[0]-1, self.centre[1]+1]],
                                  [self.centre, [self.centre[0]+1, self.centre[1]+1], [self.centre[0], self.centre[1]+1], [self.centre[0], self.centre[1]-1]],
                                  [self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]-1], [self.centre[0]+1, self.centre[1]]]]
            self.colour = 4

            screen_shapes.append(self)

        if type == 'J':
            self.centre = [10,10]

            self.conformations = [[self.centre, [self.centre[0]+1, self.centre[1]-1], [self.centre[0], self.centre[1]+1], [self.centre[0], self.centre[1]-1]],
                                  [self.centre, [self.centre[0]-1, self.centre[1]-1], [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]]],
                                  [self.centre, [self.centre[0]-1, self.centre[1]+1], [self.centre[0], self.centre[1]+1], [self.centre[0], self.centre[1]-1]],
                                  [self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0]+1, self.centre[1]+1], [self.centre[0]-1, self.centre[1]]]]
            self.colour = 5

            screen_shapes.append(self)
        
        if type == 'z':
            self.centre = [10,10]

            self.conformations = [[self.centre, [self.centre[0], self.centre[1]-1], [self.centre[0]-1, self.centre[1]], [self.centre[0]-1, self.centre[1]+1]],
                                  [self.centre, [self.centre[0], self.centre[1]-1], [self.centre[0]-1, self.centre[1]-1], [self.centre[0]+1, self.centre[1]]]]
            self.colour = 6

            screen_shapes.append(self)

        if type == 'S':
            self.centre = [10,10]
            
            self.conformations = [[self.centre, [self.centre[0], self.centre[1]-1], [self.centre[0]+1, self.centre[1]], [self.centre[0]+1, self.centre[1]+1]],
                                  [self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0]-1, self.centre[1]+1], [self.centre[0], self.centre[1]+1]]]
            self.colour = 7

            screen_shapes.append(self)



"""for drawing shapes and assigning colours""" 
def draw(shape, form, screen):
    points = shape.conformation[form] #a list of points corresponding to desired conformation (form)
    colour = shape.colour #an integer colour output (1-7)

    for coords in points:
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

    #draw(centre_ = [10,10], shape = z, screen=Z)

    ax.set_xticks([])
    ax.set_yticks([])
    
    return Z

def movement(centre_, shape):
    pass
    #shapes move down at a rate of delta t 

def rotation(shape, centre_, conformation):
    #create list of conformations - for every up click, the next conformation is chosen
    if shape == I:
        conformations = I(info = 'conformations')
        if conformation == 0:
            form = conformations[0]
        if conformation == 1:
            form = conformations[1]
        #I has only 1 other conformation
    
    elif shape == T:
        centre_ = T(info = 'points')
        conformations = T(info = 'conformations')
        if conformation == 0:
            form = conformations[0]        
        if conformation == 1:
            form = conformations[1]
        elif conformation == 2:
            form = conformations[2]
        elif conformation == 3:
            form = conformations[3]

        #T has 4 conformations (3 other)
    
    elif shape == L:
        centre_ = L(info = 'points')
        conformations = L(info = 'conformations')
        if conformation == 0:
            form = conformations[0]
        if conformation == 1:
            form = conformations[1]
        elif conformation == 2:
            form = conformations[2]
        elif conformation == 3:
            form = conformations[3]

        #L has 4 conformations (3 other)
    
    elif shape == J:
        centre_ = J(info = 'points')
        conformations = J(info = 'conformations')
        if conformation == 0:
            form = conformations[0]
        if conformation == 1:
            form = conformations[1]
        elif conformation == 2:
            form = conformations[2]
        elif conformation == 3:
            form = conformations[3]

        #J has 4 conformations (3 other)
    
    elif shape == z:
        centre_ = z(info = 'points')
        conformations = z(info = 'conformations')
        if conformation == 0:
            form = conformations[0]
        if conformation == 1:
            form = conformations[1]

        #z has 4 conformations (3 other)
    
    elif shape == S:
        centre_ = S(info = 'points')
        conformations = S(info = 'conformations')
        if conformation == 0:
            form = conformations[0]
        if conformation == 1:
            form = conformations[1]

        #S has 4 conformations (3 other)
    
    return form
    #rotation of shape when up pressed - gets points for the form wanted to then input into the draw function...

def keypress(event):
    if event.key == 'space':
        pass
        #instant placement
    if event.key == 'down':
        pass
        #speed up placement
    if event.key == 'up':
        counter += 1
        rotation(conformation = counter)
        #rotation - needs shape input and centre input - O shape has no rotation

"""def line_break():
    for x in range(grid_size):
        for y in range(grid_size):
            if Z[x][y] == 0:
    pass
    #if whole line is filled/complete whole line erases"""

def Z_update(size = grid_size):
    Z = [[0 for x in range(size)] for x in range(size)]

    return Z

def chose_shape():
    choice = rand.randint(0, 7)
    if choice == 1:
        shape = O
    elif choice == 2:
        shape = I
    elif choice == 3:
        shape = T
    elif choice == 4:
        shape = L
    elif choice == 5:
        shape = J
    elif choice == 6:
        shape = z
    elif choice == 7:
        shape = S
    
    return shape

def placement(shape):
    pass
    #to define whether a piece has been placed

def run(x):
    ax.set_xticks([])
    ax.set_yticks([])

    Z = Z_update()
    image.set_data(Z)


fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","yellowgreen","powderblue","khaki","indianred","thistle","lightpink","orange"])

fig.canvas.mpl_connect('key_press_event', keypress)

image = ax.imshow(background(), origin = 'upper', cmap=cmap)

ani = FuncAnimation(fig, background(), frames = 100, interval = 10, blit = False)
plt.show()