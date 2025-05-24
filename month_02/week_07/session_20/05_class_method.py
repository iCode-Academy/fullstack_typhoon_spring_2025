class Dog:
    count = 0  # Class attribute

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.count += 1

    @classmethod
    def get_count(cls):
        """Class method to get the count of dogs"""
        return f"There are {cls.count} dogs"

    @classmethod
    def from_string(cls, dog_string):
        """Class method as an alternative constructor"""
        name, breed = dog_string.split("-")
        return cls(name, breed)


fido = Dog("Fido", "Golden Retriever")
rex = Dog("Rex", "German Shepherd")

print(Dog.get_count())  # There are 2 dogs

# Using alternative constructor
buddy = Dog.from_string("Buddy-Poodle")
print(buddy.name)  # Buddy
print(buddy.breed)  # Poodle
print(Dog.get_count())  # There are 3 dogs
