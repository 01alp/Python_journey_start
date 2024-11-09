# If the bill was $150.00, split between 5 people, with 12% tip.
bill_total = float(input("How much is the bill? $"))
add_tip = float(
    input(
        f"How much tip would you like to leave? {bill_total*0.10:.2f}, {bill_total*0.12:.2f}, {bill_total*0.15:.2f}: "
    )
)
bill_total += add_tip

if bill_total > 150:
    people_number = int(input("How many people will split the bill?"))

    bill_perperson = bill_total / people_number
    print(f"Each person has to pay {bill_perperson:.2f}$")
else:
    print(f"The Total is {bill_total:.2f}")

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
