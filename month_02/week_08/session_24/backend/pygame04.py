# Bouncing ball
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Bouncing Ball")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Ball properties
ball_x = 100
ball_y = 100
ball_radius = 20
ball_speed_x = 4
ball_speed_y = 3

clock = pygame.time.Clock()

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for wall collisions
    if ball_x <= ball_radius or ball_x >= 640 - ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y <= ball_radius or ball_y >= 480 - ball_radius:
        ball_speed_y = -ball_speed_y
    
    # Draw everything
    screen.fill(BLACK)
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
