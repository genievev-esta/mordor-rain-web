import pygame

pygame.init()

# Set display mode to 800x600 pixels
screen = pygame.display.set_mode((800, 600))

# Check if the display was initialized successfully
if screen:
    print("Display initialized successfully")
else:
    print("Failed to initialize display")

# Example with flags and depth
# screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN | pygame.HWSURFACE, 32)

pygame.quit()
