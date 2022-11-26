from carbon import Carbon
from beams import Beams
from coins import Coins
from bullets import Bullets
from input import input_to, Get
import time
import os
import sys
class Mando(Carbon):
    def __init__(self):
        Carbon.__init__(self, 20, 10, (3, 5),[['^','^','(','o',')'], 
                                             ['|','|','[','|',']'],
                                             [' ',' ','/',' ','\\']])
        self._fly_shape = [['^','^','(','o',')'], 
                           ['|','|','[','|',']'],
                           ['!','!','\\',' ','/']]
        self._money = 0
        self._lives = 12
        self._bullets = []
        self._shield = 1
        self._shield_active = False
        self._shield_time = 10
        self._shield_start = -1
        self._shield_stop = 0
        self._shield_cooldown = 20
        self._speedup = 1
        self._speedup_active = False
        self._speedup_time = 5
        self._speedup_start = -1
        self._speedup_stop = 0
        self._speedup_cooldown = 10

    def fly(self):
        self._shape = [['^','^','(','o',')'], 
                       ['|','|','[','|',']'],
                       ['!','!','\\',' ','/']]
        self._fly = 1
    def check_shield(self):
        return self._shield_active
    
    def move(self, chbuff, frame, start_time, dev):
        self.clear_old(frame)
        dev.clear_old(frame)
        old_shift = 1
        frame_shift = int((time.time() - start_time) * 10 * (1 + 0.33 * self._speedup_active))
        if(old_shift > frame_shift):
            frame_shift = old_shift
        old_shift = frame_shift
        if chbuff == 'w':
            self._fly = 1
            self._x -= int(3 * (1 + 0.33 * self._speedup_active))
            if self._x < 2:
                self._x = 2
            for k in range(2):
                for i in range(self._size[1]):
                    frame.set_cell(self._x+self._size[0]+k, self._y+i, ' ')
            self._shape = self._fly_shape
        else:
            self._shape = self._orig_shape     
        if chbuff == 'd':


            for i in range(self._size[0]):
                frame.set_cell(self._x+i, self._y, ' ')    
            self._y += int(3 * (1 + 0.33 * self._speedup_active))
            if self._y > 480: self._y = 480
        elif chbuff == 'a':


            self._y -= int(3 * (1 + 0.33 * self._speedup_active))
            for i in range(self._size[0]):
                frame.set_cell(self._x+i, self._y+self._size[1], ' ')
        elif chbuff == 'm':


            new_bul = Bullets(self._x+1, self._y+2)
            self._bullets.append(new_bul)
            # frame.spawn_bullet(new_bul)
        # chbuff = ' '
        # frame_shift = int((time.time() - start_time) * 10)
        elif chbuff == 'v' and self._shield == 1:

            self._shield = 0
            self._shield_active = True
            self._shield_start = time.time()

        elif chbuff == 'e' and self._speedup == 1:
            self._speedup = 0
            self._speedup_active = True
            self._speedup_start = time.time()

        if frame_shift > 400: frame_shift = 400
        if self._y < frame_shift + 10:
            self._y = frame_shift + 10
        self.collect_coin(frame.get_coin_list())
        self.hit_beam(frame.get_beam_list(), frame)
        if(self.hit_beam(frame.get_beam_list(), frame) == 0):
            frame.lol_ded(self, frame_shift)
        # for bul in self._bullets:
        #     frame.set_cell(bul.get_x(), bul.get_y(), ' ')
        #     frame.set_cell(bul.get_x(), bul.get_y()+1, ' ')
        #     bul.set_y(bul.get_y()+bul.get_speed())
        #     frame.spawn_bullet(bul)
        dev.follow_mando(self, frame)
        dev.shoot_mando(self, frame)
        frame.spawn_bullet(self._bullets, frame.get_beam_list(), self, dev)
        self.check_magnet(frame)
        self.update_speed(frame)
        self.update_shield(start_time)
        self.render(frame, self._shield_active)
        dev.render(frame)
        os.system('clear')
        # print("\033[2J")
        # print("\033[0;0H")
        # print(frame.print_board(frame_shift))
        frame.render_screen(self, frame_shift, start_time)


    def update_shield(self, start_time):
        if self._shield_active == True:
            self._shield_time = 10 - int((time.time() - self._shield_start) * 10) / 10
        if self._shield_cooldown > 0 and self._shield_active == False:
            self._shield_cooldown = 20 - int((time.time() - self._shield_stop) * 10) / 10
            self._shield_time = 10
        if self._shield_time <= 0:
            self._shield_active = False
            self._shield_time = 10
            self._shield_cooldown = 20
            self._shield_stop = time.time()
        if self._shield_cooldown <= 0:
            self._shield = 1
            self._shield_cooldown = 20

    def update_speed(self, start_time):
        if self._speedup_active == True:
            self._speedup_time = 5 - int((time.time() - self._speedup_start) * 10) / 10
        if self._speedup_cooldown > 0 and self._speedup_active == False:
            self._speedup_cooldown = 10 - int((time.time() - self._speedup_stop) * 10) / 10
            self._speedup_time = 5
        if self._speedup_time <= 0:
            self._speedup_active = False
            self._speedup_time = 5
            self._speedup_cooldown = 10
            self._speedup_stop = time.time()
        if self._speedup_cooldown <= 0:
            self._speedup = 1
            self._speedup_cooldown = 10

    def gravity(self, frame, start_time, dev):
        # print(self.check_ground(frame))
        ref = time.time()
        old_shift = 1
        while(self.check_ground(frame) == 0):
            self.clear_old(frame)
            dev.clear_old(frame)
            skip = int((time.time() - ref) * 10 // 3) #number of characters to travel down
            if skip > 3: 
                skip = 3
            self._x += skip
            if(self._x > 30):
                self._x = 30
            # for i in range(self._size[1]):
            #     for j in range(self._size[0]):
            #         frame.set_cell(self._x-skip+j, self._y+i, ' ')
            getch = Get()
            chbuff = input_to(getch)
            if(chbuff):
                if(chbuff == 'w'):
                    break
                else:
                    self.move(chbuff, frame, start_time, dev)
            else:
                self._shape = self._orig_shape
            # self._y += frame_shift

            frame_shift = int((time.time() - start_time) * 10 * (1 + 0.33 * self._speedup_active))
            if(frame_shift < old_shift):
                frame_shift = old_shift
            old_shift = frame_shift
            if frame_shift > 400: frame_shift = 400
            if self._y < frame_shift + 10:
                self._y = frame_shift + 10
            self.collect_coin(frame.get_coin_list())
            self.hit_beam(frame.get_beam_list(), frame)
            if(self.hit_beam(frame.get_beam_list(), frame) == 0):
                frame.lol_ded(self, frame_shift)
            # for bul in self._bullets:
            #     frame.set_cell(bul.get_x(), bul.get_y(), ' ')
            #     frame.set_cell(bul.get_x(), bul.get_y()+1, ' ')
            #     bul.set_y(bul.get_y()+bul.get_speed())
            #     frame.spawn_bullet(bul)
            dev.shoot_mando(self, frame)
            dev.follow_mando(self, frame)
            frame.spawn_bullet(self._bullets, frame.get_beam_list(), self, dev)
            self.check_magnet(frame)
            self.render(frame, self._shield_active)
            dev.render(frame)
            self.update_speed(start_time)
            self.update_shield(start_time)
            os.system('clear')
            # print("\033[35A")
            # print("\033[100D")
            # print("\033[0;0H")       
            # # print(frame.print_board(frame_shift))
            frame.render_screen(self, frame_shift, start_time)

    def collect_coin(self, coin_list):
        for coin in coin_list:
            for i in range(self._size[0]):
                for j in range(self._size[1]):
                    if coin.get_coin_x() == self._x+i and coin.get_coin_y() == self._y+j:
                        self._money += 1
                        coin_list.remove(coin)

    def hit_beam(self, beam_list, frame):
        br_flag = 0
        for beam in beam_list:
            xs = beam.get_xs()
            # print(xs, ys)
            ys = beam.get_ys()
            for le in range(beam.get_len()):
                for i in range(self._size[0]):
                    for j in range(self._size[1]):
                        # print(beam.get_len(), xs[le], ys[le])
                        if xs[le] == self._x+i and ys[le] == self._y+j:
                            if self._shield_active == False: self._lives -= 1
                            beam_list.remove(beam)
                            frame.erase_beam(beam)
                            br_flag = 1
                            break
                    if br_flag: break
                if br_flag: break
            if br_flag: break
        if(self._lives == 0):
            return 0 #lol, ded
        else:
            return 1
    
    def check_magnet(self, frame):
        self.clear_old(frame)
        for mag in frame.get_mag_list():
            if abs(self._x - mag.get_x()) <= 5 and abs(self._y - mag.get_y()) <= 5:
                if self._x - mag.get_x() > 0: 
                    self._x -= 1
                elif self._x - mag.get_x() < 0: 
                    self._x += 1
                if self._y - mag.get_y() > 0:
                    self._y -= 1
                elif self._x - mag.get_y() < 0:
                    self._y += 1 
        
    