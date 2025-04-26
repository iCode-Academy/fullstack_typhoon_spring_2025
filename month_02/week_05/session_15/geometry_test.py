"""geometry пакетийг турших."""

# Пакетийг импортлох
import geometry
from geometry import shapes, utils

# Классуудыг шууд ашиглах (init.py-д импортлосон учир)
circle = geometry.Circle(5, 3, 4)
print(f"Тойргийн талбай: {circle.area():.2f}")
print(f"Тойргийн периметр: {circle.perimeter():.2f}")
print(
    f"""Тойргийн төвөөс координатын эхлэл хүртэлх зай:
      {circle.distance_from_origin():.2f}"""
)

# Тодорхой модулиас импортлох

rect = shapes.Rectangle(4, 6)
print(f"Тэгш өнцөгтийн талбай: {rect.area()}")
print(f"Тэгш өнцөгтийн периметр: {rect.perimeter()}")

# Функцийг ашиглах
dist = utils.distance(0, 0, 3, 4)
mid = utils.midpoint(0, 0, 6, 8)
print(f"Зай: {dist}")
print(f"Дунд цэг: {mid}")
