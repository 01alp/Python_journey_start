import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# print(len(letters))//52
# print(len(numbers))//10
# print(len(symbols))//9
password = []


for letter in range(nr_letters):
    # Bir eklemedim cunku 0 dan basladigi icin 2 girilse 3 kere donerdi!
    random_letter = random.randint(0, 51)
    password.append(letters[random_letter])
for number in range(nr_numbers):
    random_numbers = random.randint(0, 9)
    password.append(numbers[random_numbers])
for symbol in range(nr_symbols):
    random_symbols = random.randint(0, 8)
    password.append(symbols[random_symbols])
random.shuffle(password)
print("".join(password))
# or
passo = ""
for char in password:
    passo += char
print(passo)
