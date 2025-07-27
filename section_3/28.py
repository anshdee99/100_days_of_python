ascii_art = """
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-'''-._  ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
"""


print ("Welcome to treasure island \nYour mission is to find the treasure.")
choice1 = input ("You're at cross roads where do you want to go? Left or Right\n").lower()
if choice1 == "left":
    choice2 = input ("""You've come to a lake.
There is an island in the middle of the lake.
Type 'wait' to wait for a boat or 'swim' to swim accross\n""").lower()
    if choice2 == "wait":
        choice3 = input("""You arrive at the island unharmed. 
There is a house with 3 doors. 
Which door would you choose ? R, Y or B\n""").lower()
        if choice3 == "y":
            print ("You found the treasure with gold. You win!")
        elif choice3 == "r":
            print ("You were attacked by hounds. Game over")
        elif choice3 == "b":
            print ("Rock fell on you. Game over!")    
    else: 
        print ("Game Over!")  
else: 
    print ("You fell into a hole. Game over!")
