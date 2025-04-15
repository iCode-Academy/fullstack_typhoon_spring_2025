# Python strings

single_quotes = "This is single quotation text"
double_quotes = "This is double quotation text"
multi_line_string = """
        Multi Line String
        Text
    """

# special characters
special_chars = "New Line: \n\tTabulator"
print(special_chars)

# raw string
special_chars = r"New Line: \n\tTabulator"
print(special_chars)

text = "Монгол"
# Индексээр хандах
print(text[0])  # М
print(text[-1])  # л
# Хэсэгчлэх
print(text[0:3])  # Мон
print(text[:3])  # Мон
print(text[3:])  # гол
print(text[::-1])  # логноМ

text = "Монгол улс"
# Урт
print(len(text))  # 10
# Том, жижиг үсэг
print(text.upper())  # МОНГОЛ УЛС
print(text.lower())  # монгол улс
print(text.capitalize())  # Монгол улс
print(text.title())  # Монгол Улс
# Хайх
print(text.find("гол"))  # 3
print(text.find("орос"))  # -1 (олдоогүй)
print("гол" in text)  # True
print(text.count("о"))  # 2

# Орлуулах
print(text.replace("улс", "хэл"))  # Монгол хэл
# Тэмдэгт мөрийг хуваах
words = text.split(" ")
print(words)  # ["Монгол", "улс"]
# Тэмдэгт мөрүүдийг нэгтгэх
joined = ", ".join(words)
print(joined)  # Монгол, улс

# Эхлэл, төгсгөл шалгах
print(text.startswith("Мон"))  # True
print(text.endswith("улс"))  # True
# Хоосон зай арилгах
padded = " Монгол "
print(padded.strip())  # "Монгол"
print(padded.lstrip())  # "Монгол "
print(padded.rstrip())  # " Монгол"
# Тэмдэгт мөрийн бүтцийг шалгах
print("123".isdigit())  # True
print("abc".isalpha())  # True
print("abc123".isalnum())  # True
print(" ".isspace())  # True

# % оператор ашиглах (хуучин арга)
name = "Бат"
age = 25
print("Сайн уу, %s! Таны нас %d." % (name, age))  # Сайн уу, Бат! Таны нас 25.0
# format() арга ашиглах
print("Сайн уу, {}! Таны нас {}.".format(name, age))  # Сайн уу, Бат! Таны нас 25.
print("Сайн уу, {0}! Таны нас {1}.".format(name, age))  # Сайн уу, Бат! Таны нас 25.
print(
    "Сайн уу, {name}! Таны нас {age}.".format(name=name, age=age)
)  # Сайн уу, Бат! Таны нас 25.
# f-string ашиглах (Python 3.6+)
print(f"Сайн уу, {name}! Таны нас {age}.")  # Сайн уу, Бат! Таны нас 25.
print(f"Таны 5 жилийн дараах нас: {age + 5}")

# Тоонуудыг форматлах
pi = 3.14159
print(f"Пи тоо: {pi:.2f}")  # Пи тоо: 3.14
print(f"Хувь: {0.25:.1%}")  # Хувь: 25.0%

first = "Монгол"
last = "Улс"
# + оператор ашиглах
full = first + " " + last
print(full)  # Монгол Улс
# += оператор ашиглах
message = "Сайн уу, "
message += "Бат!"
print(message)  # Сайн уу, Бат!
# Олон тэмдэгт мөрийг нэгтгэх
words = ["Python", "хэл", "сурах", "хялбар"]
sentence = " ".join(words)
print(sentence)  # Python хэл сурах хялбар

# Тэмдэгт мөрийн ойлголт
text = "Hello, World!"
# list comprehension
vowels = [char for char in text if char.lower() in "aeiou"]
print(vowels)  # ['e', 'o', 'o']
# Тэмдэгт мөрийг хөрвүүлэх
uppercase = [char.upper() for char in text]
print(uppercase)  # ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D', '!']
