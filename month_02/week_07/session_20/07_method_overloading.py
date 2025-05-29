class Calculator:
    def add(self, *args):
        """Method that accepts variable number of arguments"""
        return sum(args)

    def multiply(self, x, y=1, z=1):
        """Method with default parameters"""
        return x * y * z


calc = Calculator()
print(calc.add(1, 2))  # 3
print(calc.add(1, 2, 3, 4))  # 10
print(calc.multiply(5))  # 5
print(calc.multiply(5, 2))  # 10
print(calc.multiply(5, 2, 3))  # 30
