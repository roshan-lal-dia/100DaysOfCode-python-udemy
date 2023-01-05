#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to Tip Calculator")

billAmount = float(input("What was the total Bill? $"))

tip_Percentage = int(input("What percentage Tip would you like to give? 10, 12 or 15? "))

People = int(input("How many people to split the Bill? "))

tip_Percentage = tip_Percentage / 100

tip_Percentage = billAmount * tip_Percentage

billAmount = billAmount + tip_Percentage

splitAmount = billAmount / People

splitAmount = '{:.2f}'.format(splitAmount)

print(f"Each person should pay :${splitAmount}")
