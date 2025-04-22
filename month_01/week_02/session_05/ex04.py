# Python-д тэмдэгт мөрүүд өөрчлөгдөшгүй
s = "hello"  # unmodifiable
print(s)
# s[0] = "H"  # Энэ TypeError үүсгэнэ

# Оронд нь шинэ тэмдэгт мөр үүсгэх
s = "H" + s[1:]  # "Hello"
print(s)
# Тэмдэгт мөрийн үйлдлүүдийг ойлгох
s1 = "hello"
s2 = s1.upper()  # Шинэ тэмдэгт мөр үүсгэнэ, s1-г өөрчлөхгүй
print(s1)  # "hello" (өөрчлөгдөөгүй)
print(s2)  # "HELLO"

# Санах ойн нөлөөлөл
id_before = id(s1)
s1 = s1 + " world"  # Шинэ тэмдэгт мөрийн объект үүсгэнэ
id_after = id(s1)
print(id_before == id_after)  # False - өөр объектууд
