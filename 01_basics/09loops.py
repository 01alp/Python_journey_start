# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"The highest score in the class is: {max_score}")

# Range
sum = 0
for number in range(2, 101, 2):  # Even numbers
    sum += number
print(sum)

# FizzBuzz game
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Password generator
