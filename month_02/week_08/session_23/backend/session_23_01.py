import os

# Current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Joining paths (OS-independent)
# Windows - C:/Users/tamir
# MacOS - /Users/tamir
# Linux - /usr/tamir

data_file = os.path.join(current_dir, "data", "sample.txt")
print(f"Data file path: {data_file}")

# Checking if a file exists
if os.path.exists(data_file):
    print(f"File exists: {data_file}")
else:
    print(f"File does not exist: {data_file}")
