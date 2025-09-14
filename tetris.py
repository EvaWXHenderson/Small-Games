import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import random as rand
import time

grid_size = 21
delt_t = 0.3

frame_rate = 200

loss = False
choices = ['O', 'I', 'T', 'S', 'L', 'J', 'z']

filled_tiles = []
current_shape = ""

screen_shapes = []
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
            self.conformations =[[self.centre, [self.centre[0],self.centre[1]+1], [self.centre[0],self.centre[1]+2], [self.centre[0],self.centre[1]+3]],
                                 [self.centre, [self.centre[0]+1,self.centre[1]], [self.centre[0]+2,self.centre[1]], [self.centre[0]+3,self.centre[1]]]]
            self.colour = 2

            self.form = 0
            self.points = self.conformations[form]

        if type == 'T':
            self.name = 'T'
            self.centre = centre
            self.conformations = [[self.centre,[self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]], [self.centre[0], self.centre[1]+1]],
                                   [self.centre,[self.centre[0], self.centre[1]+1], [self.centre[0], self.centre[1]-1], [self.centre[0]-1, self.centre[1]]],
                                   [self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]], [self.centre[0], self.centre[1]-1]],
                                   [self.centre,[self.centre[0], self.centre[1]+1], [self.centre[0], self.centre[1]-1], [self.centre[0]+1, self.centre[1]]]]
            self.colour = 3

            self.form = 0
            self.points = self.conformations[form]

        if type == 'L':
            self.name = 'L'
            self.centre = centre
            self.conformations = [[self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]-2, self.centre[1]], [self.centre[0], self.centre[1]-1]],
                                  [self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0], self.centre[1]-1], [self.centre[0], self.centre[1]-2]],
                                  [self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0]+2, self.centre[1]], [self.centre[0], self.centre[1]+1]],
                                  [self.centre, [self.centre[0], self.centre[1]+1], [self.centre[0], self.centre[1]+2], [self.centre[0]-1, self.centre[1]]]]
            self.colour = 4

            self.form = 0
            self.points = self.conformations[form]
        
        if type == 'J':
            self.name = 'J'
            self.centre = centre
            self.conformations = [[self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]-2, self.centre[1]], [self.centre[0], self.centre[1]+1]],
                                   [self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0], self.centre[1]-1], [self.centre[0], self.centre[1]-2]],
                                   [self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0]+2, self.centre[1]], [self.centre[0], self.centre[1]-1]],
                                   [self.centre, [self.centre[0], self.centre[1]+1], [self.centre[0]-1, self.centre[1]], [self.centre[0]-2, self.centre[1]]]]
            self.colour = 5

            self.form = 0
            self.points = self.conformations[form]
        
        if type == 'z':
            self.name = 'z'
            self.centre = centre
            self.conformations = [[self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]+1, self.centre[1]+1], [self.centre[0], self.centre[1]+1]],
                                  [self.centre, [self.centre[0], self.centre[1]-1], [self.centre[0]-1, self.centre[1]], [self.centre[0]-1, self.centre[1]+1]]]   
            self.colour = 6

            self.form = 0
            self.points = self.conformations[form]

        if type == 'S':
            self.name = 'S'
            self.centre = centre
            self.conformations = [[self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0]-1, self.centre[1]+1], [self.centre[0], self.centre[1]+1]],
                                [self.centre, [self.centre[0], self.centre[1]-1], [self.centre[0]+1, self.centre[1]], [self.centre[0]+1, self.centre[1]+1]]]
            self.colour = 7

            self.form = 0
            self.points = self.conformations[form]



def change_coords(form, centre, shape = current_shape):
        if shape.name == "O":
            shape.centre = centre
            shape.conformations = [[shape.centre, [shape.centre[0]+1, shape.centre[1]], [shape.centre[0], shape.centre[1]+1], [shape.centre[0]+1, shape.centre[1]+1]]]
            
            shape.form = form
            shape.points = shape.conformations[shape.form]
                  
        if shape.name == "I":
            shape.centre = centre
            shape.conformations =[[shape.centre, [shape.centre[0],shape.centre[1]+1], [shape.centre[0],shape.centre[1]+2], [shape.centre[0],shape.centre[1]+3]],
                                 [shape.centre, [shape.centre[0]+1,shape.centre[1]], [shape.centre[0]+2,shape.centre[1]], [shape.centre[0]+3,shape.centre[1]]]]

            shape.form = form
            shape.points = shape.conformations[shape.form]
        
        if shape.name == "T":
            shape.centre = centre
            shape.conformations = [[shape.centre,[shape.centre[0]-1, shape.centre[1]], [shape.centre[0]+1, shape.centre[1]], [shape.centre[0], shape.centre[1]+1]],
                                   [shape.centre,[shape.centre[0], shape.centre[1]+1], [shape.centre[0], shape.centre[1]-1], [shape.centre[0]-1, shape.centre[1]]],
                                   [shape.centre, [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]+1, shape.centre[1]], [shape.centre[0], shape.centre[1]-1]],
                                   [shape.centre,[shape.centre[0], shape.centre[1]+1], [shape.centre[0], shape.centre[1]-1], [shape.centre[0]+1, shape.centre[1]]]]
            shape.form = form
            shape.points = shape.conformations[shape.form]
        
        if shape.name == "L":
            shape.centre = centre
            shape.conformations = [[shape.centre, [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]-2, shape.centre[1]], [shape.centre[0], shape.centre[1]-1]],
                                  [shape.centre, [shape.centre[0]+1, shape.centre[1]], [shape.centre[0], shape.centre[1]-1], [shape.centre[0], shape.centre[1]-2]],
                                  [shape.centre, [shape.centre[0]+1, shape.centre[1]], [shape.centre[0]+2, shape.centre[1]], [shape.centre[0], shape.centre[1]+1]],
                                  [shape.centre, [shape.centre[0], shape.centre[1]+1], [shape.centre[0], shape.centre[1]+2], [shape.centre[0]-1, shape.centre[1]]]]

            shape.form = form
            shape.points = shape.conformations[shape.form]
        
        if shape.name == "J":
            shape.centre = centre
            shape.conformations = [[shape.centre, [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]-2, shape.centre[1]], [shape.centre[0], shape.centre[1]+1]],
                                   [shape.centre, [shape.centre[0]-1, shape.centre[1]], [shape.centre[0], shape.centre[1]-1], [shape.centre[0], shape.centre[1]-2]],
                                   [shape.centre, [shape.centre[0]+1, shape.centre[1]], [shape.centre[0]+2, shape.centre[1]], [shape.centre[0], shape.centre[1]-1]],
                                   [shape.centre, [shape.centre[0], shape.centre[1]+1], [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]-2, shape.centre[1]]]]

            shape.form = form
            shape.points = shape.conformations[shape.form]
       
        if shape.name == "z":
            shape.centre = centre
            shape.conformations = [[shape.centre, [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]+1, shape.centre[1]+1], [shape.centre[0], shape.centre[1]+1]],
                                  [shape.centre, [shape.centre[0], shape.centre[1]-1], [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]-1, shape.centre[1]+1]]]            

            shape.form = form
            shape.points = shape.conformations[shape.form]
        
        if shape.name == "S":
            shape.centre = centre
            shape.conformations = [[shape.centre, [shape.centre[0]+1, shape.centre[1]], [shape.centre[0]-1, shape.centre[1]+1], [shape.centre[0], shape.centre[1]+1]],
                                [shape.centre, [shape.centre[0], shape.centre[1]-1], [shape.centre[0]+1, shape.centre[1]], [shape.centre[0]+1, shape.centre[1]+1]]]

            shape.form = form
            shape.points = shape.conformations[shape.form]



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
def movement(direction, shape = current_shape):
    global current_shape, can_move

    can_move = True
    hit_b = False

    if direction == "constant":
        change_coords(shape = current_shape, form = shape.form, centre = [shape.centre[0], shape.centre[1]+1])

        hit_bottom()
        
        if hit_b == False:
            hit_shape()
                    #checks points in the current shape, checks if the tile below it (one greater on y and same on x) is filled - if so - shape is redefined and shape is added to filled tiles list

    if direction == "left":

        check_move('left')

        if can_move == True:
            change_coords(shape = current_shape, form = shape.form, centre = [shape.centre[0]-1, shape.centre[1]])
        elif can_move == False:
            pass
        
        set_new_Z()
            
    if direction == "right":

        check_move('right')
        
        if can_move == True:
            change_coords(shape = current_shape, form = shape.form, centre = [shape.centre[0]+1, shape.centre[1]])
        elif can_move == False:
            pass
        
        set_new_Z()

def rotation(shape = current_shape):
        if current_shape.name == 'T' or current_shape.name == 'L' or current_shape.name == 'J':
            if current_shape.form <= 3:
                current_shape.form += 1
            if current_shape.form > 3:
                current_shape.form  = 0
        
        elif current_shape.name == 'S' or current_shape.name == 'z' or current_shape.name == 'I':
            if current_shape.form <= 1:
                current_shape.form += 1
            if current_shape.form > 1:
                current_shape.form  = 0
        
        elif current_shape.name == 'O':
            current_shape.form = 0

        print(str(current_shape.name) + " " + str(current_shape.form))

        #for point in current_shape.points:
            #if point[1] >= 20:
                #print("shape rotation bring points below window")
                #current_shape.centre[1] = 20
        
        change_coords(shape = current_shape, form = current_shape.form, centre = current_shape.centre)
        set_new_Z()

def redefine(shape = current_shape):
    global filled_tiles, current_shape, choices

    past_shape = Shape(type = current_shape.name, centre = current_shape.centre, form = current_shape.form)
    
    filled_tiles.append(past_shape)
    
    choice = rand.choice(choices)
    
    new_shape = Shape(type = choice, centre = [10,0], form = 0) #data for shape stored in current_shape
                                                                    #creates shaped at top border in initial conformation (conformation 0)
    return new_shape
 
def placement():
    global filled_tiles

    x_current = []
    y_current = []

    x_filled = []
    y_filled = []
    
    for point in current_shape.points:
        x_current.append(point[0])
        y_current.append(point[1])

    for tile in filled_tiles:
        for coord in tile.points:
            x_filled.append(coord[0])
            y_filled.append(coord[1])
    
    y_min = min(y_filled)



def hit_bottom():
    global hit_b, current_shape

    for point in current_shape.points:
        if point[1] >= 20: #hits bottom of window
            #print(current_shape.points)
            current_shape = redefine()
            print('shape change - hit bottom of window')
            hit_b = True
            return

def hit_shape():
    global current_shape, filled_tiles

    for point in current_shape.points:
        for shapes in filled_tiles:
            for tile in shapes.points:
                if point[1] + 1 == tile[1] and point[0] == tile[0]:
                    current_shape = redefine()
                    print('shape change - hit other shape')
                    return
    
def check_move(direction):
    global current_shape, can_move, filled_tiles

    if direction == 'left':
        for point in current_shape.points:
            if point[0] <= 0:
                print('shape at left boundary, cannot continue')
                can_move = False

        for point in current_shape.points:
            for shapes in filled_tiles:
                for coord in shapes.points:
                    if point[0] - 1 == coord[0] and point[1]== coord[1]:
                        can_move = False

    if direction == 'right':
        for point in current_shape.points:
            if point[0] >= 20:
                print('shape at right boundary, cannot continue')
                can_move = False

        for point in current_shape.points:
            for shapes in filled_tiles:
                for coord in shapes.points:
                    if point[0] + 1 == coord[0] and point[1] == coord[1]:
                        can_move = False

def speed_place(x = frame_rate):
    x = 100

def keypress(event):
    global frame_rate, can_move, current_shape

    if event.key == '<space>':
        print("space")
        #placement()
        #instant placement
    if event.key == 'down':
        pass
        #frame_rate = 100
        #speed_place()
    
    if event.key == 'up':
        rotation()
    
    if event.key == 'left':
        check_move('left')
        movement(shape = current_shape, direction = "left")
        if can_move == True:
            movement(shape = current_shape, direction = "left")
        else:
            pass
        print(current_shape.points)
   
    if event.key == 'right':
        check_move('right')
        if can_move == True:
            movement(shape = current_shape, direction = "right")
        else:
            pass
        print(current_shape.points)



"""checks"""
def line_break():
    pass
    #if whole line is filled/complete whole line erases

def loss_check():
    global loss
    
    for point in current_shape.points:
        if point[1] <= 0:
            print(point)
            loss = True
            break
    
    if loss == True:
        print('you loose, womp womp.')
        time.sleep(2)
        quit()

def check_error(error):
    global current_shape

    if error == "above window":
        for point in current_shape.points:
            if point[1] < 0:
                print('shape above window threshold')
                print(current_shape.points)
                print(point)
                #quit()
    
    if error == "below window":
        for point in current_shape.points:
            if point[1] > 20:
                print('shape below window threshold')
                print(point)
                #quit()


"""animation"""
def set_new_Z():
    Z = Z_update()
    image.set_data(Z)

def Z_update(size = grid_size):
    Z = [[0 for x in range(size)] for x in range(size)]
    
    for shape in filled_tiles:
        for points in shape.points:
            Z[points[1]][points[0]] = shape.colour

    for point in current_shape.points:
        print([point[1], point[0]])
        Z[point[1]][point[0]] = current_shape.colour
    return Z

def run(x):

   #actions
    movement(shape = current_shape, direction = "constant")
    check_error("above window")
    check_error("below window")
    #print(str(current_shape.name) + str(current_shape.form) + str(current_shape.points))

    ax.set_xticks([])
    ax.set_yticks([])

    Z = Z_update()
    image.set_data(Z)

    #loss_check()



current_shape = Shape(type = rand.choice(choices), centre = [10,0], form = 0)

fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","yellowgreen","powderblue","khaki","indianred","thistle","lightpink","orange"])

fig.canvas.mpl_connect('key_press_event', keypress)

image = ax.imshow(background(), origin = 'upper', cmap=cmap)

ani = FuncAnimation(fig, run, frames = 100, interval = frame_rate, blit = False)
plt.show()

"""print("number of generated shapes: " + str(len(filled_tiles)+1))
for shape in filled_tiles:
    print("tiles on screen: " + str(shape.name) + ". Coords: " + str(shape.centre))
print("current shape: " + str(current_shape.name) + ". Coods: " + str(current_shape.centre))

print(str(current_shape.name) + str(current_shape.form))"""