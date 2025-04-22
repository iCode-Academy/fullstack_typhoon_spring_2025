# Python Loop - FOR

# Recapture

colors = ['red', 'yellow', 'blue', 'green', 'purple']  # list
print(colors)

# print out 'blue'
print(colors[2])  # blue
print(colors[0])
print(colors[1])
print(colors[3])
print(colors[4])
# print(colors[5])

# Solution - Loop
# FOR - Loop
for a in colors:
    print(a)

# FOR - range
for i in range(9):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(3, 10, 3):
    print(i)


# WHILE - Loop
i = 1
while i < 9:
    print(i)  # infinite loop
    i = i + 1  # i += 1

# цаашаагаа үргэлжлэх

# Exercise

# WHILE loop ашиглан 10-аас 100 хүртэлх тоонуудыг хэвлэнэ үү
i = 10
while i <= 100:
    print(i)
    i = i + 1

# 20-оос 60 хүртэлх тоонуудыг зөвхөн тэгш тоонуудыг нь хэвлэнэ үү

i = 20
while i <= 60:
    print(i)
    i = i + 2

i = 20
while i <= 60:
    if i % 2 == 0:
        print(i)
    i = i + 1
    
