import pygame
import sys

pygame.init()

# Create window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Shapes Example")

# Define colors (R, G, B)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill((255, 255, 255))

    # Draw rectangle
    pygame.draw.rect(screen, RED, (50, 50, 100, 80))

    # Draw circle
    pygame.draw.circle(screen, GREEN, (400, 100), 50)

    # Draw line
    pygame.draw.line(screen, BLUE, (100, 200), (500, 200), 5)

    # Draw polygon
    pygame.draw.polygon(
        screen, YELLOW, 
        [(300, 300), (400, 280), 
         (450, 350), (350, 400), (250, 380)]
    )

    pygame.display.flip()

pygame.quit()
sys.exit()
