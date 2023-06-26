import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 400))

# Game loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # To prevent the error
            # pygame.error: video system not initialized
            sys.exit()

    # Draw all our elements
    # Update everything
    pygame.display.update()
