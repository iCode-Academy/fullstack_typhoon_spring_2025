import pygame
import sys

pygame.init()

# Create window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My First Pygame Window")

# Main Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with color (R,G,B)
    screen.fill((0, 128, 255))

    pygame.display.flip()


pygame.quit()
sys.exit()
