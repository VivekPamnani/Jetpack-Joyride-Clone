from colorama import Fore, Back, Style 
# from board import Board
class Beams:
    def __init__(self, start_x, start_y, len, orient):
        self._startx = start_x
        self._starty = start_y
        self._xs = []
        self._ys = []
        self._size = len
        self._orient = orient
        self._shape = []
        for i in range(len):
            if self._orient == "h":
                self._xs.append(self._startx)
                self._ys.append(self._starty+i)
                self._shape = Fore.LIGHTMAGENTA_EX + "_"
            elif self._orient == "v":
                self._xs.append(self._startx+i)
                self._ys.append(self._starty)
                self._shape = Fore.LIGHTMAGENTA_EX + "|"
            elif self._orient == "d+":
                self._xs.append(self._startx-i)
                self._ys.append(self._starty+i)
                self._shape = Fore.LIGHTMAGENTA_EX + "/"
            elif self._orient == "d-":
                self._xs.append(self._startx+i)
                self._ys.append(self._starty+i)
                self._shape = Fore.LIGHTMAGENTA_EX + "\\"
    
    def get_xs(self):
        return self._xs

    def get_ys(self):
        return self._ys

    def get_len(self):
        return self._size

    def debug_print(self):
        print(self._size)
        print("lol")
        for le in range(self._size):
            print(self._xs[le], self._ys[le])
    # def draw_beam(self, frame):
    #     for i in range(self._size):
    #         if self._orient == "h":
    #             frame.set_cell(self._xs[i], self._ys[i], '_')
    #         elif self._orient == "v":
    #             frame.set_cell(self._xs[i], self._ys[i], '|')
    #         elif self._orient == "d+":
    #             frame.set_cell(self._xs[i], self._ys[i], '/')
    #         elif self._orient == "d-":
    #             frame.set_cell(self._xs[i], self._ys[i], '\\')

    