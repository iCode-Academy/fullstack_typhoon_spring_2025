class Dog:
    """Энгийн нохой класс"""

    pass


banhar = Dog()  # object - бодит зүйл
print(banhar)
bulldog = Dog()
print(bulldog)


# __init__ гэдэг классын функц
class Cat:
    def __init__(self, name, race):  # class parameter
        self.name = name  # class attributes, class variables
        self.race = race

    # class function/method
    def meow(self):
        return f"Meow! I'm a {self.name}"

    def __str__(self):
        return f"{self.name} нь {self.race}"

    def __repr__(self):
        return f"Cat(name={self.name}, race={self.race})"


# cat гэдэг классаас 2 төрлийн object буюу 2 төрлийн муур үүсгэнэ үү.
# object oriented programming буюу объект хандалтат программчлал
koshka = Cat("Koshka", "Marine Coon")
print(koshka)
print(koshka.name)  # Koshka
print(koshka.meow())
print(repr(koshka))
cindy = Cat("Cindy", "Birman")
print(cindy)
print(cindy.name)
print(cindy.race)
# class function call
print(cindy.meow())
print(repr(cindy))


# class identities
class Horse:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


black_horse = Horse("Har Mori", 3)
print(black_horse.species)
print(black_horse.age)
print(black_horse.name)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def bark(self, sound):
        return f"{self.name} says {sound}"


#  2 бодит нохой үүсгээд функцүүдийг нь дуудаж харуулна уу.
balt = Dog(name="Balt", age=5)
hartsaga = Dog("Hartsaga", age=3)
print(balt.description())
print(balt.bark("Hov Hov"))
print(hartsaga.description())
print(hartsaga.bark("Hav Hav"))


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.__account_number = "123456"

    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value


khangai_account = BankAccount("Khangaikhuu", 1000000)
khangai_account.balance(1000)
print(khangai_account.balance)


# класс дотор буруу attribute ашиглах
class Dog:

    # tricks = []  # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")
print(d.tricks)
print(e.tricks)
