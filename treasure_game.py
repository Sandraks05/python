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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure island /n your mission is to find the treasure")
step1 =input( 'You\'re at a cross road . Where do you want to go ? \n\t\t\t\t Type "left" or "right"\n') .lower()
if step1=="left":
    step2=input('You have come to a lake There is an island in the middle of the lake. Type "wait" to wait. Type "swim" to swim across \n') .lower()
    if step2=="wait":
        step3=input('You have arrived at the island unharmed. There is house with Three door . One "red", one "yellow" and another is "blue"\n') .lower()
        if step3=="red":
            print("\n\t\t\t\tIts room full of fire.\n\t\t\t\tGame over.")
        elif step3=="blue":
            print("\n\t\t\t\tyou enter room of beasts.\n\t\t\t\t Game over.")
        elif step3=="yellow":
            print("you found the treasure.You Win!!!")
        else:
            print("\n\t\t\t\tGame Over")
    else:
        print("\n\t\t\t\tYou got attack by trout.\n\t\t\t\tGame over")            
else:
    print("\n\t\t\t\tYou fell in to hole.\n\t\t\t\tGame over")
    



