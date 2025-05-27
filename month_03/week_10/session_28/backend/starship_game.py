import random
import pygame

# Тоглоомын тогтмол утгууд
FRAME_REFRESH_RATE = 30
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400
STARSHIP_SPEED = 5
BACKGROUND_COLOR = (0, 0, 0)  # Хар өнгө (RGB)
INITIAL_METEOR_Y_POSITION = 10
MAX_METEOR_SPEED = 5


class GameObject:
    # Энд GameObject классын кодыг бичнэ
    def load_image(self, filename):
        self.image = pygame.image.load(filename).convert()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        return pygame.display_surface.blit(self.image, (self.x, self.y))


class Starship(GameObject):
    # Энд Starship классын кодыг бичнэ
    def __init__(self, game):
        self.game = game
        self.x = DISPLAY_WIDTH / 2
        self.y = DISPLAY_HEIGHT - 40
        self.load_image('./images/starship.png')


class Meteor(GameObject):
    # Энд Meteor классын кодыг бичнэ
    def __init__(self, game):
        self.game = game
        # self.x 0-оос DISPLAY_WIDTH хүртэлх дурын утга авна
        # self.y INITIAL_METEOR_Y_POSITION 
        # self.speed  1, MAX_SPEED random утга авна
        # load_image meteor.png ийм зураг оруулж ирнэ
        self.x = random.randint(0, DISPLAY_WIDTH)
        self.y = INITIAL_METEOR_Y_POSITION
        self.speed = random.randint(1, MAX_METEOR_SPEED)
        self.load_image("./images/meteor.png")


class Game:
    # Энд Game классын кодыг бичнэ
    pass


def main():
    # Энд main функцийн кодыг бичнэ
    pass


if __name__ == "__main__":
    main()
