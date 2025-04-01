# math library
# sin(30) =>
import math

# 4 -ийн язгуур
yazguur = math.sqrt(4)
print(yazguur)  # 2

# 99-ийн язгуурыг хувьсагчид оноогоод хэвлэж харуулна уу
yazguur = math.sqrt(99)
print(yazguur)

# floor

a = 6
b = 7

result = a / b
print(f"Result is : {result}")
print(f"Result is with Floor: {math.floor(result)}")
print(f"Result is with Ceil: {math.ceil(result)}")

# 4.56867 - ceil болон floor-ийг олоод дээрх шиг хэвлэнэ үү
result = 4.56867
print(f"Result is : {result}")
print(f"Result is with Floor: {math.floor(result)}")
print(f"Result is with Ceil: {math.ceil(result)}")
