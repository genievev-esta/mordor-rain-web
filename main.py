import pygame
import sys
import os

os.environ["SDL_AUDIODRIVER"] = "dummy" #TEMP: for audio driver warn

SCREEN_WIDTH=720
SCREEN_HEIGHT=1280

pygame.init()

#create surface
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
screen.fill("#1a1a1a")

pygame.quit()