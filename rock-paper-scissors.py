print("Welcome to rock paper scissors game")
#rock
rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random
game_image = [rock , paper , scissors]
user_choice=int(input("what do you choose ,type 0 for rock ,1 for  paper or 2 for scissors \n"))
print(game_image[user_choice])
computer_choice= random.randint(0,2)
print("computer chose")
print(game_image[computer_choice])
if user_choice >=3 or user_choice < 0:
    print("you entered invalid number.")
elif user_choice == 0 and computer_choice ==2:
    print("you win !")
elif computer_choice == 0 and user_choice == 2:
    print("you lose :(")
elif computer_choice > user_choice:
    print("you lose :(")
elif user_choice > computer_choice:
    print("you win! ")    
elif computer_choice == user_choice:
    print("It's a draw")
elif user_choice >=3 or user_choice < 0:
    print("you entered invalid number.")
