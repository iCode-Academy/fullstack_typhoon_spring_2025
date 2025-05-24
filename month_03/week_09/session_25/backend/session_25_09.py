# sound effect
import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Sound Example")

pygame.mixer.init()

try:
    sound_file = os.path.join("sounds", "beep.wav")
    beep_sound = pygame.mixer.Sound(sound_file)
except Exception:
    print(
        "Warning: Sound file not found. Make sure to create a "
        "'sounds' folder and "
        "add a 'beep.wav' file, or change the path to your sound file."
    )
    beep_sound = None

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and beep_sound:
                beep_sound.play()

    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)
    text = font.render("Press SPACEBAR to play sound", True, BLACK)
    screen.blit(text, (120, 200))
    pygame.display.flip()
pygame.quit()
sys.exit()
