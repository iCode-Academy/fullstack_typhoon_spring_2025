import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mouse Interaction")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

circles = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if mouse click happened
        if event.type == pygame.MOUSEBUTTONDOWN:
            # left button
            if event.button == 1:
                color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
                # add a new circle where it is clicked
                circles.append(
                    {"pos": event.pos, "radius": random.randint(10, 50), "color": color}
                )
            # right button - clear circles
            if event.button == 3:
                circles = []
    screen.fill(WHITE)
    # draw all circles
    for circle in circles:
        pygame.draw.circle(screen, circle["color"], circle["pos"], circle["radius"])

    # draw instructions
    font = pygame.font.Font(None, 24)
    text = font.render("Left click: Add circle | Right click: Clear all", True, BLACK)
    screen.blit(text, (10, 10))
    pygame.display.flip()

pygame.quit()
sys.exit()
