import math

#random module
import random
rand1 = random.randint(0,2)
rand2 = random.randint(50,100)
rand3 = random.randint(-30, -10)

print(f"rand1: {rand1}")
print(f"rand2: {rand2}")
print(f"rand3: {rand3}")

#choice function from random module
import random
coin = random.choice(["Head", "Tails"])
dice = random.choice([1,2,3,4,5,6])

print(f"Your coin flip is: {coin}")
print(f"Your dice roll is: {dice}")