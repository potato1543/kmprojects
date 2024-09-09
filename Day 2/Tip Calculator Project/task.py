print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# print("Welcome to the tip calculator.")
# est_total = input("What is the total of the bill?")
# tip = input("What percentage tip would you like to give? 10, 12, or 15?")
# peeps = input("How many people to split the bill?")

tip1 = float((int(tip) / 100) + 1.0)
bill_per_person = float(bill) / float(people)
amt = bill_per_person * tip1
final = round(amt, 2)
# final = "{:.2f}".format(amt)
print(f"Each person should pay: {final}")
