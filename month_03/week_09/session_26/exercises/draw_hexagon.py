import pygame
import math

# Pygame тохиргоо
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (70, 130, 180)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hexagons")


def drawHexagon(x: int, y: int, size: int) -> None:
    """
    Зургаан өнцөгт зурах функц

    Args:
        x: Төвийн x координат
        y: Төвийн y координат
        size: Зургаан өнцөгтийн радиус
    """
    points = []

    # Зургаан өнцөгтийн 6 цэгийг тооцоолох (pointy-top байдлаар)
    for i in range(6):
        angle = math.pi / 3 * i  # 0 градусаас эхлэх (pointy-top)
        pointX = x + size * math.cos(angle)
        pointY = y + size * math.sin(angle)
        points.append((pointX, pointY))

    # Зургаан өнцөгт зурах
    pygame.draw.polygon(screen, BLUE, points, 2)


def main():
    """Үндсэн програм"""
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Дэлгэцийг цэвэрлэх
        screen.fill(WHITE)

        # Зургаан өнцөгтүүдийг зурах
        hexSize = 60

        # Төв цэг
        centerX = WIDTH // 2
        centerY = HEIGHT // 2

        # Эхлэлийн зургаан өнцөгт
        drawHexagon(centerX, centerY, hexSize)
        drawHexagon(centerX+40, centerY+40, hexSize)

        # Эргэн тойрны 6 зургаан өнцөгт
        # TODO

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
