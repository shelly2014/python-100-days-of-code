#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("**Welcome to the Tip Calculator!**")
total_bill = float(input("What was the total bill?\n$"))
percent = int(input("What percentage tip would like to give? 10, 12, or 15?\n"))
num = int(input("How many people to split the bill?\n"))

pay = round(total_bill*(1+percent/100)/num, 2)
pay = "{:.2f}".format(pay)
print(f"Each person should pay: \n${pay}")