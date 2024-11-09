# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

#     Take both people's names and check for the number of times the letters in the word TRUE occurs.

#     Then check for the number of times the letters in the word LOVE occurs.

#     Then combine these numbers to make a 2 digit number.

name1 = "David Beckham"
name2 = "Victoria Beckham"
count1 = 0
count2 = 0
combined_names = (name1 + name2).lower()
for text in combined_names:
    if text in "true":
        count1 += 1
    if text in "love":
        count2 += 1
score = int((str(count1) + str(count2)))
print(score)
