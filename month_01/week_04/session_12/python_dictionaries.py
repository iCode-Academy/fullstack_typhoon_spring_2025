# Хоосон толь бичиг
empty_dict = {}
empty_dict = dict()

# Анхны утгатай толь бичиг (key, value)
student = {"нэр": "Бат", "нас": 20, "хот": "Улаанбаатар"}

# Олон төрлийн өгөгдөл агуулсан толь бичиг
mixed_dict = {
    "тоо": 42,
    "үсэг": "a",
    "жагсаалт": [1, 2, 3],
    "кортеж": (4, 5, 6),
    "логик": True,
    "дэд_толь": {"x": 1, "y": 2},
}

# dict() функцээр толь бичиг үүсгэх
person = dict(нэр="Болд", нас=25, хот="Дархан")

# Түлхүүр-утга хослолоос толь бичиг үүсгэх
items = [("алим", 3), ("банана", 5), ("жүрж", 2)]
fruit_count = dict(items)

# Толь бичгийн элементэд хандах
student = {"нэр": "Бат", "нас": 20, "хот": "Улаанбаатар"}

# Түлхүүрээр хандах
name = student["нэр"]  # "Бат"

# get() аргыг ашиглах (түлхүүр байхгүй бол алдаа заахгүй)
age = student.get("нас")  # 20
email = student.get("имэйл")  # None (түлхүүр байхгүй)
email = student.get("имэйл", "Мэдээлэл байхгүй")  # "Мэдээлэл байхгүй"

# Толь бичгийн элементийг өөрчлөх
student = {"нэр": "Бат", "нас": 20, "хот": "Улаанбаатар"}

# Элемент өөрчлөх
student["нас"] = 21

# Шинэ элемент нэмэх
student["мэргэжил"] = "Програмист"

# Олон элемент нэмэх/өөрчлөх
student.update({"нас": 22, "утас": "99112233", "хот": "Дархан"})

print(student)
# {'нэр': 'Бат', 'нас': 22, 'хот': 'Дархан', 'мэргэжил':
# 'Програмист', 'утас': '99112233'}

# Толь бичгийн элементийг устгах
student = {"нэр": "Бат", "нас": 20, "хот": "Улаанбаатар", "мэргэжил": "Програмист"}

# pop() аргаар устгах - устгасан элементийн утгыг буцаана
age = student.pop("нас")  # age = 20

# popitem() аргаар сүүлийн элементийг устгах
last_item = student.popitem()  # last_item = ('мэргэжил', 'Програмист')

# del түлхүүр үгээр устгах
del student["хот"]

# Бүх элементийг устгах
student.clear()  # {}

student = {"нэр": "Бат", "нас": 20, "хот": "Улаанбаатар"}

# Бүх түлхүүрийг авах
keys = student.keys()  # dict_keys(['нэр', 'нас', 'хот'])

# Бүх утгыг авах
values = student.values()  # dict_values(['Бат', 20, 'Улаанбаатар'])

# Бүх түлхүүр-утга хослолыг авах
items = (
    student.items()
)  # dict_items([('нэр', 'Бат'), ('нас', 20), ('хот', 'Улаанбаатар')])

# Жагсаалт болгох
keys_list = list(student.keys())  # ['нэр', 'нас', 'хот']

# Түлхүүр шалгах
student = {"нэр": "Бат", "нас": 20, "хот": "Улаанбаатар"}

# in операторыг ашиглах
has_name = "нэр" in student  # True
has_email = "имэйл" in student  # False

# Түлхүүр байхгүй бол анхны утга оноох
email = student.setdefault("имэйл", "bat@example.com")  # "bat@example.com"
print(
    student
)  # {'нэр': 'Бат', 'нас': 20, 'хот': 'Улаанбаатар', 'имэйл': 'bat@example.com'}

# Толь бичгийг давтах
student = {"нэр": "Бат", "нас": 20, "хот": "Улаанбаатар"}

# Түлхүүрээр давтах
for key in student:
    print(f"{key}: {student[key]}")

# Түлхүүр, утгаар давтах
for key, value in student.items():
    print(f"{key}: {value}")

# Зөвхөн түлхүүрээр давтах
for key in student.keys():
    print(key)

# Зөвхөн утгаар давтах
for value in student.values():
    print(value)

# Толь бичгийг хуулах
original = {"a": 1, "b": 2, "c": {"x": 10, "y": 20}}

# Гүехэн хуулбар (shallow copy)
copy1 = original.copy()
copy2 = dict(original)

# Гүн хуулбар (deep copy)
import copy

deep_copy = copy.deepcopy(original)

# Гүехэн хуулбарт анхаарах зүйл
original["c"]["x"] = 100
print(copy1["c"]["x"])  # 100 - Дотоод толь бичиг өөрчлөгдсөн!
print(deep_copy["c"]["x"])  # 10 - Дотоод толь бичиг өөрчлөгдөөгүй

# Толь бичгийг эрэмбэлэх
# Түлхүүрээр эрэмбэлэх
student = {"нэр": "Бат", "нас": 20, "хот": "Улаанбаатар"}

sorted_keys = sorted(student.keys())
sorted_dict = {k: student[k] for k in sorted_keys}
print(sorted_dict)  # {'нас': 20, 'нэр': 'Бат', 'хот': 'Улаанбаатар'}

# Толь бичгийн ойлголт (Dictionary Comprehension)
# Тоо болон тооны квадратыг агуулсан толь бичиг
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Нөхцөлтэй толь бичгийн ойлголт
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Өгөгдсөн жагсаалтаас толь бичиг үүсгэх
names = ["Бат", "Болд", "Сараа", "Туяа"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Бат': 3, 'Болд': 4, 'Сараа': 5, 'Туяа': 4}

# Сурагчдын мэдээлэл агуулсан давхар толь бичиг
students = {
    "s001": {
        "нэр": "Бат",
        "нас": 20,
        "хичээлүүд": ["Математик", "Физик", "Програмчлал"],
    },
    "s002": {
        "нэр": "Болд",
        "нас": 21,
        "хичээлүүд": ["Англи хэл", "Програмчлал", "Дизайн"],
    },
}

# Давхар толь бичгийн элементэд хандах
print(students["s001"]["нэр"])  # "Бат"
print(students["s002"]["хичээлүүд"][0])  # "Англи хэл"

# Давхар толь бичгийг давтах
for student_id, info in students.items():
    print(f"Сурагчийн ID: {student_id}")
    print(f"Нэр: {info['нэр']}")
    print(f"Нас: {info['нас']}")
    print(f"Хичээлүүд: {', '.join(info['хичээлүүд'])}")
    print()

# Exercise 01
# Үгсийн давтамжийг тоолох
text = "би чамд хайртай би чамд хайртай гэдгээ хэлмээр байна"
words = text.split()
print(words)
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
# {'би': 2, 'чамд': 2, 'хайртай': 2, 'гэдгээ': 1, 'хэлмээр': 1, 'байна': 1}

# Exercise 02
# Сурагчдыг насаар нь бүлэглэх
students = [
    {"нэр": "Бат", "нас": 20},
    {"нэр": "Болд", "нас": 21},
    {"нэр": "Сараа", "нас": 20},
    {"нэр": "Туяа", "нас": 21},
]

students_by_age = {}
for student in students:
    age = student["нас"]
    if age in students_by_age:
        students_by_age[age].append(student["нэр"])
    else:
        students_by_age[age] = [student["нэр"]]


print(students_by_age)
# {20: ['Бат', 'Сараа'], 21: ['Болд', 'Туяа']}


# Exercise 03
def word_frequency(text):
    # Текстийг цэвэрлэх
    text = text.lower()
    # Тэмдэгтүүдийг арилгах
    for char in '.,?!;:()[]{}""' "":
        text = text.replace(char, "")

    # Үгсийг задлах
    words = text.split()

    # Үгсийн давтамжийг тооцоолох
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


text = "Би Python хэл сурч байна. Python бол маш сонирхолтой хэл. Би Python-г сайн сурах хэрэгтэй."
freq = word_frequency(text)
print(freq)
# {'би': 2, 'python': 3, 'хэл': 2, 'сурч': 1, 'байна': 1, 'бол': 1,
#  'маш': 1, 'сонирхолтой': 1, 'pythonг': 1, 'сайн': 1, 'сурах': 1, 'хэрэгтэй': 1}
