class MathUtils:
    @staticmethod
    def add(x, y):
        """Static method that doesn't use class or instance data"""
        return x + y

    @staticmethod
    def is_even(number):
        """Static method to check if a number is even"""
        return number % 2 == 0


# Using static methods
print(MathUtils.add(5, 3))  # 8
print(MathUtils.is_even(4))  # True

# Can also be called on an instance, but not common
math = MathUtils()
print(math.add(2, 3))  # 5
