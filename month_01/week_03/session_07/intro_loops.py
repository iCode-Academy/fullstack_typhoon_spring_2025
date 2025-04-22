# python loops

fruits = ["алим", "банана", "гүзээлзгэнэ"]

# Problem  -- 100 ширхэг жимсний төрөлтэй list байвал яах вэ?
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Solution - Loop буюу давталт

# 1. FOR loop
for f in fruits:
    print(f)

# 0-ээс 5 хүртэл (5 орохгүй)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# 2-оос 8 хүртэл
for i in range(2, 8):
    print(i)  # 2, 3, 4, 5, 6, 7

# 1-ээс 10 хүртэл, 2 алхамаар
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9


# string буюу text
message = "Python"

# Тэмдэгт бүрээр давталт
for c in message:
    print(c)

# enumerate
fruits = ["алим", "банана", "гүзээлзгэнэ"]

# Индекс болон элементийг авах
for index, fruit in enumerate(fruits):
    print(f"Индекс {index}: {fruit}")

# Гаралт:
# Индекс 0: алим
# Индекс 1: банана
# Индекс 2: гүзээлзгэнэ

# Тодорхой индексээс эхлэх
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")  # 1. алим, 2. банана, 3. гүзээлзгэнэ

# break
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9

# break хэрэглээгүй үед else хэсэг ажиллана
for i in range(5):
    print(i)
else:
    print("Давталт амжилттай дууслаа!")

# break хэрэглэсэн үед else хэсэг ажиллахгүй
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Энэ хэсэг ажиллахгүй")

# double loop 
# Үржүүлэх хүснэгт
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("-----")

# Энгийн давталт
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# Жагсаалтын ойлголт
squares = [i ** 2 for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Нөхцөлтэй жагсаалтын ойлголт
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]