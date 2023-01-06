print('''
*******************************************************************************
                             --,     ___
                            /  '---.'   \
                             \          `.
                              `.         '`--.__
                                |  *            ``.
                               / .- Jalpaiguri     |
                               \ \ \_   .-.        |
                              _/ |   \../ `.      /
                            _/ _/           \__--.
                          ,'  /
                          \   |
                           '\  \-.,
                             \.    \
                            ._|     `-.-,
                           /             |
                          |        _/--_/
                          |    .  |
                          |   | \./
                          |   |
                           |  \
                           |   \..
                          /       \-'|
                       ._/           /
                    _,/              \
               _._-'   * Suri       /-
          __,/'                    /
         /                         \
   /. _/'                           |
  |  '                              "-.
  \.                                  |
    \.                                \
     --'\                             |
        `-.                   Kolkata  /
           \_                  *       |
             \    *                    \
           _-"     Midnapore            \
           \.                 ".     _  |
             \.              / |    | \ |
               \  .         /  \    / '\|
                \| "|     ,'    S@yaN
                    \.   /          15.08.02
                     |;-'

*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input("Do you want to move Left or Right:\n")
direction = direction.lower()
if direction != "left":
    print("No way there, Game Over")
else:
    lake = input("There is a lake between you and a island, want to Swim or Wait for a Boat:\n")
    lake = lake.lower()
    if lake == "swim":
        print("You,re eaten by Piranhas, Game Over")
    else:
        door = input("You have reached the island, There are three doors in island\n Which door you want to open?\n Red Yellow Blue:\n")
        door = door.lower()
        if door == "red":
            print("You have been taken to hell")
        elif door == "yellow":
            print("You have been eaten by dinosaur")
        else:
            print("You got the treasure, but nothing in there")
    

