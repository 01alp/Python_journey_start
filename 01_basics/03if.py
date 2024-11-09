print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("Good to go")
else:
    print("Grow up!")
age = int(input("How old are you?"))
if age < 12:
    print("You should pay 5$")
elif 12 <= age <= 18:
    print("Pay $7")
elif age > 18:
    print("Pay $12")
