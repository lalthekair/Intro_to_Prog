print("-------------------------------------------")
keep_going = 'y'

while keep_going == 'y':
    item_price = float(input("Enter the item price"))
    discount_rate = float(input("Enter the discount rate"))
    discounted_price = (1 - discount_rate) * item_price
    print("The price after discount is ", discounted_price)
    keep_going = input("Do you want to calculate the price for another item? y or n")

print("-------------------------------------------")
budget = float(input("Enter the budget"))

while budget < 0:
    print("Enter a valid budget")
    budget = float(input("Enter the budget"))

expenses = int(input("Enter the expenses you have"))
total = 0

while expenses > 0:
    total += expenses #total = total + expenses
    expenses = int(input("Enter the expenses you have"))

print("The total expenses is ", total)

if total > budget:
    print("You exceeded the budget")
else:
    print("You are within the budget")

print("-------------------------------------------")
score = int(input("Enter a score"))
while score < 0 or score > 100:
    print("Error: The score cannot be negative or greater than 100")
    score = int(input("Enter a score"))
print("Accepted score!")

print("-------------------------------------------")
score = int(input("Enter a valid score"))
while score < 0: #50 < 0 --> false
    print("Error: the scpre cannot be negative")
    score = int(input("Enter a valid score"))

print("Accepted score")

print("-------------------------------------------")
score = int(input("Enter a score"))

while score < 0:
    print("Error: The score cannot be negative")
    score = int(input("Enter a score"))

print("Accepted score!")