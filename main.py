import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner PyGame")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# test_surface = pygame.Surface((100, 200))
# test_surface.fill((255, 0, 0)) # or test_surface.fill("Red")
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("Runner PyGame", False, 'Black')

# Convert Snail Surface to Rectangle
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600, 300))

# Player Surface inside the rectangle
player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))

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

    # Snail movement
    # Important to draw the background first before drawing other objects
    snail_rect.x -= 4
    if snail_rect.left < 0:
        snail_rect.right = 800
    screen.blit(snail_surface, snail_rect)

    # Move the Player by moving the rectangle that contains the player
    player_rect.left += 2
    screen.blit(player_surface, player_rect)

    # Collision Detection with Snail
    # r1.colliderect(r2)
    # if player_rect.colliderect(snail_rect):
    #     print("COLLISION!")

    # Collision Detection with Mouse
    # r1.collidepoint((x,y))
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print("MOUSEOVER!")
        print(pygame.mouse.get_pressed())

    # Draw all our elements
    # Update everything
    pygame.display.update()
    # Setting max framerate to 60 fps
    clock.tick(60)
