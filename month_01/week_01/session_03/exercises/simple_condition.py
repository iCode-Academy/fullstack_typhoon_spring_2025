# check your age range 
age = int(input("Give me your age: "))

# baby
# teenager
# adult
# senior
# old age
if age < 0:
    print("Age cannot be Zero!")
elif age < 13:
    print('You are a baby')
elif age < 18:
    print("You are a teenager")
elif age < 65:
    print('You are an adult')
elif age < 100:
    print("You are a senior")
else:
    print('You are a dinosaur')