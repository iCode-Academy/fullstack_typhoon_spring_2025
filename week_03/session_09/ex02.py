# 1.
def profile(name, age):
    print(f"{name} нь {age} настай")


# Байрлалаар дамжуулах
profile("Болд", 25)

# Нэрээр нь дамжуулах
profile(age=25, name="Болд")


# 2. default утга
def profile(name, age=30, city="Ulaanbaatar"):
    print(f"{name} нь {age} настай, {city}-д амьдардаг")


# Функцийг дуудах
profile("Болд")  # Анхны утгуудыг ашиглана
profile("Сараа", 25)  # Насыг дарж бичнэ
profile("Баяр", city="Darhan")  # Зөвхөн хотыг дарж бичнэ


# many arguments
def sum(*numbers):
    """Дурын тооны аргументуудын нийлбэрийг олох.

    Args:
        *numbers: Хувьсах тооны аргументууд

    Returns:
        int/float: Өгөгдсөн тоонуудын нийлбэр
    """
    total = 0
    for number in numbers:
        total += number
    return total


# Функцийг дуудах
print(sum(1, 2, 3))  # Гаралт: 6
print(sum(5, 10, 15, 20))  # Гаралт: 50
