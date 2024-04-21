print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
stage1=input('Enter your choice "Left" or "Right"\n')
if stage1=="left":
    print("Great Choice, Move Ahead!!")

    stage2=input('There is a river with a crocodile here, What is your choice do you like to "Swim" or "Wait" for the Boat ?\n').lower()
    if stage2 == "swim":
        print("Oh No! as i already said Before There is a crocodile in a River So you Dead, Game Over.\n")
    else:
        print("Great You choose to wait for Boat, After 15 MINUTES the boat arrived and you reached your next destination\n")

        stage3=input('Now you are in the last challenge of the Game, There are three doors in front of you which one you need to open "Red", "Blue" and "Yellow", You can select any one of these.\n').lower()
        if stage3=="red":
            print("Wrong door, Game Over")
        elif stage3=="yellow":
            print("Great Choice!!, You Won a Game.")
        else:
            print("Wrong Door, Game Over.")
else:
    print("OOps you fall into the Hole, You are Dead, Game Over")
