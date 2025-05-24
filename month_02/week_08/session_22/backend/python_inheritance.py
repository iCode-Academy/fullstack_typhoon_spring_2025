# Animal нэртэй класс үүсгээрэй. name гэдэг class attribute-тай байна.
# speak гэдэг функцтэй байна. энэхүү функц нь юу ч хийхгүй бөгөөд үүнийг pass
#  гэж тэмдэглээрэй.
# PEP8
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


# dinosaur гэдэг animal объект үүсгэнэ үү
dinosaur = Animal("Dinosaur")
print(dinosaur.name)  # Dinosaru
dinosaur.speak()  # ?


# Problem: Dog, Cat гэдэг animal төрөлтэй классуудыг үүсгэе. Тухайн класс
# болгоныг өөрсдийнх нь дуугаар хариулдаг болгоорой.
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


# cat гэдэг классыг Meow гэдэг болгоно уу
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# 1 муур, 1 нохой object-үүдийг үүсгээд түүнийгээ speak хийлгэнэ үү.
# Creating instances
fido = Dog("Fido")
whiskers = Cat("Whiskers")

print(fido.speak())  # Fido says Woof!
print(whiskers.speak())  # Whiskers says Meow!


# Human гэдэг класс үүсгээд түүндээ хүмүүсийг боддог болгоно уу бас
# ярьдаг болгоно уу
# энэхүү функц нь заавал implement хийгдсэн байх шаардлагагүй
# Одоо түүнээс Mongolian, Chinese гэсэн 2 төрлийн race үүсгэнэ үү
# тэгээд ярьдаг болгохдоо тухайн хэлээр нь мэндчилдэг болгоорой.
class Human:
    def __init__(self, name):
        self.name = name

    def think(self):
        pass

    def talk(self):
        pass


class Mongolian(Human):
    def talk(self):
        return f"{self.name} speaks: Сайн байна уу!"

    def think(self):
        return f"Mongolian {self.name} is thinking"


class Chinese(Human):
    def talk(self):
        return f"{self.name} speaks: Ni Hao Ma!"

    def think(self):
        return f"Chinese  Man {self.name} is thinking"


khangai = Mongolian("Khangai")
print(khangai.talk())
