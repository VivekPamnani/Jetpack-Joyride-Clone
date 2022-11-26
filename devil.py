from carbon import Carbon
from beams import Beams
from coins import Coins
from bullets import Bullets
from input import input_to, Get
import random
import time
import os
import sys
from colorama import Fore, Back, Style 

class Devil(Carbon):
    def __init__(self, x, y):
        Carbon.__init__(self, x, y, (19,29), [[' ', ' ', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', '/', '(', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ')', '`', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', ' ', ' ', '\\', ' ', '\\', '_', '_', '_', ' ', ' ', ' ', '/', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', ' ', ' ', '/', '-', ' ', '_', ' ', ' ', '`', '-', '/', ' ', ' ', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', ' ', '(', '/', '\\', '/', ' ', '\\', ' ', '\\', ' ', ' ', ' ', '/', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', ' ', '/', ' ', '/', ' ', ' ', ' ', '|', ' ', '`', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', ' ', 'O', ' ', 'O', ' ', ' ', ' ', ')', ' ', '/', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', ' ', '`', '-', '^', '-', '-', "'", '`', '<', ' ', ' ', ' ', ' ', ' ', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', '(', '_', '.', ')', ' ', ' ', '_', ' ', ' ', ')', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', ' ', '`', '.', '_', '_', '_', '/', '`', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', ' ', ' ', ' ', '`', '-', '-', '-', '-', '-', "'", ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', ' ', ' ', ' ', '_', '_', ' ', '/', ' ', '_', '_', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', '=', '=', 'O', ')', ')', ')', '=', '=', ')', ' ', '\\', ')', ' ', '/', '=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', ' ', ' ', '`', '-', '-', "'", ' ', '`', '.', '_', '_', ',', "'", ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['<', '-', '-', '|', ' ', ' ', '_', '_', '_', '_', '_', '(', ' ', '(', '_', ' ', ' ', '/', ' ', '\\', '_', '_', '_', '_', '_', '_', '_', ' ', ' '], ['<', '-', '-', '|', ',', "'", ' ', ' ', ',', '-', '-', '-', '-', '-', "'", ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' '], ['_', '_', '/', '`', '-', '-', '{', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', ')', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '/', ' ', ' ']])
        self._lives = 20
        self._bullets = []
    def follow_mando(self, man, frame):
        if(man.get_position()[0] < self.get_position()[0]):
            self._x -= 1
        elif(man.get_position()[0] > 16 + self.get_position()[0]):
            self._x += 1
        self.clear_old(frame)
        # self.render(frame)

    #returns 1 if devil ded
    def get_bullet_list(self):
        return self._bullets

    def shoot_mando(self, man, frame, first_time=0):
        if man.get_y() >= 410:
            dev_bul = Bullets(random.randint(self._x, self._x+18), 470, ['<','='])
            self._bullets.append(dev_bul)

    def render(self, frame, shield=False):
        color = Fore.LIGHTRED_EX
        """Places character on screen"""
        try:
            for i in range(self._size[0]):
                for j in range(self._size[1]):
                    frame.set_cell(self._x+i, self._y+j, self._shape[i][j], color)
        except IndexError:
            print(str(i) + ' ' +str(j))
        print(Style.RESET_ALL, end="")