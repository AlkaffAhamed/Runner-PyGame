import pygame
import sys


def display_score():
    current_time = pygame.time.get_ticks()
    score_surface = test_font.render(f"{current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 30))
    pygame.draw.rect(screen, "#C0E8EC", score_rect)  # Fill
    screen.blit(score_surface, score_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner PyGame")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True

# test_surface = pygame.Surface((100, 200))
# test_surface.fill((255, 0, 0)) # or test_surface.fill("Red")
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# Score Text inside Rectangle
# score_surface = test_font.render("Runner PyGame", False, (64, 64, 64))
# score_rect = score_surface.get_rect(center=(400, 30))

# Convert Snail Surface to Rectangle
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600, 300))

# Player Surface inside the rectangle
player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

# Game loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # To prevent the error
            # pygame.error: video system not initialized
            sys.exit()

        # Not Game Over State
        if game_active:
            # Mouse event using event loop
            # if event.type == pygame.MOUSEMOTION:
            #     if player_rect.collidepoint(event.pos):
            #         print("MOUSEOVER - EVENT")
            # if event.type == pygame.MOUSEBUTTONUP:
            #     print("Mouse-UP")
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     print("Mouse-DOWN")

            # Keyboard event using event loop
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         print("JUMP! - EVENT")
            # if event.type == pygame.KEYUP:
            #     print("Key-UP")

            # Jump when Space is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

            # Jump when player is clicked
            if event.type == pygame.MOUSEBUTTONUP:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
        # Game Over State
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

    # Not Game Over State
    if game_active:
        # screen.blit(test_surface, (200, 100))
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # Score Text
        # pygame.draw.rect(screen, "#C0E8EC", score_rect)  # Fill
        # # pygame.draw.rect(screen, "#C0E8EC", score_rect, 10,6)  # Border/Margins
        # screen.blit(score_surface, score_rect)
        display_score()

        # Snail movement
        # Important to draw the background first before drawing other objects
        snail_rect.x -= 4
        if snail_rect.left < 0:
            snail_rect.right = 800
        screen.blit(snail_surface, snail_rect)

        # Keys using the key module
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("JUMP!")

        # Move the Player by moving the rectangle that contains the player
        # player_rect.left += 2

        # Player Gravity
        player_gravity += 1
        player_rect.y += player_gravity

        # To prevent the player from falling below ground
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surface, player_rect)

        # Collision Detection with Snail
        # r1.colliderect(r2)
        # if player_rect.colliderect(snail_rect):
        #     print("COLLISION!")

        # Collision Detection with Mouse
        # r1.collidepoint((x,y))
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print("MOUSEOVER!")
        #     print(pygame.mouse.get_pressed())

        # Check for Game Over State
        if snail_rect.colliderect(player_rect):
            game_active = False

    # Game Over State
    else:
        # Game Over Logic
        screen.fill("Yellow")

    # Draw all our elements
    # Update everything
    pygame.display.update()
    # Setting max framerate to 60 fps
    clock.tick(60)
