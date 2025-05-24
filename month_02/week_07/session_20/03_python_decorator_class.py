class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        """Getter for name"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name"""
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

    @property
    def age(self):
        """Getter for age"""
        return self._age

    @age.setter
    def age(self, value):
        """Setter for age"""
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


# Using properties
person = Person("John", 30)
print(person.name)  # Using getter: John
person.name = "Jane"  # Using setter
print(person.name)  # Jane

# This will raise an error
try:
    person.age = -5
except ValueError as e:
    print(e)  # Age cannot be negative
