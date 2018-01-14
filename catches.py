from sense_hat import SenseHat
##Egg Drop###
##Coded by dan_aldred###

import time
import random
sense = SenseHat()
sense.clear()

global game_over
global score

game_over = False
basket_x = 7
score = 0

'''main pitch measurement'''
def basket_move(pitch, basket_x):
    sense.set_pixel(basket_x, 7, [0,0,0])
    new_x = basket_x
    if 1 < pitch <179 and basket_x != 0:
        new_x -= 1
    elif 359 > pitch >179 and basket_x != 7:
        new_x += 1
    return new_x,

"Main game setup"
def main()
    global game_over


sense.show_message ("I am working", text_colour = [255,255,0]
                    
