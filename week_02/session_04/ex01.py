# python variables
name = "John"  # string
age = 25  # integer
height = 1.75  # float, double
is_student = True  # boolean

print(type(name))  # <class 'str'>
print(type(age))  # <class 'str'>
# үлдсэн хэсгийн төрлийг нь харуулж гүйцээнэ үү
print(type(height))  # <class 'float'>
print(type(is_student))  # <class 'bool'>

# Not wanted
# i = 5 
# StudentName = "John" -> student_name = "John"
# int = 5
# str = 'Hi'
# Snake_Case = 'Hi'  not equal snake_case = 'Hi'

# Олон хувьсагчид ижил утга оноох
x = y = z = 0
print(x, y, z)
# Олон хувьсагчид өөр өөр утга оноох
a, b, c = 1, 2, 3
print(a, b, c)
# Цуглуулгыг задлах
coordinates = (3, 4)
x, y = coordinates
print(x, y)  # 3 4

# Хувьсагчдыг солих
a, b = 5, 10
a, b = b, a  # Python-ы тооны утгыг солих арга
print(a, b)  # 10 5

x = 10
print(type(x))  # <class 'str'>

# Төрөл хөрвүүлэх
float_number = float(10)  # 10.0
integer = int(3.14)  # 3
string_number = str(42)  # "42"

print(type(float_number))  # <class 'float'>
print(type(integer))  # <class 'int'>
print(type(string_number))  # <class 'str'>


# Бүхэл тоо (int)
age = 25
population = 7_800_000_000  # Уншихад хялбар болгох доогуур зураас

# Бутархай тоо (float)
height = 1.75
pi = 3.14159
scientific = 2.5e6  # 2,500,000.0

# Комплекс тоо (complex)
complex_number = 3 + 4j
print(complex_number.real)  # 3.0
print(complex_number.imag)  # 4.0

# Тэмдэгт мөр үүсгэх өөр өөр аргууд
single_quotes = 'Сайн' # ''
double_quotes = "Байна"
triple_quotes = """Энэ бол
олон мөрт тэмдэгт мөр"""

# Тэмдэгт мөрийн үйлдлүүд
greeting = "Сайн"
name = "Байна"
full_greeting = greeting + ", " + name + "!"  # Залгах: "Сайн, Байна!"
repeated = "Python " * 5  # Давтах: "Python Python Python "
print(repeated)
# Тэмдэгт мөрийн индекс ба хэсэгчлэл
message = "Python Програмчлал"
first_char = message[0]  # 'P'
substring = message[7:18]  # 'Програмчлал'


# Логик утгууд
is_active = True
is_completed = False

# AND logic - 2 утга 2-уулаа үнэн үед үнэн байдаг
print(False and False)  # False
print(False and True)  # False
print(True and False)  # False
print(True and True)  # True

# OR Logic - аль нэг утга нь үнэн байвал үнэн болдог тэр тохиолдлыг
print(False or False)  # False
print(True or False)  # True
print(False or True)  # True
print(True or True)  # True

# NOT logic - тухайн boolean утгын эсрэг
print(not False)  # True
print(not True)  # False

# Логик үйлдлүүд
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Логик утга руу хөрвүүлэх илэрхийллүүд
print(10 > 5)          # True
print(10 == 5)         # False
print(bool(0))         # False
print(bool(1))         # True
print(bool(""))        # False
print(bool("Hello"))   # True


# Жагсаалт үүсгэх
fruits = ["алим", "банана", "интоор"]
mixed_list = [1, "сайн байна", 3.14, True]

# Элементүүд рүү хандах
first_fruit = fruits[0]  # "алим"
last_fruit = fruits[-1]  # "интоор"

# Жагсаалтыг өөрчлөх
fruits.append("улаан лооль")  # Төгсгөлд нэмэх
fruits.insert(1, "манго")  # Тодорхой байрлалд оруулах
fruits.remove("банана")  # Утгаар нь хасах
popped_fruit = fruits.pop()  # Сүүлийн элементийг хасаж буцаах

# Жагсаалтын хэсэгчлэл
numbers = [0, 1, 2, 3, 4, 5]
subset = numbers[1:4]  # [1, 2, 3]


# Хязгаар үүсгэх
numbers = range(5)  # 0, 1, 2, 3, 4
print(numbers)
# range(эхлэл, төгсгөл)
numbers = range(2, 7)  # 2, 3, 4, 5, 6
print(numbers)
# range(эхлэл, төгсгөл, алхам)
even_numbers = range(0, 10, 2)  # 0, 2, 4, 6, 8

# Хязгаарыг жагсаалт болгох
numbers_list = list(range(5))  # [0, 1, 2, 3, 4]
print(numbers_list)


x = 10  # Үндсэн оноолт

# Нийлмэл оноолт
x += 5   # x = x + 5 (15)
x -= 3   # x = x - 3 (12)
x *= 2   # x = x * 2 (24)
x /= 4   # x = x / 4 (6.0)
x //= 2  # x = x // 2 (3.0)
x %= 2   # x = x % 2 (1.0)
x **= 3  # x = x ** 3 (1.0)

# Олон оноолт
a, b, c = 1, 2, 3


a = 10
b = 5

equal = a == b         # False
not_equal = a != b     # True
greater_than = a > b   # True
less_than = a < b      # False
greater_equal = a >= b  # True
less_equal = a <= b    # False

# Гинжин харьцуулалт
result = 1 < 3 < 5     # True (1 < 3 and 3 < 5 гэсэнтэй адил)
result = 5 > 3 < 1     # False (5 > 3 and 3 < 1 гэсэнтэй адил)