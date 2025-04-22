# Recapture
# tuple ашиглаад create_point гэдэг функц үүсгэнэ үү
# энэхүү функц нь x, y гэдэг параметрууд авдаг бөгөөд
# энэ 2 параметраар tuple буцаана


def create_point(x, y):
    return (x, y)


# calculate_distance гэдэг функц тодорхойлоод point1, point2 гэдэг
# tuple параметраар аваад картесиан продукт олдог болгоорой.
def calculate_distance(point1, point2):
    import math

    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]))


# Хэрэглээний жишээ
point_a = create_point(0, 0)
point_b = create_point(3, 4)
distance = calculate_distance(point_a, point_b)
print(f"Хоёр цэг хоорондын зай: {distance}")  # 5.0

# Python sets
# Хүснэгт хаалтаар олонлог үүсгэх
set1 = {1, 2, 3, 4, 5}

# Давтагдсан элементүүд автоматаар арилна
set2 = {1, 2, 2, 3, 4, 4, 5}
print(set2)  # {1, 2, 3, 4, 5}

# set() функцээр олонлог үүсгэх
set3 = set([1, 2, 3, 4, 5])

# Хоосон олонлог
empty_set = set()  # Хоосон хүснэгт хаалт {} нь dictionary үүсгэдэг

# Тэмдэгт мөрнөөс олонлог үүсгэх
letters = set("hello")
print(letters)  # {'h', 'e', 'l', 'o'}

# Олонлогийн үндсэн үйлдлүүд
# Олонлог үүсгэх
fruits = {"алим", "банана", "жүрж"}

# Элемент нэмэх
fruits.add("усан үзэм")
print(fruits)  # {'алим', 'банана', 'жүрж', 'усан үзэм'}

# Олон элемент нэмэх
fruits.update(["манго", "киви"])
print(fruits)  # {'алим', 'банана', 'жүрж', 'усан үзэм', 'манго', 'киви'}

# Элемент хасах
fruits.remove("банана")  # Элемент байхгүй бол алдаа заана
print(fruits)  # {'алим', 'жүрж', 'усан үзэм', 'манго', 'киви'}

fruits.discard("лийр")  # Элемент байхгүй бол алдаа заахгүй

# Сүүлийн элементийг хасах
popped = fruits.pop()  # Аль элемент хасагдах нь тодорхойгүй
print(popped)
print(fruits)

# Бүх элементийг устгах
fruits.clear()
print(fruits)  # set()


# Олонлогийн логик үйлдлүүд
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Нэгдэл (Union) - хоёр олонлогийн бүх элементүүд
print(A | B)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))  # {1, 2, 3, 4, 5, 6, 7, 8}

# Огтлолцол (Intersection) - хоёр олонлогт байгаа нийтлэг элементүүд
print(A & B)  # {4, 5}
print(A.intersection(B))  # {4, 5}

# Ялгавар (Difference) - нэг олонлогт байгаа, нөгөөд байхгүй элементүүд
print(A - B)  # {1, 2, 3}
print(A.difference(B))  # {1, 2, 3}

# Симметрик ялгавар (Symmetric Difference) - аль нэг олонлогт байгаа,
# хоёуланд байхгүй элементүүд
print(A ^ B)  # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))  # {1, 2, 3, 6, 7, 8}

# Олонлогийн шалгах үйлдлүүд
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {6, 7, 8}

# Дэд олонлог мөн эсэхийг шалгах
print(B.issubset(A))  # True - B нь A-н дэд олонлог
print(A.issuperset(B))  # True - A нь B-г агуулсан

# Огтлолцолгүй эсэхийг шалгах
print(A.isdisjoint(C))  # True - A, C хоёрт нийтлэг элемент байхгүй

# Тэнцүү эсэхийг шалгах
D = {1, 2, 3, 4, 5}
print(A == D)  # True - A, D хоёр ижил элементүүдтэй

# Олонлогийн хэрэглээ

# Давхардлыг арилгах: Жагсаалтын давхардсан элементүүдийг арилгахад
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)  # [1, 2, 3, 4, 5]

# Гишүүнчлэлийг шалгах: Элемент олонлогт байгаа эсэхийг хурдан шалгахад
fruits = {"алим", "банана", "жүрж"}
print("алим" in fruits)  # True - O(1) хугацаанд шалгана

# Математик үйлдлүүд: Нэгдэл, огтлолцол, ялгавар зэрэг үйлдлүүдэд
# Хоёр текстэд байгаа нийтлэг үсгүүдийг олох
text1 = "hello"
text2 = "world"
common_letters = set(text1) & set(text2)
print(common_letters)  # {'l', 'o'}
# Өгөгдлийг шүүх: Давтагдашгүй утгуудыг олоход
# Хоёр жагсаалтын нийтлэг элементүүдийг олох
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = list(set(list1) & set(list2))
print(common_elements)  # [4, 5]

# Frozen set үүсгэх
frozen = frozenset([1, 2, 3, 4, 5])

# Логик үйлдлүүд хийх боломжтой
A = frozenset([1, 2, 3, 4, 5])
B = frozenset([4, 5, 6, 7, 8])
print(A | B)  # frozenset({1, 2, 3, 4, 5, 6, 7, 8})

# Элемент нэмэх боломжгүй
# frozen.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'

# Dictionary түлхүүр болгон ашиглах боломжтой
data = {frozen: "Frozen set түлхүүр"}
print(data[frozen])  # "Frozen set түлхүүр"


# Exercise 01 - энэхүү функц нь өгөгдсөн текстийн үгнүүдийг тоолоод
# тэгээд хэдэн ширхэг үгнүүдийг давтагдахгүй хэрэглэгдэж байгааг
# олоод буцаана.
def count_unique_words(text):
    words = text.lower().split()
    unique_words = set(words)
    return len(unique_words)


text = "Би Python хэл сурч байна. Python бол маш сонирхолтой хэл."
print(f"Давтагдашгүй үгсийн тоо: {count_unique_words(text)}")

# Давтагдашгүй үгсийн тоо: 9
