'''



size = 5
lst = [None] * size

index = 10
while index > size:
    lst[index-6] = float(input("Enter the number"))

    index -= 1

for a in lst:
    print(a)

'''

n = [1,2,3,4,5]
print(n)

for a in n:
    print(a, end=' ')
print()

index = 0
while index < len(n):
    print(n[index])

    index +=1
