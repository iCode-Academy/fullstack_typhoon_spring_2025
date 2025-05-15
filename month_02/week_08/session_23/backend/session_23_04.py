import pygame
import sys

# Initialize Pygame / Pygame эхлүүлэх
pygame.init()

# Set up the display / Дэлгэц тохируулах
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Window")

# Define colors (R, G, B) / Өнгө тодорхойлох
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game loop / Тоглоомын давталт
clock = pygame.time.Clock()
running = True

while running:
    # Handle events / Үйлдлүүд боловсруулах
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen / Дэлгэц дүүргэх
    screen.fill(WHITE)

    # Draw here / Энд зурах
    pygame.draw.circle(screen, RED, (400, 300), 50)

    # Update the display / Дэлгэц шинэчлэх
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

# Quit / Гарах
pygame.quit()
sys.exit()
















