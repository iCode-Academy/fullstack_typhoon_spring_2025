# Game with menu

import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Game States Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2

# Game variables
game_state = MENU
score = 0
game_time = 0
player_rect = pygame.Rect(300, 400, 40, 40)
obstacles = []
spawn_timer = 0

# Font
font = pygame.font.Font(None, 36)

# Clock
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # handle menu state menu input
        if game_state == MENU and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_state = PLAYING
                score = 0
                game_time = 0
                player_rect.x = 300
                obstacles = []

        if game_state == GAME_OVER and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_state = MENU

    screen.fill(WHITE)
    # Menu state
    if game_state == MENU:
        title = font.render("SIMPLE GAME", True, BLUE)
        screen.blit(title, (240, 180))
        instruction = font.render("Presse SPACE to start", True, BLACK)
        screen.blit(instruction, (210, 240))
    elif game_state == PLAYING:
        game_time += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.x > 0:
            player_rect.x -= 5
        if keys[pygame.K_RIGHT] and player_rect.y < 600:
            player_rect.x += 5

        spawn_timer += 1
        if spawn_timer >= 60:
            spawn_timer = 0
            obstacle = pygame.Rect(random.randint(0, 600), -50, 40, 40)
            obstacles.append(obstacle)

        # move obstacles
        for obstacle in obstacles[:]:
            obstacle.y += 5

            if obstacle.colliderect(player_rect):
                game_state = GAME_OVER

            if obstacle.y > 480:
                obstacles.remove(obstacle)
                score += 1
        # draw obstacles
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, obstacle)
        # draw player
        pygame.draw.rect(screen, BLUE, player_rect)

        # Draw score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
    elif game_state == GAME_OVER:
        title = font.render("GAME OVER", True, RED)
        screen.blit(title, (250, 180))

        score_text = font.render(f"Final Score: {score}", True, BLACK)
        screen.blit(score_text, (240, 240))
        instruction = font.render("Press SPACE to return to menu", True, BLACK)
        screen.blit(instruction, (160, 300))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
