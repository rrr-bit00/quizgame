import pygame
import numpy
import sys
from pygame.locals import *

def run():
    pygame.init()
    screen = pygame.display.set_mode((1280,960))
    #フルスクリーンの場合
    #screen = pygame.display.set_mode(SCREEN_SIZE,FULLSCREEN) 
    pygame.display.set_caption('Hello,World')

    running = True
    while running:
        screen.fill((0,0,0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__=="__main__":
    run()