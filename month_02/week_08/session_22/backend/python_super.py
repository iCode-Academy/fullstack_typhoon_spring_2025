class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name} is {self.age} years old"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent's __init__
        self.breed = breed

    def info(self):
        # Extend the parent's info method
        basic_info = super().info()
        return f"{basic_info} and is a {self.breed}"


rex = Dog("Rex", 3, "German Shepherd")
print(rex.info())  # Rex is 3 years old and is a German Shepherd
print(isinstance(rex, Dog))  # True
print(isinstance(rex, Animal))  # True
print(issubclass(Dog, Animal))  # True


# Exercise
class Shape:
    def area(self):
        pass  # Abstract method

    def perimeter(self):
        pass  # Abstract method


# Rectangle гэдэг класс үүсгээд түүнийг Shape class-аас удамшдаг болгоорой.
# Гэхдээ энэхүү класс нь заавал height, width авах ёстой
# одоо түүнийгээ тэгш өнцөгтийн талбай болон периметрийг олоод буцаадаг
# болгоорой нэг нэгш өнцөгт үүсгэж тестлэнэ үү


# Circle гэдэг класс үүсгээд түүнийг Shape class-аас удамшдаг болгоорой.
# Гэхдээ энэхүү класс нь заавал radius авах ёстой
# одоо түүнийгээ тойргийн талбай болон периметрийг олоод буцаадаг
# болгоорой нэг дугуй дүрс үүсгэж тестлэнэ үү. math санг import хийж
# оруулж ашиглаарай.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rectangle = Rectangle(5, 6)
print(rectangle.area())
print(rectangle.perimeter())


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math

        return math.pi * self.radius**2

    def perimeter(self):
        import math

        return 2 * math.pi * self.radius


circle = Circle(5)
print(circle.area())
print(circle.perimeter())
