import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner PyGame")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# test_surface = pygame.Surface((100, 200))
# test_surface.fill((255, 0, 0)) # or test_surface.fill("Red")
sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")
text_surface = test_font.render("Runner PyGame", False, 'Black')

# Game loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # To prevent the error
            # pygame.error: video system not initialized
            sys.exit()

    # screen.blit(test_surface, (200, 100))
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 30))

    # Draw all our elements
    # Update everything
    pygame.display.update()
    # Setting max framerate to 60 fps
    clock.tick(60)
