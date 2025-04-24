# exception handling

# problem

print("This line will print")
x = 10
y = 0

if x == 5:
    print("Hello")

print("Next line ")

# Division by Zero
# print(x / y)

print("Third line")

# Үндсэн бүтэц - Exception Handler
try:
    # Алдаа гарч болзошгүй код
    result = 10 / 0
except ZeroDivisionError:
    # Алдаа гарвал хийх үйлдэл
    print("Тэгээр хуваах боломжгүй!")

print("Fourth Line")

# Олон төрлийн алдааг барих
try:
    number = int(input("Тоо оруулна уу: "))
    result = 10 / number
except ValueError:
    print("Зөв тоо оруулна уу!")
except ZeroDivisionError:
    print("Тэгээр хуваах боломжгүй!")

print("Fifth Line")

# Хэд хэдэн алдааг нэг дор барих
try:
    number = int(input("Тоо оруулна уу: "))
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("Буруу оролт эсвэл тэгээр хуваах оролдлого!")

# Хэрвээ ямар алдааг бусдаас ялгаж чадахгүй бол
# Бүх алдааг барих (болгоомжтой хэрэглэх)
# file = open("nonexistent.txt", "r")

try:
    # Эрсдэлтэй код
    file = open("nonexistent.txt", "r")
except Exception as e:
    print(f"Алдаа гарлаа: {e}")

print("Sixth Line")


# Алдааны мэдээлэл авах:
try:
    x = 10 / 0
except Exception as e:
    print(f"Алдааны төрөл: {type(e).__name__}")
    print(f"Алдааны мессеж: {str(e)}")

# else блок - алдаа гараагүй үед ажиллана:
try:
    number = int(input("Тоо оруулна уу: "))
    result = 10 / number
except ValueError:
    print("Зөв тоо оруулна уу!")
except ZeroDivisionError:
    print("Тэгээр хуваах боломжгүй!")
else:
    # Алдаа гараагүй бол ажиллана
    print(f"Үр дүн: {result}")

# finally блок - алдаа гарсан эсэхээс үл хамааран ажиллана:
try:
    # Эрсдэлтэй код
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Файл олдоогүй!")
else:
    print(f"Файл нэр: {file.name}")
    print(f"Файл үндэс: {file.undest}")
finally:
    # Үл хамааран ажиллана
    if "file" in locals() and not file.closed:
        file.close()

# Алдаа дамжуулах (re-raising):
try:
    x = int("тоо биш")
except ValueError:
    print("ValueError боловсруулж байна...")
    # Алдааг дамжуулах
    # raise

# Өөр алдаа үүсгэх:
try:
    age = int(input("Насаа оруулна уу: "))
    if age < 0:
        raise ValueError("Нас сөрөг тоо байж болохгүй")
except ValueError as e:
    if "invalid literal" in str(e):
        print("Зөв тоо оруулна уу")
    else:
        print(e)

# Exception chaining:(Алдаа холбох):
try:
    # Анхны алдаа
    x = int("тоо биш")
except ValueError as e:
    # Шинэ алдаа үүсгэж, анхны алдаатай холбох
    # raise RuntimeError("Боловсруулалт амжилтгүй болсон") from e
    print(e)

# traceback модуль ашиглах:
import traceback

try:
    # Алдаа гарч болзошгүй код
    1 / 0
except Exception:
    # Дэлгэрэнгүй traceback мэдээлэл хэвлэх
    traceback.print_exc()


# Exercise divide гэдэг функц бичээд a, b гэдэг параметр авдаг болгоно уу
# энэхүү функц нь тухайн параметрүүдийг тоо эсэхийг шалгаад тоо биш бол
# ValueError алдаа өгдөг харин 0-д хуваавал ZeroDivisionError өгдөг байлгаарай.
def divide(a, b):
    try:
        int(a)
        int(b)
        result = a / b
    except ValueError:
        print("Give me correct numbers")
    except ValueError:
        print("Give me correct numbers")
    except ZeroDivisionError:
        print("Do not divide number by Zero")
    except Exception:
        print('Error occurred')
    else:
        print(result)


divide(4, 0)  # Do not divide number by Zero
divide("4", 5)  # Give me correct numbers
divide("hi", "hi")  # Give me correct numbers
