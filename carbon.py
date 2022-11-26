from board import Board
from input import input_to, Get
import os
import time
from colorama import Fore, Back, Style 
class Carbon:
    # refers to carbon based life forms
    # x: x coord of char
    # y: y coord of char
    # shape: ascii art
    # size: dimensions
    def __init__(self, x, y, size, shape):
        self._x = x
        self._y = y
        self._shape = shape
        self._orig_shape = shape
        self._size = size
        self._fly = 0
        self._fly_shape = [[]]
        self._lives = 10
    def get_position(self):
        return (self._x, self._y)
    def get_x(self):
        return self._x
    def set_x(self, x):
        self._x = x
    def get_y(self):
        return self._y
    def set_y(self, y):
        self._y = y
    def set_size(self, dim):
        self._size = dim
    def set_shape(self, shape):
        self._shape = shape

    def check_ground(self, frame):
        # print("|" + frame.get_cell(self._x+1, self._y) + "|")
        if frame.get_cell(self._x+self._size[0], self._y) != Fore.GREEN + 'T':
            return 0
        else:
            return 1

    def clear_old(self, frame):
        try:
            for i in range(self._size[0]):
                for j in range(self._size[1]):
                    frame.set_cell(self._x+i, self._y+j, ' ')
        except IndexError:
            print(str(i) + ' ' +str(j))
    def render(self, frame, shield=False):
        if shield == False:
            color = Fore.RED
        else:
            color = Fore.CYAN
        """Places character on screen"""
        try:
            for i in range(self._size[0]):
                for j in range(self._size[1]):
                    frame.set_cell(self._x+i, self._y+j, self._shape[i][j], color)
        except IndexError:
            print(str(i) + ' ' +str(j))
        print(Style.RESET_ALL, end="")

    def hurt(self):
        self._lives -= 1
        if self._lives > 0:
            return 0
        else:
            return 1