# simple collision

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Collision Example")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# first rectangle
player_rect = pygame.Rect(100, 100, 50, 50)
player_speed = 5

# second obstacle
obstacle_rect = pygame.Rect(400, 300, 80, 80)

clock = pygame.time.Clock()

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # move player with keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed
        if keys[pygame.K_UP]:
            player_rect.y -= player_speed
        if keys[pygame.K_DOWN]:
            player_rect.y += player_speed
    # keep player on screen
    player_rect.x = max(0, min(player_rect.x, 640 - player_rect.width))
    player_rect.y = max(0, min(player_rect.y, 480 - player_rect.height))

    # check for collision
    collision = player_rect.colliderect(obstacle_rect)

    # draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, obstacle_rect)

    if collision:
        player_color = GREEN
    else:
        player_color = RED
    pygame.draw.rect(screen, player_color, player_rect)

    # draw collision status
    font = pygame.font.Font(None, 36)
    text = font.render(f"Collision: {collision}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
