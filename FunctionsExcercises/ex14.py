def main():
    print(find_str('apple', 'a'))
    print(find_str('orAnge', 'a'))
    print(find_str("Nour", 'b'))

def find_str(str1, str2):
    index = str1.find(str2)

    if index != -1:
        return str2 + " was found in " + str1 + " at index number " + index

    else:
        return -1

main()