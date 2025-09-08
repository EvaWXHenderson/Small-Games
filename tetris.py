import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import random as rand

grid_size = 21
delt_t = 0.3

frame_rate = 1000

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
            
            self.form = 0
            self.points = self.conformations[form]

        if type == 'I':
            self.name = 'I'
            self.centre = centre
            self.conformations =[[self.centre, [self.centre[0],self.centre[1]+1], [self.centre[0],self.centre[1]+2], [self.centre[0],self.centre[1]+3]]]
            self.colour = 2

            self.form = 0
            self.points = self.conformations[form]

        if type == 'T':
            self.name = 'T'
            self.centre = centre
            self.conformations = [[self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]], [self.centre[0], self.centre[1]+1]]]
            self.colour = 3

            self.form = 0
            self.points = self.conformations[form]

        if type == 'L':
            self.name = 'L'
            self.centre = centre
            self.conformations = [[self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]], [self.centre[0]-1, self.centre[1]+1]]]
            self.colour = 4

            self.form = 0
            self.points = self.conformations[form]
        
        if type == 'J':
            self.name = 'J'
            self.centre = centre
            self.conformations = [[self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0]+1, self.centre[1]+1], [self.centre[0]-1, self.centre[1]]]]
            self.colour = 5

            self.form = 0
            self.points = self.conformations[form]
        
        if type == 'z':
            self.name = 'z'
            self.centre = centre
            self.conformations = [[self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]+1], [self.centre[0], self.centre[1]+1]]]
            self.colour = 6

            self.form = 0
            self.points = self.conformations[form]

        if type == 'S':
            self.name = 'S'
            self.centre = centre
            self.conformations = [[self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0]-1, self.centre[1]+1], [self.centre[0], self.centre[1]+1]]]
            self.colour = 7

            self.form = 0
            self.points = self.conformations[form]



def change_coords(form, centre, shape = current_shape):
        if shape.name == "O":
            shape.centre = centre
            shape.conformations = [[shape.centre, [shape.centre[0]+1, shape.centre[1]], [shape.centre[0], shape.centre[1]+1], [shape.centre[0]+1, shape.centre[1]+1]]]
            
            shape.form = form
            shape.points = shape.conformations[form]
                  
        if shape.name == "I":
            shape.centre = centre
            shape.conformations =[[shape.centre, [shape.centre[0],shape.centre[1]+1], [shape.centre[0],shape.centre[1]+2], [shape.centre[0],shape.centre[1]+3]],
                                 [shape.centre, [shape.centre[0]+1,shape.centre[1]], [shape.centre[0]+2,shape.centre[1]], [shape.centre[0]+3,shape.centre[1]]]]

            shape.form = form
            shape.points = shape.conformations[form]
        
        if shape.name == "T":
            shape.centre = centre
            shape.conformations = [[shape.centre, [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]+1, shape.centre[1]], [shape.centre[0], shape.centre[1]+1]],
                                  [shape.centre,[shape.centre[0], shape.centre[1]+1], [shape.centre[0], shape.centre[1]-1], [shape.centre[0]+1, shape.centre[1]]],
                                  [shape.centre,[shape.centre[0]-1, shape.centre[1]], [shape.centre[0]+1, shape.centre[1]], [shape.centre[0], shape.centre[1]-1]],
                                  [shape.centre,[shape.centre[0]-1, shape.centre[1]], [shape.centre[0], shape.centre[1]-1], [shape.centre[0], shape.centre[1]+1]]]
            shape.form = form
            shape.points = shape.conformations[form]
        
        if shape.name == "L":
            shape.centre = centre
            shape.conformations = [[shape.centre, [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]+1, shape.centre[1]], [shape.centre[0]-1, shape.centre[1]+1]],
                                  [shape.centre, [shape.centre[0], shape.centre[1]-1], [shape.centre[0], shape.centre[1]+1], [shape.centre[0]-1, shape.centre[1]-1]],
                                  [shape.centre, [shape.centre[0]+1, shape.centre[1]+1], [shape.centre[0], shape.centre[1]+1], [shape.centre[0], shape.centre[1]-1]],
                                  [shape.centre, [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]+1, shape.centre[1]-1], [shape.centre[0]+1, shape.centre[1]]]]

            shape.form = form
            shape.points = shape.conformations[form]
        
        if shape.name == "J":
            shape.centre = centre
            shape.conformations = [[shape.centre, [shape.centre[0]+1, shape.centre[1]], [shape.centre[0]+1, shape.centre[1]+1], [shape.centre[0]-1, shape.centre[1]]],
                                  [shape.centre, [shape.centre[0]+1, shape.centre[1]-1], [shape.centre[0], shape.centre[1]+1], [shape.centre[0], shape.centre[1]-1]],
                                  [shape.centre, [shape.centre[0]-1, shape.centre[1]-1], [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]+1, shape.centre[1]]],
                                  [shape.centre, [shape.centre[0]-1, shape.centre[1]+1], [shape.centre[0], shape.centre[1]+1], [shape.centre[0], shape.centre[1]-1]]]

            shape.form = form
            shape.points = shape.conformations[form]
       
        if shape.name == "z":
            shape.centre = centre
            shape.conformations = [[shape.centre, [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]+1, shape.centre[1]+1], [shape.centre[0], shape.centre[1]+1]],
                                  [shape.centre, [shape.centre[0], shape.centre[1]-1], [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]-1, shape.centre[1]+1]]]            

            shape.form = form
            shape.points = shape.conformations[form]
        
        if shape.name == "S":
            shape.centre = centre
            shape.conformations = [[shape.centre, [shape.centre[0]+1, shape.centre[1]], [shape.centre[0]-1, shape.centre[1]+1], [shape.centre[0], shape.centre[1]+1]],
                                [shape.centre, [shape.centre[0], shape.centre[1]-1], [shape.centre[0]+1, shape.centre[1]], [shape.centre[0]+1, shape.centre[1]+1]]]

            shape.form = form
            shape.points = shape.conformations[form]



"""for drawing shapes and assigning colours""" 
def draw(shape, form, screen):
    points = shape.conformations[form] #a list of points corresponding to desired conformation (form)
    colour = shape.colour #an integer colour output (1-7)

    for coords in points:
        screen[coords[1]][coords[0]] = colour


"""background setting - allow all colours to set"""
def background(size = grid_size):
    Z = [[0 for x in range(size)] for x in range(size)]

    Z[0][1] = 1
    Z[0][2] = 2
    Z[0][3] = 3
    Z[0][4] = 4
    Z[0][5] = 5
    Z[0][6] = 6
    Z[0][7] = 7

    #draw(shape = current_shape , form = 1, screen=Z)

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
    can_move = True

    if direction == "constant":
        change_coords(shape = current_shape, form = current_shape.form, centre = [shape.centre[0], shape.centre[1]+1])
        if shape.centre[1] >= 20: #needs changed to bottom of window or coloured tile
            placement()
        #shapes move down 1 tile with each frame???

    if direction == "left":
        for point in shape.form:
            if point[0] <= 0:
                can_move = False

        if can_move == True:
            change_coords(current_shape, current_shape.name, 0, [shape.centre[0]-1, shape.centre[1]])
            
    if direction == "right":
        for point in shape.form:
            if point[0] >= 20:
                can_move = False
        
        if can_move == True:
            change_coords(current_shape, current_shape.name, 0, [shape.centre[0]-1, shape.centre[1]])

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

def placement():
    global current_shape, new_shape

    filled_tiles.append(current_shape)

    current_shape = ""
    new_shape = True
    #to define whether a piece has been placed - should put shape at the highest unoccupied value of Y
    #clears list containing the current shape and indicated for next shape to generated and added

def speed_place(x = frame_rate):
    x = 100

def keypress(event):
    global shape_form

    if event.key == '<space>':
        print("space")
        #placement()
        #instant placement
    if event.key == 'down':
        print("down")
        #speed_place()
        #speed up placement - change delt_t (independent of frames) or link to framerate???
    
    if event.key == 'up':
        if current_shape.name == 'T' or current_shape.name == 'L' or current_shape.name == 'J':
            if current_shape.form <= 3:
                current_shape.form +=1
            if current_shape.form > 3:
                current_shape.form = 0
        
        if current_shape.name == 'S' or current_shape.name == 'z' or current_shape.name == 'I':
            if current_shape.form <= 1:
                current_shape.form +=1
            if current_shape.form > 1:
                current_shape.form = 0
        
        if current_shape.name == 'O':
            current_shape.form = 0
        
        change_coords(shape = current_shape, form = current_shape.form, centre = current_shape.centre)
        set_new_Z()
    
    if event.key == 'left':
        print("left")
        #movement(shape = current_shape, direction = "left")
    if event.key == 'right':
        print("right")
        #movement(shape = current_shape, direction = "right")
    #need to define the shape in current use



"""checks"""
def line_break():
    pass
    #if whole line is filled/complete whole line erases

def loss_check():
    pass



"""animation"""
def set_new_Z():
    Z = Z_update()
    image.set_data(Z)

def Z_update(size = grid_size):
    Z = [[0 for x in range(size)] for x in range(size)]

    for tile in filled_tiles:
        Z[tile.conformations[0]][tile.conformation[1]] = tile.colour

    for point in current_shape.points:
        Z[point[1]][point[0]] = current_shape.colour
    return Z

def run(x):
    new_shape = False

   #actions 
    #shape_gen()
    movement(shape = current_shape, direction = "constant")
    
   #checks 
    #line_break()
    #loss_check()

    ax.set_xticks([])
    ax.set_yticks([])

    Z = Z_update()
    image.set_data(Z)



current_shape = Shape(type = 'S', centre = [10,0], form = 0)

fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","yellowgreen","powderblue","khaki","indianred","thistle","lightpink","orange"])

fig.canvas.mpl_connect('key_press_event', keypress)

image = ax.imshow(background(), origin = 'upper', cmap=cmap)

ani = FuncAnimation(fig, run, frames = 100, interval = frame_rate, blit = False)
plt.show()