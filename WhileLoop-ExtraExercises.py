print("Exercise 1")

'''
#Exercise 1
num = int(input("Enter a number "))
print("The summation of numbers between 1 and", num, "is ", end='')
sum = 0
while num >= 1:
    sum += num
    num -= 1

print(sum)

'''


print("Exercise 2")
'''
num = 10
while num >= 1:
    print(num)
    num -=1

'''


print("Exercise 3")
'''
num = 1
while num <=10:
    if num % 2 == 0:
        print(num)
    num +=1
'''



print("Exercise 4")
'''
num = 10
sum = 0
while num >= 1:
    if num % 2 ==1:
        print(num)
        sum += num

    num -= 1

print("The summation of odd numbers between 1 and 10 is ", sum)
'''



print("Exercise 5")

'''
num1 = int(input("Enter num 1 "))
num2 = int(input("Enter num 2 "))

while num1 < 1 or num2 > 15 or num2 < num1:

    if num2 < num1:
        print("num1 must be smaller than num2")
    elif num1 < 1:
        print("num1 must be positive")
    else:
        print("num2 must be less than or equal to 15")
    num1 = int(input("Enter num 1 "))
    num2 = int(input("Enter num 2 "))

print("The values are accepted. The summation of all numbers between ", num1, " and ", num2, " is ", end='')
sum = 0


while num1 <= num2:
    sum += num1
    num1 +=1

print(sum)

'''