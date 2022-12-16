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
def game_over():
    print('''
   ~`. ~`. ~`.
   ~`.  O<-<   ~`.     GAME OVER
    ~`. ~`. ~`.                
    ''')
    exit()

def win():
    print('''
   ~`. ~`. ~`.
   ~`. \()/   ~`.
   ~`   ||   ~`.       HOORAY!
    ~`. /\   ~`.
    ~`. ~`. ~`.                

    ''')
    exit()

print("\n\nYou come to a crossroad.")
print('''
        ()
 <----- /\ -----> 
        /\    
 ''')
choice = input("Where do you want to go? Type 'left' or 'right':\n").lower()
if choice == 'right':
    print("\nYou fall into a hole...")
    game_over()

print("\n\nYou come to a lake. There is an island in the middle of the lake.")
print('''
                  /   ~~~~     ~~~~~       ~~~~     
        ()       /~~~    ~~~~    _____________  ~~~~
        /\      /  ~~~   ~~~~   /   ISLAND    \       ~~
        /\     /~~   ~~~~~     /               \  ~~~
 ''')
choice = input("How do you want to go, swim over or wait for a boat? Type 'swim' or 'wait':\n").lower()
if choice == 'swim':
    print("\nYou are attacked by trout...")
    game_over() 

print("\n\nNow you arrive at the island. There is a house with 3 doors. One red, one yellow and one blue.")
print('''
          ______________________
         /..................... \ 
        /....................... \ 
         |                      |
         |   __     __     __   |
         |  |R |   |Y |   |B |  |
         |  |  |   |  |   |  |  |
         ````````````````````````
 ''')
choice = input( "Which colour do you choose? Type 'red' or 'yellow' or 'blue':\n").lower()
if choice == 'red':
    print("\nYou enter a room full of fire..")
    game_over()
elif choice == 'yellow':
    print("\nYou enter a room and find the treasure!")
    win()
elif choice == 'blue':
    print("\nYou enter a room full of beasts..")
    game_over()
else:
    print("\nYou picked a room doesn't exist..")
    game_over()