from colorama import Fore, Back, Style 
class Coins:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._shape = Fore.YELLOW + '$'

    def get_coin_x(self):
        return self._x
    def get_coin_y(self):
        return self._y
