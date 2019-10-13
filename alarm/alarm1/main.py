import sendMessage
import Alarm3
import time
import pygame
import newmain
from threading import Thread

"""def countdown():
    t = 10
    while t:
        mins, secs = divmod(t, 10)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        #print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
        t -= 1
    print("You're out of time!\n")"""

def main():
    #count_thread = threading.Thread(None, countdown)
    #start = time.time()
    #x = input("Do you want option 1: whacka mole or option 2: draw gingerbreadman?")
    #if x is 1:
    flag = 0
    my_game = Alarm3.GameManager()

    flag = my_game.start()

    #if flag == -1:
        #sendMessage.sms()
    #if x is 2:

    if(newmain.main()!=1):
        sendMessage.sms()


main()
"""Thread(target = countdown().start())
Thread(target = main().start())"""
