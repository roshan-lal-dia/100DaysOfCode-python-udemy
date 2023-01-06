# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

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
import random as r

user_choose = int(input("What do you want to choose? Type 0 for Rocks, 1 for Paper and 2 for Scissors\n"))

choice = [rock, paper, scissors]

print (choice[user_choose])

computer_choose = r.randint(0,2)

print("Computer Choose:\n" + choice[computer_choose])

if user_choose == 0 and computer_choose ==1:
    result = "loose"
    print("You "+ result)
elif user_choose == 1 and computer_choose ==0:
    result = "win"
    print("You "+ result)
elif user_choose == 1 and computer_choose == 2:
    result = "loose"
    print("You "+ result)
elif user_choose == 2 and computer_choose == 1:
    result = "win"
    print("You "+ result)
elif user_choose == 2 and computer_choose == 0:
    result= "loose"
    print("You "+ result)
elif user_choose == 0 and computer_choose == 2:
    result= "win"
    print("You "+ result)
else:
    print("Same sweet, try again")