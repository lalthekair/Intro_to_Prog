







'''
name = 'Aldana'
for var in name:
    print(var)


lst = ['a', 'b', 'c']
for a in lst:
    print(a)

name = 'Aldana'
for var in name:
    print('var')




name = 'Ali'
for var in name:
    var = 'X'
    print(name)



name = 'Ali'
for var in name:
    var = 'X'
print(name)

'''

print("Program 8.1")
stringValue = input("Enter a string value")
counter = 0
for x in stringValue:
    if x == 'T' or x == 't':
        counter +=1

print("String value has T and t ", counter, "times" )

str1 = 'Hello'
str2 = 'World'
res = str1 + str2

print(res)
