

#Write a for loop that prints only odd numbers from 51 to 45

for num in range(51,44,-2):
    print(num)


'''
Write a loop that prompts the user to enter odd numbers. The loop stops if the user entered an even number that is bigger than 100. When the loop stops, the program should print the number of:

- Odd values entered by the user.

- Even values entered by the user.

- Summation of all odd values.

- Summation of all even values.
'''

sumOdd = 0
sumeven = 0
oddOccurances = 0
evenOccurances = 0

num = int(input("Enter a number"))

while num % 2 == 1 or (num % 2 == 0 and num < 100):

    if num % 2 == 1:
        sumOdd += num
        oddOccurances += 1

    else:
        sumeven += num
        evenOccurances += 1

    num = int(input("Enter a number"))


if num % 2 == 0 and num > 100:
    print("I won't calculate ", num)

print("You have entered", oddOccurances, "odd values. Their summation is ", sumOdd)
print("You have entered", evenOccurances, "even values. Their summation is ", sumeven)
