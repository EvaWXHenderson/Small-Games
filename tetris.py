import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

import random as rand
import time




class Shape:

    types = {
    "O": (np.array([[0,0], [1, 0], [0, 1], [1, 1]])),

    "I": (np.array([0, 0], [0, 1], [0, 2], [0, 3]), 
         np.array([0, 0], [1, 0], [2, 0], [3, 0])),

    "T":(np.array([0, 0], [-1, 0], [1, 0], [0, 1]),
        np.array([0, 0], [0, 1], [0, -1], [-1, 0]),
        np.array([0, 0], [-1, 0], [1, 0], [0, -1]),
        np.array([0, 0], [0, 1], [0, -1], [1, 0])),

    "L": (np.array([0, 0], [1, 0], [2, 0], [0, 1]),
        np.array([0, 0] [-1, 0], [-2, 0], [0, 0]),
        np.array([0, 0] [1, 0], [0, -1], [0, -2]),
        np.array([0, 0] [0, 1], [0, 2], [-1, 0])),

    "J": (np.array([0, 0],[1, 0], [2, 0], [0, -1]),
        np.array([0, 0], [0, 1], [-1, 0], [-2, 0]),
        np.array([0, 0], [-1, 0], [0, -1], [0, -2]),
        np.array([0, 0], [-1, 0], [-2, 0], [0, +1])),

    "Z": (np.array([0, 0], [-1, 0], [1, 1], [0, 1]),
        np.array([0, 0], [0, -1], [-1, 0], [-1, 1])),

    "S": (np.array([0, 0], [1, 0], [-1, 1], [0, 1]),
        np.array([0, 0], [0, -1], [1, 0], [1, 1]))
    }
    
    def __init__(self):
        rotation = 0
        form = self.types["O"]
        location = [0, 0]
        pass

    def move(self):
        pass
    def rotate(self):
        pass
    def place(self):
        pass


class Game:
    def __init__(self):
        blocks = []
        pass
    def background(self):
        pass
    def display_update(self):
        pass
    def generate(self):
        pass
    def keypress(event):
        if event.key == u"\u0020":
            pass
        if event.key == 'down':
            pass
        if event.key == 'up':
            pass
        if event.key == 'left':
            pass
        if event.key == 'right':
            pass
    def line_break(self):
        pass
    def loss_check(self):
        pass


class Display:
    def __init__(self):
        pass
    def set_display(self):
        pass
    def run(self):
        pass


fig, ax = plt.subplots(figsize = (5,5))
cmap = ListedColormap(["white","yellowgreen","powderblue","khaki","indianred","thistle","lightpink","orange"])

fig.canvas.mpl_connect('key_press_event', keypress)

image = ax.imshow(background(), origin = 'upper', cmap=cmap)

ani = FuncAnimation(fig, run, frames = 100, interval = frame_rate, blit = False)
plt.show()