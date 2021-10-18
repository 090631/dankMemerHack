import os
import time
import random
import threading
import pyautogui as pg
from discord import utils
from pynput import keyboard
from pynput.keyboard import Key
from pynput.keyboard import Controller as  KeyboardController

current_time = time.strftime("%H:%M:%S", time.localtime())

# ///======================================================================Global Variables=================================================================================///


FLAG = True
counter = 0
first = 0
last = 0

# ///======================================================================Global Functions================================================================================///

def send(message):
    keyboard1 = KeyboardController()
    keyboard1.type(message)
    keyboard1.press(Key.enter)
    keyboard1.release(Key.enter)

    
def beg_loop():
    while FLAG:
        send('pls beg')
        send('pls dep all')
        time.sleep(random.randint(46, 50))

        
def findButton():
    color = (88, 101, 242)
    clicked = False
    s = pg.screenshot()
    
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                pg.click(x, y)
                clicked = True
                break 
        if clicked == True:
            break
            
    keyboard2 = KeyboardController()
    keyboard2.press(Key.tab)
    keyboard2.release(Key.tab)


def search_loop(counter, first, last):
    time.sleep(5)

    while FLAG:
        send('pls search')
        time.sleep(2)
        findButton()
        time.sleep(random.randint(29, 33))
        send("pls beg")
        time.sleep(1)
        send("pls dep all")


# ///======================================================================Program Start Point==============================================================================///
        

print('-'*33)
print(f'The time of starting is: {current_time}')
print('-'*33 + '\n\n')
threads = [threading.Thread(target=beg_loop), threading.Thread(target=search_loop(counter, first, last))]

for thread in threads:
    thread.start()
