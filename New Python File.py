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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
First = input("You are in a beautiful forest and you reach a Crossroad where one on your right leads to deep in the forest and the path seems to have disappeared as no one had walked on it for a long time. While the other on your left is surrounded by trees but the path seems to be waked on before. Which way would you like to go? Left Or Right ")
if First == "Left":
    Second = input("You walk on the path for a while and you are meet with a river.You can ether wait for a boat or swim across the.What would you like to do Would you like to wait or Swim Across the river? Answer Wait or Swim ")
    if Second == "Wait":
        Third = input("After waiting for the boat for a hour it arrives you wonder how it come to that side then you hop in and started your journy across the river .you reach the river shore there is a path that again leads back into the jugle you start walking on it mesmerized by the beauty of the forest untile you reach a big open space with three doors in the middle. Which one would you like to go into ? The red one , The green one or the blue one one of them will have your treasure.Answer Red, Green or Blue ")
        if Third == "Green":
            print("You went throught the green door and find your self in a room full of unimageable riches. You Won!")
        elif Third == "Blue":
            print("You went throught the blue door you are lock inside the room in complete darkness . Game Over ")
        elif Third == "Red":
            print("You enter the Red door and find your self facing a gaint dragon and the door locks behind you. Game over ")
        else:
            print("You went the wrong way and got lost in the jungle. Game over ")
    elif Second == "Swim":
        print("You start swimming and after swimming for a few minutes you come across some strainge fish and then you realise that those are the flesh eating fishes. Game Over ")
    else:
        print("You went the wrong way and got lost in the jungle. Game over ")
elif First == "Right":
    print("You start walking on the right path for some time and as the path was not walked on for a long time you end up getting lost and can not find your way out. Game Over ")
else:
    print("You went the wrong way and got lost in the jungle. Game over ")