print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

sum = 0

if size == "S":
    sum += 15
elif size == "M":
    sum += 20
elif size == "L":
    sum += 25

# print("The sum after sizes " + str(sum))

if size == "S" and pepperoni == "Y":
    sum += 2
if size == "M" or size == "L" and pepperoni == "Y":
    sum += 3
# print("The sum after pepperoni choice " + str(sum))

if extra_cheese == "Y":
    sum += 1

print("Your final bill is: "+ "$" + str(sum) + ".")