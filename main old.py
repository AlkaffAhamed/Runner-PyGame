# Code before converting to OOP
import pygame
import sys
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 30))
    pygame.draw.rect(screen, "#C0E8EC", score_rect)  # Fill
    screen.blit(score_surface, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 4
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


def collisions(player, obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if obstacle_rect.colliderect(player):
                return False
    return True


def player_animation():
    # Walk Animation if player on the ground
    # Jump Animation if player is not on the ground
    global player_surface, player_index

    # Jump
    if player_rect.bottom < 300:
        player_surface = player_jump
    # Walk
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner PyGame")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0

# test_surface = pygame.Surface((100, 200))
# test_surface.fill((255, 0, 0)) # or test_surface.fill("Red")
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# Score Text inside Rectangle
# score_surface = test_font.render("Runner PyGame", False, (64, 64, 64))
# score_rect = score_surface.get_rect(center=(400, 30))

# Obstacles
# # Convert Snail Surface to Rectangle
# snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
# # snail_rect = snail_surface.get_rect(bottomright=(600, 300))
# fly_surface = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()

# Snail
snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

# Fly
fly_frame_1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []

# Player
# Animation Surfaces
player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()

player_index = 0
player_walk = [player_walk_1, player_walk_2]

# Player Surface inside the rectangle
# player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

# Intro Screen
player_stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
# player_stand = pygame.transform.scale(player_stand, (200, 400))
# player_stand = pygame.transform.scale2x(player_stand)
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render("Runner PyGame", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render("Press SPACE to run!", False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 330))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
                # snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

        # Obstacle spawning
        if game_active:
            # Spawning Snail or Fly
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(bottomright=(randint(900, 1100), 200)))
            # Snail Animation
            if event.type == snail_animation_timer:
                snail_frame_index = 1 if snail_frame_index == 0 else 0
                snail_surface = snail_frames[snail_frame_index]
            # Fly Animation
            if event.type == fly_animation_timer:
                fly_frame_index = 1 if fly_frame_index == 0 else 0
                fly_surface = fly_frames[fly_frame_index]

    # Not Game Over State
    if game_active:
        # screen.blit(test_surface, (200, 100))
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # Score Text
        # pygame.draw.rect(screen, "#C0E8EC", score_rect)  # Fill
        # # pygame.draw.rect(screen, "#C0E8EC", score_rect, 10,6)  # Border/Margins
        # screen.blit(score_surface, score_rect)
        score = display_score()

        # Snail movement
        # Important to draw the background first before drawing other objects
        # snail_rect.x -= 4
        # if snail_rect.left < 0:
        #     snail_rect.right = 800
        # screen.blit(snail_surface, snail_rect)

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

        player_animation()
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

        # Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collisions
        game_active = collisions(player_rect, obstacle_rect_list)

        # Check for Game Over State
        # if snail_rect.colliderect(player_rect):
        #     game_active = False

    # Game Over State
    else:
        # Game Over Logic
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        obstacle_rect_list = []
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    # Draw all our elements
    # Update everything
    pygame.display.update()
    # Setting max framerate to 60 fps
    clock.tick(60)
