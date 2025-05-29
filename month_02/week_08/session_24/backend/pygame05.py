# Display Text with Different Fonts
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

# colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create different fonts
default_font = pygame.font.Font(None, 36)
system_font = pygame.font.SysFont("Arial", 48)

# count the frames for animation
counter = 0
clock = pygame.time.Clock()

# Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    counter += 1
    screen.fill(WHITE)

    # Render static text
    text1 = default_font.render("Hello, Pygame!", True, GREEN)
    screen.blit(text1, (50, 50))

    # Render bigger text
    text2 = system_font.render("Сайн байна уу", True, BLUE)
    screen.blit(text2, (50, 150))

    # Render animated text (color changes)
    color_value = abs(255 - (counter % 510))
    if color_value > 255:
        color_value = 510 - color_value
    animated_color = (color_value, 0, 255 - color_value)

    text3 = default_font.render("Animated Text", True, animated_color)
    screen.blit(text3, (50, 250))

    # Display counter value
    counter_text = default_font.render(f"Counter: {counter}", True, RED)
    screen.blit(counter_text, (50, 350))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
