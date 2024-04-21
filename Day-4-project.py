import random

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

options=[rock, paper, scissors]

user_opinion=int(input("Enter your Choice 0 for Rock, 1 for Paper and 2 for Scissors :  "))
print("Your Opinion is : \n\n" , options[user_opinion])

sys_opinion=random.randint(0,2)
print("System Opinion is : \n\n", options[sys_opinion])

print("\n\n\n")
if user_opinion >= 3 or user_opinion <= 0:
    print("Oops, Wrong Number you have Entered")
if user_opinion == 0 and sys_opinion == 0:
    print("Draw")
elif user_opinion == 0 and sys_opinion == 1:
    print("System Wins, You Lose the Game!")
elif user_opinion == 0 and sys_opinion == 2:
    print("You Win the Game")
elif user_opinion == 1 and sys_opinion == 0:
    print("You win the Game")
elif user_opinion == 1 and sys_opinion == 1:
    print("Draw!!")
elif user_opinion == 1 and sys_opinion == 2:
    print("System Wins, You Lose the Game!")
elif user_opinion == 2 and sys_opinion == 0:
    print("System Wins, You Lose the Game!")
elif user_opinion == 2 and sys_opinion == 1:
    print("You Win the game")
elif user_opinion == 2 and sys_opinion == 2:
    print("Draw!!")
