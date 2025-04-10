# random number буюу дурын утга
import random

roll_dice = random.randint(1, 6)
print(roll_dice)


is_heads = random.choice([True, False])
print("You flipped heads: " + str(is_heads))

# 4 ширхэг хоолны цуглуулга list үүсгээд түүнийгээ random-оор хэвлэж
# харуулна уу
foods = ['tsuivan', 'buuz', 'khuushuur', 'plov']
is_food = random.choice(foods)
print('Your food is ' + is_food)
