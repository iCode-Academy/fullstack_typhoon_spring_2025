# intro into python list

# Problem  - Variables so many variables to define
b = 7
print(b)

# Solution - Lists
fruits = ["алим", "банана", "гүзээлзгэнэ"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "хоёр", 3.0, True]
empty_list = []

print(type(fruits))
print(fruits)

# list index
# Эерэг индекс (эхнээс нь тоолно)
print(fruits[0])  # алим
print(fruits[1])  # банана
print(fruits[2])  # гүзээлзгэнэ

# Сөрөг индекс (төгсгөлөөс нь тоолно)
print(fruits[-1])  # гүзээлзгэнэ
print(fruits[-2])  # банана
print(fruits[-3])  # алим

# Change list
# Элемент өөрчлөх
fruits[0] = "үзэм"
print(fruits)  # ['үзэм', 'банана', 'гүзээлзгэнэ']

# Элемент нэмэх
fruits.append("киви")
print(fruits)  # ['үзэм', 'банана', 'гүзээлзгэнэ', 'киви']

# Тодорхой байрлалд элемент оруулах
fruits.insert(1, "манго")
print(fruits)  # ['үзэм', 'манго', 'банана', 'гүзээлзгэнэ', 'киви']

# Элемент устгах
fruits.remove("банана")
print(fruits)  # ['үзэм', 'манго', 'гүзээлзгэнэ', 'киви']

# Индексээр элемент устгах
removed_fruit = fruits.pop(1)  # манго-г устгаж, хувьсагчид хадгална
print(removed_fruit)  # манго
print(fruits)  # ['үзэм', 'гүзээлзгэнэ', 'киви']

# Бүх элементийг устгах
fruits.clear()
print(fruits)  # []

# List methods
fruits = ["алим", "банана", "гүзээлзгэнэ"]

# Жагсаалтын урт
print(len(fruits))  # 3

# Жагсаалтыг эрэмбэлэх
fruits.sort()
print(fruits)  # ['алим', 'банана', 'гүзээлзгэнэ']

# Жагсаалтыг урвуу эрэмбэлэх
fruits.reverse()
print(fruits)  # ['гүзээлзгэнэ', 'банана', 'алим']

# Элементийн индексийг олох
print(fruits.index("банана"))  # 1

# Элементийн тоог тоолох
print(fruits.count("банана"))  # 1

# Жагсаалтыг хуулбарлах
fruits_copy = fruits.copy()
print(fruits_copy)  # ['гүзээлзгэнэ', 'банана', 'алим']

# Жагсаалтуудыг нэгтгэх
more_fruits = ["киви", "манго"]
fruits.extend(more_fruits)
print(fruits)  # ['гүзээлзгэнэ', 'банана', 'алим', 'киви', 'манго']

## List Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Эхлэл:төгсгөл
print(numbers[2:5])  # [2, 3, 4]

# Эхлэлээс төгсгөл хүртэл
print(numbers[:5])  # [0, 1, 2, 3, 4]

# Эхлэлээс жагсаалтын төгсгөл хүртэл
print(numbers[5:])  # [5, 6, 7, 8, 9]

# Алхам тодорхойлох
print(numbers[1:9:2])  # [1, 3, 5, 7]

# Жагсаалтыг хуулбарлах
numbers_copy = numbers[:]