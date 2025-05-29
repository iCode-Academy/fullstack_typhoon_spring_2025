class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        """Instance method"""
        return f"{self.name} says Woof!"

    def change_name(self, new_name):
        """Instance method that modifies instance data"""
        self.name = new_name


fido = Dog("Fido", "Golden Retriever")
print(fido.bark())  # Fido says Woof!
fido.change_name("Buddy")
print(fido.bark())  # Buddy says Woof!
