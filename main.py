import os
import sys
import time
from input import input_to, Get
import random
from board import Board 
from mando import Mando
from devil import Devil
from coins import Coins
from beams import Beams
from colorama import Fore, Back, Style 

screen = Board(35, 100)
man  = Mando()
dev = Devil(14, 470)

#setting up the board
beams = []

screen.rand_coins()
screen.rand_beams()
screen.rand_mags()
# devil_shape = [[]]
# with open('./devil.asc') as ascii:
#     for line in ascii:
#         devil_shape.append(line.strip('\n'))
# screen.render_screen(man, 0, time.time())
# exit()
# screen.render_screen(man, 400, 100)
# exit()
# print(screen.print_board(0))
# for coin in screen.get_coin_list():
#     print(coin.get_coin_x(), coin.get_coin_y())
# for bem in screen._beams:
#     bem.debug_print()
# exit()

print(Fore.LIGHTBLACK_EX)

if __name__ == '__main__':
    start_time = time.time()
    screen_shift = 1
    old_shift = 1
    # game_start = time.time()
    while(1):
        getch = Get()
        chbuff = input_to(getch)

        if chbuff == 'q':
            exit()
        if chbuff:
            man.move(chbuff, screen, start_time, dev)
        
        # man._y += screen_shift
        man.gravity(screen, start_time, dev)
        os.system('clear') 
        # print("\033[35A")
        # print("\033[100D")
        # print("\033[0;0H")
        if man._y < screen_shift + 10:
            man.clear_old(screen)
            dev.clear_old(screen)
            man._y = screen_shift + 10
            man.collect_coin(screen.get_coin_list())
            man.hit_beam(screen.get_beam_list(), screen)
            if(man.hit_beam(screen.get_beam_list(), screen) == 0):
                screen.lol_ded(man, screen_shift)
        # for bul in man._bullets:
        #     screen.set_cell(bul.get_x(), bul.get_y(), ' ')
        #     screen.set_cell(bul.get_x(), bul.get_y()+1, ' ')
        #     bul.set_y(bul.get_y()+bul.get_speed())
        #     screen.spawn_bullet(bul)
        dev.follow_mando(man, screen)
        dev.shoot_mando(man, screen)
        screen.spawn_bullet(man._bullets, screen.get_beam_list(), man, dev)
        man.update_shield(start_time)
        man.update_speed(start_time)
        man.check_magnet(screen)
        # man._shield_time = 10 - int((time.time() - start_time) * 10) / 10
        man.render(screen, man.check_shield())
        dev.render(screen)

        if screen_shift < old_shift:
            screen_shift = old_shift
        screen_shift = int((time.time() - start_time) * 10 * (1 + 0.33 * man._speedup_active))
        old_shift = screen_shift
        if screen_shift > 400: screen_shift = 400
        screen.render_screen(man, screen_shift, start_time)
