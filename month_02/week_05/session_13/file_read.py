# File Read


# Open File
file = open('file_intro.md', 'r')
content = file.read()
print(content)
file.close()

# File modes:
# 'r' - Read (default)
# 'w' - Write (creates new file or truncates existing)
# 'a' - Append
# 'x' - Exclusive creation
# 'b' - Binary mode
# 't' - Text mode (default)
# '+' - Update (read and write)

# file read line by line
file = open('file_intro.md', 'r')
for i in range(8):
    content = file.readline()
    print(content)
file.close()

# file read all lines
file = open('file_intro.md', 'r')
content = file.readlines()
print(content)
file.close()
