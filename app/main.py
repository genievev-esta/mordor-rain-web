"""import asyncio, pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

async def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (400, 300), 30)
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())
"""
import pygame
import sys
import os

os.environ["SDL_AUDIODRIVER"] = "dummy" #TEMP: for audio driver warn

SCREEN_WIDTH=720
SCREEN_HEIGHT=1280

pygame.init()

#create surface
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
screen.fill("#50a565")
pygame.quit()