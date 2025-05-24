class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed  # Instance attribute


fido = Dog("Fido", "Golden Retriever")  # object fido
rex = Dog("Rex", "German Shepherd")  # rex object

print(Dog.species)  # Output: Canis familiaris
print(fido.species)  # Output: Canis familiaris
print(rex.species)  # Output: Canis familiaris

# Changing class attribute affects all instances
Dog.species = "Canis lupus familiaris"
print(fido.species)  # Output: Canis lupus familiaris
print(rex.species)  # Output: Canis lupus familiaris

# But setting the attribute on an instance creates an instance attribute
fido.species = "Changed for Fido"
print(fido.species)  # Output: Changed for Fido
print(rex.species)  # Output: Canis lupus familiaris
