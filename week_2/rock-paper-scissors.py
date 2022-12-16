rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice_img = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors:\n"))
if(human_choice < 0 or human_choice >= 3):
    print("Invalid input. Please try again.")
    exit()
print(choice_img[human_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(choice_img[computer_choice])

if (human_choice == 0 and computer_choice == 2) or \
   (human_choice == 1 and computer_choice == 0) or \
   (human_choice == 2 and computer_choice == 1):
    print("You win!")
elif (human_choice == 0 and computer_choice == 1) or \
     (human_choice == 1 and computer_choice == 2) or \
     (human_choice == 2 and computer_choice == 0):
     print("You lose..")
else:
    print("It's a draw.")