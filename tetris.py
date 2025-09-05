import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import random as rand

grid_size = 21
delt_t = 0.3

filled_tiles = []
screen_shapes = []
current_shape = ""

shape_form = ""


"""defining shapes, their points of origin, conformation, colour, etc."""
class Shape:
    def __init__(self, type, centre, form):
        if type == 'O':
            self.name = 'O'
            self.centre = centre

            self.conformations = [[self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0], self.centre[1]+1], [self.centre[0]+1, self.centre[1]+1]]]
            self.colour = 1

            self.form = self.conformations[form]

        if type == 'I':
            self.name = 'I'
            self.centre = centre

            self.conformations =[[self.centre, [self.centre[0],self.centre[1]+1], [self.centre[0],self.centre[1]+2], [self.centre[0],self.centre[1]+3]],
                                 [self.centre, [self.centre[0]+1,self.centre[1]], [self.centre[0]+2,self.centre[1]], [self.centre[0]+3,self.centre[1]]]]
            self.colour = 2

            self.form = self.conformations[form]

        if type == 'T':
            self.name = 'T'
            self.centre = centre

            self.conformations = [[self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]], [self.centre[0], self.centre[1]+1]],
                                  [self.centre,[self.centre[0], self.centre[1]+1], [self.centre[0], self.centre[1]-1], [self.centre[0]+1, self.centre[1]]],
                                  [self.centre,[self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]], [self.centre[0], self.centre[1]-1]],
                                  [self.centre,[self.centre[0]-1, self.centre[1]], [self.centre[0], self.centre[1]-1], [self.centre[0], self.centre[1]+1]]]
            self.colour = 3

            self.form = self.conformations[form]

        if type == 'L':
            self.name = 'L'
            self.centre = centre

            self.conformations = [[self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]], [self.centre[0]-1, self.centre[1]+1]],
                                  [self.centre, [self.centre[0], self.centre[1]-1], [self.centre[0], self.centre[1]+1], [self.centre[0]-1, self.centre[1]-1]],
                                  [self.centre, [self.centre[0]+1, self.centre[1]+1], [self.centre[0], self.centre[1]+1], [self.centre[0], self.centre[1]-1]],
                                  [self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]-1], [self.centre[0]+1, self.centre[1]]]]
            self.colour = 4

            self.form = self.conformations[form]

        if type == 'J':
            self.name = 'J'
            self.centre = centre

            self.conformations = [[self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0]+1, self.centre[1]+1], [self.centre[0]-1, self.centre[1]]],
                                  [self.centre, [self.centre[0]+1, self.centre[1]-1], [self.centre[0], self.centre[1]+1], [self.centre[0], self.centre[1]-1]],
                                  [self.centre, [self.centre[0]-1, self.centre[1]-1], [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]]],
                                  [self.centre, [self.centre[0]-1, self.centre[1]+1], [self.centre[0], self.centre[1]+1], [self.centre[0], self.centre[1]-1]]]
            self.colour = 5

            self.form = self.conformations[form]
        
        if type == 'z':
            self.name = 'z'
            self.centre = centre

            self.conformations = [[self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]+1], [self.centre[0], self.centre[1]+1]],
                                  [self.centre, [self.centre[0], self.centre[1]-1], [self.centre[0]-1, self.centre[1]], [self.centre[0]-1, self.centre[1]+1]]]
            self.colour = 6

            self.form = self.conformations[form]

        if type == 'S':
            self.name = 'S'
            self.centre = centre
            
            self.conformations = [[self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0]-1, self.centre[1]+1], [self.centre[0], self.centre[1]+1]],
                                  [self.centre, [self.centre[0], self.centre[1]-1], [self.centre[0]+1, self.centre[1]], [self.centre[0]+1, self.centre[1]+1]]]
            self.colour = 7

            self.form = self.conformations[form]



"""for drawing shapes and assigning colours""" 
def draw(shape, form, screen):
    points = shape.conformations[form] #a list of points corresponding to desired conformation (form)
    colour = shape.colour #an integer colour output (1-7)

    for coords in points:
        screen[coords[1]][coords[0]] = colour



def background(size = grid_size):
    Z = [[0 for x in range(size)] for x in range(size)]

    Z[0][1] = 1
    Z[0][2] = 2
    Z[0][3] = 3
    Z[0][4] = 4
    Z[0][5] = 5
    Z[0][6] = 6
    Z[0][7] = 7

    draw(shape = sshape , form = 1, screen=Z)

    ax.set_xticks([])
    ax.set_yticks([])
    
    return Z


"""actions"""
def shape_gen():
    global new_shape, current_shape

    choices = ['O', 'I', 'T', 'S', 'L', 'J', 'z']
    choice = rand.choice(choices)
    
    if new_shape == True:
        current_shape = Shape(type = choice, centre = [10,1], form = 0) #data for shape stored in current_shape
                                                                        #creates shaped at top border in initial conformation (conformation 0)

def movement(shape, direction):
    if direction == "constant":
        shape.centre = [shape.centre[0], shape.centre[1]+1]
        #shapes move down 1 tile with each frame???

    if direction == "left":
        shape.centre = [shape.centre[0]-1, shape.centre[1]]
    if direction == "right":
        shape.centre = [shape.centre[0]+1, shape.centre[1]]

def rotation(shape = current_shape):
    #create list of conformations - for every up click, the next conformation is chosen
    if shape.name == 'L' or shape.name == 'J' or shape.name == 'S' or shape.name == 'z' or shape.name == 'T':
        counter += 1
        if counter > 4:
            counter = 0
    
    if shape.name == 'I':
        counter += 1
        if counter > 2:
            counter = 0
    
    if shape.name == 'O':
        counter = 0
    
    form = shape.conformation[counter]
    
    return form
    #rotation of shape when up pressed - gets points for the form wanted to then input into the draw function...

def placement(shape):
    global current_shape, new_shape, shape_form

    current_shape = []
    new_shape = True
    filled_tiles.append(shape_form) #adds now placed/coloured tiles to list
    
    #to define whether a piece has been placed - should put shape at the highest unoccupied value of Y
    #clears list containing the current shape and indicated for next shape to generated and added

def speed_place():
    pass

def keypress(event):
    global shape_form

    if event.key == 'space':
        placement()
        #instant placement
    if event.key == 'down':
        speed_place()
        #speed up placement - change delt_t (independent of frames) or link to framerate???
    if event.key == 'up':
        counter += 1
        shape_form = rotation(shape = current_shape[0], conformation = counter)
        #rotation - needs shape input and centre input - O shape has no rotation
    
    if event.key == 'left':
        movement(shape = current_shape[0], direction = "left")
    if event.key == 'right':
        movement(shape = current_shape[0], direction = "right")
    #need to define the shape in current use



"""checks"""
def line_break():
    pass
    #if whole line is filled/complete whole line erases

def loss_check():
    pass


"""animation"""
def Z_update(size = grid_size):
    Z = [[0 for x in range(size)] for x in range(size)]

    return Z

def run(x):
    new_shape = False

   #actions 
    shape_gen()
    movement(shape = current_shape[0], direction = "constant")
    
   #checks 
    line_break()
    loss_check()

    ax.set_xticks([])
    ax.set_yticks([])

    Z = Z_update()
    image.set_data(Z)




sshape = Shape(type = 'S', centre=[10,0])

fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","yellowgreen","powderblue","khaki","indianred","thistle","lightpink","orange"])

fig.canvas.mpl_connect('key_press_event', keypress)

image = ax.imshow(background(), origin = 'upper', cmap=cmap)

ani = FuncAnimation(fig, run(), frames = 100, interval = 10, blit = False)
plt.show()