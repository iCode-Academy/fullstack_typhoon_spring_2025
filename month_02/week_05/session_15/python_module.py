import math  # standard module
import math_utils

# Тодорхой элементүүдийг импортлох
from math_utils import PI, square

print(math.sin(90))

print(math_utils.square(4))  # 16
print(math_utils.cube(4))  # 64


print(square(4))  # 16
print(PI)  # 3.1415


import package_01.module_01
from package_01.module_01 import function1
from package_01.module_01 import function2
print(package_01.module_01.function1())

print(function1())
print(function2())
# ```
# my_project/
# ├── __init__.py
# ├── config.py
# ├── utils/
# │   ├── __init__.py
# │   ├── math_utils.py
# │   └── file_utils.py
# ├── models/
# │   ├── __init__.py
# │   └── user.py
# └── services/
#     ├── __init__.py
#     ├── auth.py
#     └── storage.py
# ```