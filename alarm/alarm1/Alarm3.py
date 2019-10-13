import pygame as pg
import random
import time
from threading import Timer
#from pygame import *


class GameManager:
    def __init__(self):
        # Define constants
        self.SCREEN_WIDTH = 300
        self.SCREEN_HEIGHT = 532
        self.FPS = 60
        self.BUTTON_WIDTH = 70
        self.BUTTON_HEIGHT = 70
        self.FONT_SIZE = 25
        self.FONT_TOP_MARGIN = 500
        self.LEVEL_SCORE_GAP = 4
        self.LEFT_MOUSE_BUTTON = 1
        self.GAME_TITLE = "Alarm Clock"
        #self.soundEffect = SoundEffect()
        # Initialize player's score, number of missed hits and level
        self.score = 0
        # Initialize screen
        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pg.display.set_caption(self.GAME_TITLE)
        self.background = pg.image.load("C:/Users/Sebastian/Desktop/alarm/alarm1/phone.jpeg")
        # Font object for displaying text
        self.font_obj = pg.font.Font('C:/Users/Sebastian/Desktop/alarm/alarm1/OpenSans.ttf', self.FONT_SIZE)
        # Positions of the holes in background
        self.hole_positions = []
        self.hole_positions.append((10, 30))
        self.hole_positions.append((119, 200))
        self.hole_positions.append((179, 169))
        self.hole_positions.append((104, 430))
        self.hole_positions.append((200, 366))
        self.hole_positions.append((210, 400))
        self.hole_positions.append((119, 410))
        self.hole_positions.append((95, 43))
        self.hole_positions.append((220, 50))




    # Get the new duration between the time the mole pop up and down the holes
    # It's in inverse ratio to the player's current level
    def get_interval_by_level(self, initial_interval):
        new_interval = initial_interval - 0.15
        if new_interval > 0:
            return new_interval
        else:
            return 0.05


    # Check whether the mouse click hit the mole or not
    def is_mole_hit(self, mouse_position, current_hole_position):
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]
        current_hole_x = current_hole_position[0]
        current_hole_y = current_hole_position[1]
        if (mouse_x > current_hole_x) and (mouse_x < current_hole_x + self.BUTTON_WIDTH) and (mouse_y > current_hole_y) and (mouse_y < current_hole_y + self.BUTTON_HEIGHT):
            return True
        else:
            return False

    # Update the game states, re-calculate the player's score, misses, level
    def update(self):
        # Update the player's score
        current_score_string = "Score: " + str(self.score)
        score_text = self.font_obj.render(current_score_string, True, (255, 255, 255))
        score_text_pos = score_text.get_rect()
        score_text_pos.centerx = self.background.get_rect().centerx
        score_text_pos.centery = self.FONT_TOP_MARGIN
        self.screen.blit(score_text, score_text_pos)

    def finalupdate(self):
        ending_string = "Successfully Snoozed!"
        score_text = self.font_obj.render(ending_string, True, (255, 255, 255))
        score_text_pos = score_text.get_rect()
        score_text_pos.centerx = self.background.get_rect().centerx
        score_text_pos.centery = 500
        self.screen.blit(score_text, score_text_pos)

    def out_of_time(self):
        exit()

    # Start the game's main loop
    # Contains some logic for handling animations, mole hit events, etc..
    def start(self):
        cycle_time = 0
        num = -1
        loop = True
        is_down = False
        interval = 0.1
        initial_interval = 1
        frame_num = 0
        left = 0
        timeout = 10
        start = 0
        #t = Timer(timeout, out_of_time())
        #t.start()
        #prompt = "You have %d seconds to choose the correct answer...\n" % timeout
        #answer = input(prompt)
        #t.cancel()
        # Time control variables
        clock = pg.time.Clock()
        start = time.time()
        end = time.time()


        pg.mixer.music.load("C:/Users/Sebastian/Desktop/alarm/alarm1/vibrate.wav")
        pg.mixer.music.play(-1)
        while loop:
            if end-start>10:
                #print("too long")
                return -1
                break
            end = time.time()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    loop = False
                """if event.type == MOUSEBUTTONDOWN and event.button == self.LEFT_MOUSE_BUTTON:
                    self.soundEffect.playvibrate()"""
                if self.is_mole_hit(pg.mouse.get_pos(), self.hole_positions[frame_num]) and num > 0 and left == 0:
                    num = 3
                    left = 14
                    is_down = False
                    interval = 0
                    self.score += 1  # Increase player's score
                    self.update()
            #end = timeit.timeit()
            #print("elapsed time is" , end-start)
            """if (end-start)>10:
                break
            if out_of_time is True:
                t.cancel()
                break"""
            if num > 5:
                self.screen.blit(self.background, (0, 0))
                self.update()
                num = -1
                left = 0

            if num == -1:
                self.screen.blit(self.background, (0, 0))
                self.update()
                num = 0
                is_down = False
                interval = 0.5
                frame_num = random.randint(0, 8)

            mil = clock.tick(self.FPS)
            sec = mil / 1000.0
            cycle_time += sec

            if cycle_time > interval:
                button = pg.image.load("C:/Users/Sebastian/Desktop/alarm/alarm1/Snooze.jpeg")
                self.screen.blit(self.background, (0, 0))
                self.screen.blit(button, (self.hole_positions[frame_num][0], self.hole_positions[frame_num][1]))
                self.update()
                if is_down is False:
                    num += 1
                else:
                    num -= 1
                if num == 4:
                    interval = 0.3
                elif num == 3:
                    num -= 1
                    is_down = True
                    interval = self.get_interval_by_level(initial_interval)  # get the newly decreased interval value
                else:
                    interval = 0.1
                cycle_time = 0

            if self.score == 5:
                #pygame.quit()
                #soundEffect.stopvibrate()
                pg.mixer.music.stop()
                self.screen.blit(self.background, (0, 0))
                self.finalupdate()
                loop = False
                return 1
                #break

            # Update the display
            pg.display.flip()

"""class SoundEffect:
    def __init__(self):
        self.vibrateSound = pg.mixer.music.load("C:/Users/Joey/Desktop/twil/message/vibrate.wav")
        self.vibrateSound=mixer.Sound("C:/Users/Joey/Desktop/twil/message/vibrate.wav")


        pg.mixer.music.play(-1)

    def playvibrate(self):

        self.vibrateSound.play()
    def stopvibrate(self):
        self.vibrateSound.stop()"""




###############################################################
# Initialize the game
#pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pg.init()

# Run the main loop

"""my_game = GameManager()
my_game.start()"""
# Exit the game if the main loop ends
#pygame.quit()
