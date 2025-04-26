"""Мэндчилгээний функцуудыг агуулсан модуль."""

# Тогтмол утга
DEFAULT_LANGUAGE = "Монгол"

# "Хувийн" хувьсагч (нэрний өмнөх доогуур зураас нь хувийн гэдгийг илэрхийлнэ)
_counter = 0


def greet(name, language=DEFAULT_LANGUAGE):
    """Хэрэглэгчид мэндчилгээ хэлэх."""
    global _counter
    _counter += 1

    if language.lower() == "монгол":
        return f"Сайн байна уу, {name}!"
    elif language.lower() == "англи":
        return f"Hello, {name}!"
    else:
        return f"Мэндчилгээ, {name}!"


def get_greeting_count():
    """Мэндчилгээ хэдэн удаа хэлснийг буцаах."""
    return _counter


# Энэ хэсэг зөвхөн файлыг шууд ажиллуулахад гүйцэтгэгдэнэ
if __name__ == "__main__":
    print("greetings.py файлыг шууд ажиллуулж байна")
    print(greet("Бат"))
    print(greet("John", "Англи"))
    print(f"Мэндчилгээ {get_greeting_count()} удаа хэлэгдсэн")
