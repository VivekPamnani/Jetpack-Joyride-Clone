import random
from coins import Coins
from beams import Beams
from magnet import Magnet
import os
import time
from colorama import Fore, Back, Style 
from tabulate import tabulate

class Board:
    def __init__(self, vertical_span, width):
        self.vertical_span = vertical_span #vertical_span: the number of vertical characters
        self.width = width
        self.init_x = 0
        self._grid = [[' ' for i in range(500)] for j in range(vertical_span)]
        self._coins = []
        self._beams = []
        self._mags = []
        self._time = 120
        #initialize grid cells here
        for i in range(500):
            self._grid[0][i] = Fore.GREEN + 'T'
            l = Fore.GREEN +'\\'
            r = Fore.GREEN +'/'
            self._grid[1][i] = r if (i%2) else l
            self._grid[vertical_span-2][i] = Fore.GREEN +'T'
            self._grid[vertical_span-1][i] = Fore.GREEN +'|'
            

    def clear_screen(self, vertical_span):
        for i in range(500):
            self._grid[0][i] = 'T'
            l = '\\'
            r = '/'
            self._grid[1][i] = r if (i%2) else l
            self._grid[vertical_span-2][i] = 'T'
            self._grid[vertical_span-1][i] = '|'

    def get_coin_list(self):
        return self._coins

    def get_beam_list(self):
        return self._beams

    def get_mag_list(self):
        return self._mags

    def get_cell(self, x, y):
        return self._grid[x][y]

    def print_board(self, x_cord): #returns a part of grid matrix as a string
        board_line = ""
        for line in self._grid:
            # board_line += ''.join(line[self._start:self._start+50]) + '\n'
            board_line += ''.join(line[x_cord:x_cord+100]) + '\n'
        #update score and coins here
        board_line += "Press Q to exit.\n"
        mag_shape = "[N|S]"
        for mag in self._mags:
            for c in range(5):
                self.set_cell(mag.get_x(), mag.get_y()+c, mag_shape[c], Fore.BLUE)
        # print(board_line)
        return board_line
    
    def set_cell(self, x, y, ch, color=Fore.WHITE):
        #to change a cell in the grid
        self._grid[x][y] = color + ch

    def rand_coins(self):
        for i in range(100):
            # coin_coord = []
            x = random.randint(2, 32)
            y = random.randint(20, 400)
            coin_sample = Coins(x, y) #creating coin objects
            self._coins.append(coin_sample)
            # screen.set_cell(coin_coord[0], coin_coord[1], '$')
            # screen.set_cell(10, 50, '$')
        for coin_sample in self._coins:
            self.set_cell(coin_sample._x, coin_sample._y, coin_sample._shape)

    def rand_beams(self):
        max_beams = random.randint(10, 30)
        for i in range(max_beams):
            # beam_coord = []
            x = random.randint(9, 25)
            y = random.randint(20, 400)
            len = random.randint(3, 6)
            # print(len)
            orientation = random.choice(["h","v","d+","d-"])
            beam_sample = Beams(x, y, len, orientation)
            self._beams.append(beam_sample)
        for beam_sample in self._beams:
            for i in range(beam_sample._size):
                self.set_cell(beam_sample._xs[i], beam_sample._ys[i], beam_sample._shape)

    def rand_mags(self):
        max_mags = 8
        for i in range(max_mags):
            x = random.randint(4, 29)
            y = random.randint(20, 400)
            mag = Magnet(x, y)
            self._mags.append(mag)
        # mag_shape = Fore.BLUE + "[N" + Fore.WHITE + "|" + Fore.BLUE + "S]" + Fore.RESET
        self.print_mags()

    def print_mags(self):
        mag_shape = "[N|S]"
        for mag in self._mags:
            for c in range(5):
                self.set_cell(mag.get_x(), mag.get_y()+c, mag_shape[c], Fore.BLUE)
    def render_screen(self, man, screen_shift, start_time):
        self._time = int((120 - time.time() + start_time) * 10) / 10
        if self._time <= 0: self.lol_ded(man, screen_shift)
        print("Lives: ", man._lives, end=" ")
        print("Score: ", man._money, end=" ")
        print("Time : ", self._time, end=" ")
        print()
        print("Shield: ", "Available" if man._shield else "Charging", end="")
        print("\nSpeedup: ", "Available" if man._speedup else "Charging", end=" ")
        # print(tabulate([["Shield: " + "Available" if man._shield else "Charging", "Speedup: " + "Available" if man._speedup else "Charging"]]))
        # print("Shield Active: ", man._shield_active, end=" ")
        print()
        if man._shield_active == True: print("\nShield Time: ", man._shield_time, end=" ")
        else: print("\nShield Cooldown: ", man._shield_cooldown, end=" ")
        if man._speedup_active == True: print("\nSpeedup Time: ", man._speedup_time, end=" ")
        else: print("\nSpeedup Cooldown: ", man._speedup_cooldown, end=" ")
        print()
        print(self.print_board(screen_shift))

    def anti_bullet(self, bullet_list, man):
        for bullet in bullet_list:
            self.set_cell(bullet.get_x(), bullet.get_y(), ' ')
            self.set_cell(bullet.get_x(), bullet.get_y()+1, ' ')
            bullet.set_y(bullet.get_y()-bullet.get_speed())
            if(bullet.get_y() > 400):
                self.set_cell(bullet.get_x(), bullet.get_y(), '<')
                self.set_cell(bullet.get_x(), bullet.get_y()+1, '<')
            else:
                self.set_cell(bullet.get_x(), bullet.get_y(), ' ')
                self.set_cell(bullet.get_x(), bullet.get_y()+1, ' ')
                bullet_list.remove(bullet)

            for bullet in bullet_list:
                if self.mando_bullet(bullet, man):
                    bullet_list.remove(bullet)

    def mando_bullet(self, bullet, man, shift=400):
        if bullet.get_x() >= man.get_x() and bullet.get_x() <= man.get_x()+2 and bullet.get_y() <= man.get_y()+4 and bullet.get_y() >= man.get_y():
            self.set_cell(bullet.get_x(), bullet.get_y(), ' ')
            self.set_cell(bullet.get_x(), bullet.get_y()+1, ' ')
            if not man.check_shield():
                if man.hurt():
                    self.lol_ded(man, shift)
            return 1
        return 0

    def spawn_bullet(self, bullet_list, beam_list, man, dev):
        for bullet in bullet_list:
            self.set_cell(bullet.get_x(), bullet.get_y(), ' ')
            self.set_cell(bullet.get_x(), bullet.get_y()+1, ' ')
            bullet.set_y(bullet.get_y()+bullet.get_speed())
            if(bullet.get_y() > 490): bullet.set_y(490)
            if(bullet.get_y() < 499):
                self.set_cell(bullet.get_x(), bullet.get_y(), '=')
                self.set_cell(bullet.get_x(), bullet.get_y()+1, '>')
            else:
                self.set_cell(bullet.get_x(), bullet.get_y(), ' ')
                self.set_cell(bullet.get_x(), bullet.get_y()+1, ' ')
                bullet_list.remove(bullet)
        
        self.anti_bullet(dev.get_bullet_list(), man)
        # for bullet in bullet_list:
        #     br_flag = 0
        #     for beam in beam_list:
        #         xs = beam.get_xs()
        #         ys = beam.get_ys()
        #         for le in range(beam.get_len()):
        #             if bullet.get_x() == xs[le]:
        #                 if bullet.get_y() == ys[le] or bullet.get_y()+1 == ys[le]:
        #                     for i in range(1):
        #                         self.set_cell(bullet.get_x(), bullet.get_y()+i, ' ')
        #                         self.set_cell(bullet.get_x(), bullet.get_y()+1, ' ')
        #                         bullet_list.remove(bullet)
        #                         self._beams.remove(beam)
        #                         self.erase_beam(beam)
        #                         br_flag = 1
        #                         break
        #                 if br_flag: break
        #             if br_flag: break
        #         if br_flag: break
        #     if br_flag: break
        for bullet in bullet_list:
            if self.beam_bullet(bullet, beam_list):
                bullet_list.remove(bullet)
            if self.devil_bullet(bullet, dev):
                bullet_list.remove(bullet)
            # self.beam_bullet(bullet, beam_list)

    def devil_bullet(self, bullet, dev):
        if bullet.get_y() >= 470 and bullet.get_x() >= dev.get_x() and bullet.get_x() < dev.get_x() + 19:
            self.set_cell(bullet.get_x(), bullet.get_y(), ' ')
            self.set_cell(bullet.get_x(), bullet.get_y()+1, ' ')
            if dev.hurt():
                self.noice_win()
            return 1
        return 0

    def noice_win(self):
        os.system('clear')
        for i in range(17):
            print()
        for i in range(45):
            print("", end=' ')
        print("YOU WON!")
        for i in range(18):
            print()
        exit()

    def beam_bullet(self, bullet, beam_list):
        br_flag = 0
        for beam in beam_list:
            xs = beam.get_xs()
            ys = beam.get_ys()
            # print(xs, ys)
            for le in range(beam.get_len()):
                for i in range(4):
                    if xs[le] == bullet.get_x() and ys[le] == bullet.get_y()+i:
                        self.set_cell(bullet.get_x(), bullet.get_y(), ' ')
                        self.set_cell(bullet.get_x(), bullet.get_y()+1, ' ')
                        beam_list.remove(beam)
                        self.erase_beam(beam)
                        br_flag = 1
                        break
                if br_flag: break
            if br_flag: break
        return br_flag

    def erase_beam(self, beam):
        xs = beam.get_xs()
        ys = beam.get_ys()
        for i in range(beam.get_len()):
            self.set_cell(xs[i], ys[i], ' ')
    
    def lol_ded(self, man, shift):
        os.system('clear')
        # print(Fore.RESET + " ", end="")
        #erasing legs
        man.render(self, man.check_shield())
        for j in range(3):
            self.set_cell(man.get_x()+2, man.get_y()+2+j, ' ')
        self.render_screen(man, shift, time.time())
        time.sleep(0.4)
        os.system('clear')
        # erasing torso
        man.render(self, man.check_shield())
        for j in range(3):
            self.set_cell(man.get_x()+2, man.get_y()+2+j, ' ')
            self.set_cell(man.get_x()+1, man.get_y()+2+j, ' ')
        self.render_screen(man, shift, time.time())
        time.sleep(0.4)
        os.system('clear')
        for j in range(3):
            self.set_cell(man.get_x()+2, man.get_y()+2+j, ' ')
            self.set_cell(man.get_x()+1, man.get_y()+2+j, ' ')
            self.set_cell(man.get_x(), man.get_y()+2+j, ' ')
        self.render_screen(man, shift, time.time())
        time.sleep(0.5)
        os.system('clear')
        man.set_shape([['^','^'], 
                       ['|','|'],
                       ['!','!']])
        man.set_size((3,2))
        while(man.check_ground(self) == 0):
            man.clear_old(self)
            man.set_x(man.get_x()+1)
            man.render(self, man.check_shield)
            self.render_screen(man, shift, time.time())
        # man.set_x(man.get_x())
            time.sleep(0.05)
            os.system('clear')
        for i in range(17):
            print()
        for i in range(45):
            print("", end=' ')
        print("YOU DIED!")
        for i in range(18):
            print()
        exit()
# bo = Board(35, 80)
# bo.print_board(0)
