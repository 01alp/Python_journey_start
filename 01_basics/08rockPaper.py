import random


choose = int(input("Type 0 for rock, 1 for paper, 2 for Scissors"))
if choose < 0 or choose > 2:
    print("Invalid number")
    exit()
computer_choice = random.randint(0, 2)

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]
print(game_images[choose])

print("Computer choose:")
print(game_images[computer_choice])


if choose == computer_choice:
    print("We are even!")

elif choose == 0 and computer_choice != 1:
    print("You win!")
elif choose == 1 and computer_choice != 2:
    print("You win")
elif choose == 2 and computer_choice != 0:
    print("You win!")
else:
    print("you lost")
