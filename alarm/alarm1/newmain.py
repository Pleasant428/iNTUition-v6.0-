import pygame, sys
from pygame.locals import *
import time

def main():
    pygame.init()
    RED = (255 , 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255,0)

    mouse_position = (0, 0)
    drawing = False
    screen = pygame.display.set_mode((300, 532))
    screen.fill(WHITE)
    pygame.display.set_caption("ScratchBoard")
    image = pygame.image.load("phone.jpeg")
    screen.blit(image,[0,0])

    font_obj = pygame.font.Font('OpenSans.ttf', 25)

    rect1 = pygame.Rect(110,50, 20, 20)
    rect2 = pygame.Rect(200, 500, 20, 20)
    rect3 = pygame.Rect(280, 250, 20, 20)
    pygame.draw.rect(screen, RED, rect1)
    pygame.draw.rect(screen, RED, rect2)
    pygame.draw.rect(screen, RED, rect3)

    last_pos = None
    first_pos = None
    test=0
    test1=False
    test2=False
    test3=False
    pygame.mixer.music.load("vibrate.wav")
    pygame.mixer.music.play(-1)
    start = time.time()
    end = time.time()
    while (test!=1):
        if end-start>10:
            #print("too long")
            return -1
            break
        end = time.time()
        for event in pygame.event.get():


            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                drawing = False
            elif event.type == MOUSEBUTTONDOWN:
                drawing = True

                first_pos = pygame.mouse.get_pos()
            elif event.type == MOUSEMOTION:

                if (drawing):
                    mouse_position = pygame.mouse.get_pos()
                    if last_pos is not None:
                        pygame.draw.line(screen, BLACK, last_pos, mouse_position, 2)
                    last_pos = mouse_position
                    if(mouse_position[0]<=130) and (mouse_position[0]>=110):
                        if(mouse_position[1]<=70) and (mouse_position[1]>=50):
                            pygame.draw.rect(screen, GREEN, rect1)
                            test1=True
                    if(mouse_position[0]<=220) and (mouse_position[0]>=200):
                        if(mouse_position[1]<=520) and (mouse_position[1]>=500):
                            pygame.draw.rect(screen, GREEN, rect2)
                            test2=True
                    if(mouse_position[0]<=300) and (mouse_position[0]>=280):
                        if(mouse_position[1]<=270) and (mouse_position[1]>=250):
                            pygame.draw.rect(screen, GREEN, rect3)
                            test3=True
                    if(last_pos[0]<=first_pos[0]) and (last_pos[0]>=first_pos[0]):
                        if (last_pos[1]<=first_pos[1]) and (last_pos[1]>=first_pos[1]):
                            if (test1 and test2 and test3):
                                print("done")
                                image = pygame.image.load("phone.jpeg")
                                screen.blit(image,[0,0])
                                ending_string = "Successfully Snoozed!"
                                pygame.mixer.music.stop()
                                score_text = font_obj.render(ending_string, True, (255, 255, 255))
                                score_text_pos = score_text.get_rect()
                                score_text_pos.centerx = image.get_rect().centerx
                                score_text_pos.centery = 500
                                screen.blit(score_text, score_text_pos)
                                test += 1
                                print(first_pos, last_pos)
                                break
        pygame.display.update()
    return 1


#main()
