# randint(a,b)
import random

# random integer
random_integer = random.randint(1, 2)
print(random_integer)

# random floating number
random_float = random.random()  # 0.0 to 1.0 , 1 not included
print(random_float)

# 0-5
r_decimal = random.random() * 5
print(f"{r_decimal:.2f}")

rnd_number = random.randint(0, 2)
print("Heads" if rnd_number == 0 else "Trials")
