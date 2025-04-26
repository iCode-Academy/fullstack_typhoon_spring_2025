"""Геометрийн дүрсүүдийг агуулсан модуль."""

import math
from . import utils  # Харьцангуй импорт


class Circle:
    """Тойрог класс."""

    def __init__(self, radius, x=0, y=0):
        self.radius = radius
        self.x = x
        self.y = y

    def area(self):
        """Тойргийн талбай."""
        return math.pi * self.radius**2

    def perimeter(self):
        """Тойргийн периметр."""
        return 2 * math.pi * self.radius

    def distance_from_origin(self):
        """Тойргийн төвөөс координатын эхлэл хүртэлх зай."""
        return utils.distance(0, 0, self.x, self.y)


class Rectangle:
    """Тэгш өнцөгт класс."""

    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Тэгш өнцөгтийн талбай."""
        return self.width * self.height

    def perimeter(self):
        """Тэгш өнцөгтийн периметр."""
        return 2 * (self.width + self.height)
