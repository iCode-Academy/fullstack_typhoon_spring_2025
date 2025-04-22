# File Read with Context

with open("output.txt", "w") as file:
    file.write("Hello World")

with open("log.txt", "a") as file:
    file.write("New Log Entry \n")

# working with multiple files

with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for line in input_file:
        output_file.write(line.upper())
