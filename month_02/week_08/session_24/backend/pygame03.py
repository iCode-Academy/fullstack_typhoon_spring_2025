import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Moving Rectangle")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Rectangle properties
rect_x = 300
rect_y = 200
rect_width = 50
rect_height = 50
rect_speed = 5

# Game clock for controlling frame rate
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keyboard input
    keys = pygame.key.get_pressed()

    # Move rectangle with arrow keys
    if keys[pygame.K_LEFT] and rect_x > 0:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT] and rect_x < 640 - rect_width:
        rect_x += rect_speed
    if keys[pygame.K_UP] and rect_y > 0:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN] and rect_y < 480 - rect_height:
        rect_y += rect_speed

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()
    clock.tick(60)  # limit to 60 frames per second

pygame.quit()
sys.exit()
