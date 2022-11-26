
class Bullets:
    def __init__(self, x, y, shape=['=','>']):
        self._x = x
        self._y = y
        self._speed = 4
        self._shape = shape

    def get_x(self):
        return self._x
    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y
    def set_y(self, y):
        self._y = y

    def get_speed(self):
        return self._speed