import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import random as rand
import time

grid_size = 20
delt_t = 0.3

frame_rate = 200

loss = False
#placed = False
update = False
coord_remove = []
choices = ['O', 'I', 'T', 'S', 'L', 'J', 'z']

filled_tiles = []
filled_tile_colours = []
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
            self.conformations = [[self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0]+2, self.centre[1]], [self.centre[0], self.centre[1]+1]],
                                  [self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]-2, self.centre[1]], [self.centre[0], self.centre[1]-1]],
                                  [self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0], self.centre[1]-1], [self.centre[0], self.centre[1]-2]],
                                  [self.centre, [self.centre[0], self.centre[1]+1], [self.centre[0], self.centre[1]+2], [self.centre[0]-1, self.centre[1]]]]
            self.colour = 4

            self.form = 0
            self.points = self.conformations[form]
        
        if type == 'J':
            self.name = 'J'
            self.centre = centre
            self.conformations = [[self.centre, [self.centre[0]+1, self.centre[1]], [self.centre[0]+2, self.centre[1]], [self.centre[0], self.centre[1]-1]],
                                  [self.centre, [self.centre[0], self.centre[1]+1], [self.centre[0]-1, self.centre[1]], [self.centre[0]-2, self.centre[1]]],
                                  [self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0], self.centre[1]-1], [self.centre[0], self.centre[1]-2]],
                                  [self.centre, [self.centre[0]-1, self.centre[1]], [self.centre[0]-2, self.centre[1]], [self.centre[0], self.centre[1]+1]]]
                                   
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
            shape.conformations = [[shape.centre, [shape.centre[0]+1, shape.centre[1]], [shape.centre[0]+2, shape.centre[1]], [shape.centre[0], shape.centre[1]+1]],
                                  [shape.centre, [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]-2, shape.centre[1]], [shape.centre[0], shape.centre[1]-1]],
                                  [shape.centre, [shape.centre[0]+1, shape.centre[1]], [shape.centre[0], shape.centre[1]-1], [shape.centre[0], shape.centre[1]-2]],
                                  [shape.centre, [shape.centre[0], shape.centre[1]+1], [shape.centre[0], shape.centre[1]+2], [shape.centre[0]-1, shape.centre[1]]]]

            shape.form = form
            shape.points = shape.conformations[shape.form]
        
        if shape.name == "J":
            shape.centre = centre
            shape.conformations = [[shape.centre, [shape.centre[0]+1, shape.centre[1]], [shape.centre[0]+2, shape.centre[1]], [shape.centre[0], shape.centre[1]-1]],
                                  [shape.centre, [shape.centre[0], shape.centre[1]+1], [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]-2, shape.centre[1]]],
                                  [shape.centre, [shape.centre[0]-1, shape.centre[1]], [shape.centre[0], shape.centre[1]-1], [shape.centre[0], shape.centre[1]-2]],
                                  [shape.centre, [shape.centre[0]-1, shape.centre[1]], [shape.centre[0]-2, shape.centre[1]], [shape.centre[0], shape.centre[1]+1]]]

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
        move("left")
        set_new_Z()
            
    if direction == "right":

        check_move('right')
        move("right")
        set_new_Z()
    
    if direction == "down":
        check_move("down")
        move("down")
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

        for point in current_shape.points:
            if point[1] >= 20:
                print("shape rotation bring points below window")
                pass
        
            if point[0] >= 20:
                print("shape rotation bring points out of window")
                pass
            elif point[0] <= 0:
                print("shape rotation bring points out of window")
                pass

            for points in filled_tiles:
                for coord in points:
                    if point[0]-1 == coord [0] and point[1] == points[1]:
                        print("No rotation - will turn into shape to left")
                        pass
                    if point[0]+1 == coord [0] and point[1] == points[1]:
                        print("No rotation - will turn into shape to right")
                        pass
                    if point[0] == coord [0] and point[1]-1 == points[1]:
                        print("No rotation - will turn into shape to below")
                        pass
        
        change_coords(shape = current_shape, form = current_shape.form, centre = current_shape.centre)
        set_new_Z()

def redefine(shape = current_shape):
    global filled_tiles, current_shape, choices

    past_shape = Shape(type = current_shape.name, centre = current_shape.centre, form = current_shape.form)
    
    filled_tiles.append(past_shape.points)
    filled_tile_colours.append(past_shape.colour)
    
    choice = rand.choice(choices)
    
    new_shape = Shape(type = rand.choice(choices), centre = [10,0], form = 0) #data for shape stored in current_shape
                                                                    #creates shaped at top border in initial conformation (conformation 0)
    return new_shape
 
def placement():
    global filled_tiles, current_shape
    
    can_place = True

    while can_place == True:
        change_coords(shape = current_shape, form = current_shape.form, centre = [current_shape.centre[0], current_shape.centre[1]+1])
        
        for point in current_shape.points:
            for points in filled_tiles:
                for coord in points:
                    if point[1] + 2 == coord[1] and point[0] == coord[0]:
                        can_place = False
        
        for point in current_shape.points:
            if point[1] >= 18:
                can_place = False

    set_new_Z()



def hit_bottom():
    global hit_b, current_shape, placed

    for point in current_shape.points:
        if point[1] >= 19: #hits bottom of window
            current_shape = redefine()
            #print('shape change - hit bottom of window')
            hit_b = True
            #placed = True
            return

def hit_shape():
    global current_shape, filled_tiles

    for point in current_shape.points:
        for points in filled_tiles:
            for coord in points:
                if point[1] + 1 == coord[1] and point[0] == coord[0]:
                    current_shape = redefine()
                    #placed = True
                    return
    
def check_move(direction):
    global current_shape, can_move, filled_tiles

    if direction == 'left':
        for point in current_shape.points:
            if point[0] <= 0:
                #print('shape at left boundary, cannot continue')
                can_move = False

        for point in current_shape.points:
            for points in filled_tiles:
                for coord in points:
                    if point[0] - 1 == coord[0] and point[1]== coord[1]:
                        can_move = False

    if direction == 'right':
        for point in current_shape.points:
            if point[0] >= 19:
                #print('shape at right boundary, cannot continue')
                can_move = False

        for point in current_shape.points:
            for points in filled_tiles:
                for coord in points:
                    if point[0] + 1 == coord[0] and point[1] == coord[1]:
                        can_move = False

    if direction == "down":
        for point in current_shape.points:
            if point[1] >= 19:
                can_move = False     

        for point in current_shape.points:
            for points in filled_tiles:
                for coord in points:
                    if point[1] + 1 == coord[1] and point[0] == coord[0]:
                        can_move = False  

def move(direction):
    global can_move, current_shape

    if direction == "left":
        if can_move == True:
            change_coords(shape = current_shape, form = current_shape.form, centre = [current_shape.centre[0]-1, current_shape.centre[1]])
        elif can_move == False:
            pass

    if direction == "right":
        if can_move == True:
            change_coords(shape = current_shape, form = current_shape.form, centre = [current_shape.centre[0]+1, current_shape.centre[1]])
        elif can_move == False:
            pass

    if direction == "down":
        if can_move == True:
            change_coords(shape = current_shape, form = current_shape.form, centre = [current_shape.centre[0], current_shape.centre[1]+2])
            #print("movement down")
        elif can_move == False:
            pass



def keypress(event):
    global can_move, current_shape

    if event.key == u"\u0020": #reference to space-key in python
        placement()

    if event.key == 'down':
        #print("down button pressed")
        movement("down")
    
    if event.key == 'up':
        rotation()
    
    if event.key == 'left':
        check_move('left')
        movement(shape = current_shape, direction = "left")
        if can_move == True:
            movement(shape = current_shape, direction = "left")
        else:
            pass
   
    if event.key == 'right':
        check_move('right')
        if can_move == True:
            movement(shape = current_shape, direction = "right")
        else:
            pass



"""checks"""
def check_full_line():
    global filled_tiles, filled_tile_colours, update, coord_remove

    restart = True

    for y in range(21):
        if restart == True:
            restart = False
            remove = []
        
        for x in range(21):
            for points in filled_tiles:
                for coord in points:
                    if x == coord[0] and y == coord[1]:
                        remove.append([coord[0], coord[1]])
                        if len(remove) == 20:
                            for coord in range(20):
                                coord_remove.append(remove[coord])
                            print('line full - line break')
                            update = True
                        else:
                            restart = True

    #print("list or coords to remove: " + str(len(coord_remove)) + str(coord_remove) + "\n")
    return coord_remove

def line_break():
    global filled_tiles, update

    coord_remove = check_full_line()
    
    if update == True:
        print('coordinates to remove: ' + str(len(coord_remove)) + " " + str(coord_remove) + "\n") #- 40 coordinates
        print('filled tiles: ' + str(len(filled_tiles)) + " " + str(filled_tiles) + "\n") #- 10 sets of 4
        print('colours: ' + str(len(filled_tile_colours)) + str(filled_tile_colours)) #- 10 colours (per shape)
        
        for y in range(len(coord_remove)):  
            for x in range(len(filled_tiles)):
                
                if coord_remove[y] in filled_tiles[x]:
                    print("coord remove: " + str(coord_remove[y]) + " filled tiles: " + str(filled_tiles[x]))                    
                    list_remove = list(filled_tiles[x])
                    print("list remove: " + str(list_remove))
                    filled_tiles.remove(filled_tiles[x])

                    #filled_tile_colours.remove(filled_tile_colours[x])

                    list_remove.remove(coord_remove[y])
                    filled_tiles.append(list_remove)

                    #filled_tile_colours.append(filled_tile_colours[x])
    
        update = False
    
    set_new_Z()

def loss_check():
    global loss
    
    for points in filled_tiles:
        for coord in points:
            if coord[1] < 0:
                print(coord[1])
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
    global filled_tiles, filled_tile_colours, current_shape

    Z = [[0 for x in range(size)] for x in range(size)]
    
    for x in range(len(filled_tile_colours)):
        for coord in filled_tiles[x]:
            Z[coord[1]][coord[0]] = filled_tile_colours[x]

    for point in current_shape.points:
        Z[point[1]][point[0]] = current_shape.colour
    return Z

def run(x):

   #actions
    
    movement(shape = current_shape, direction = "constant")
    check_error("above window")
    check_error("below window")

    ax.set_xticks([])
    ax.set_yticks([])

    Z = Z_update()
    image.set_data(Z)
    
    #if placed == True:
    line_break()
    
    loss_check()



current_shape = Shape(type = rand.choice(choices) , centre = [10,0], form = 0)
#rand.choice(choices)

fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","yellowgreen","powderblue","khaki","indianred","thistle","lightpink","orange"])

fig.canvas.mpl_connect('key_press_event', keypress)

image = ax.imshow(background(), origin = 'upper', cmap=cmap)

ani = FuncAnimation(fig, run, frames = 100, interval = frame_rate, blit = False)
plt.show()