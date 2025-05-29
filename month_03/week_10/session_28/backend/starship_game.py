import random
import pygame

# Тоглоомын тогтмол утгууд
FRAME_REFRESH_RATE = 30
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400
STARSHIP_SPEED = 30
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
        return self.game.display_surface.blit(self.image, (self.x, self.y))


class Starship(GameObject):
    # Энд Starship классын кодыг бичнэ
    def __init__(self, game):
        self.game = game
        self.x = DISPLAY_WIDTH / 2
        self.y = DISPLAY_HEIGHT - 40
        self.load_image("./images/starship.png")

    def move_right(self):
        self.x = self.x + STARSHIP_SPEED
        if self.x + self.width > DISPLAY_WIDTH:
            self.x = DISPLAY_WIDTH - self.width

    def move_left(self):
        self.x = self.x - STARSHIP_SPEED
        if self.x < 0:
            self.x = 0

    def move_up(self):
        self.y = self.y - STARSHIP_SPEED
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.y = self.y + STARSHIP_SPEED
        if self.y + self.height > DISPLAY_HEIGHT:
            self.y = DISPLAY_HEIGHT - self.height

    def __str__(self):
        return f"Starship at ({self.x}, {self.y})"


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

    def move_down(self):
        self.y = self.y + self.speed
        if self.y > DISPLAY_HEIGHT:
            self.y = 5


class Game:
    def __init__(self):
        print("Initializing game")
        pygame.init()
        self.display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption("Starship Game")
        self.clock = pygame.time.Clock()
        self.startship = Starship(self)
        self.meteors = [Meteor(self) for _ in range(5)]

    def play(self):
        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        is_running = False
                    elif event.key == pygame.K_LEFT:
                        self.startship.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.startship.move_right()
                    elif event.key == pygame.K_UP:
                        self.startship.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.startship.move_down()
            self.display_surface.fill(BACKGROUND_COLOR)
            self.startship.draw()
            for meteor in self.meteors:
                meteor.move_down()
                meteor.draw()
            pygame.display.update()
            self.clock.tick(FRAME_REFRESH_RATE)
        pygame.quit()


def main():
    # Энд main функцийн кодыг бичнэ
    print("Starting game")
    game = Game()
    game.play()
    print("Game Over")


if __name__ == "__main__":
    main()
