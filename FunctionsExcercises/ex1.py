def add_to_list(lst, strValue):
    lst.append(strValue)
    return lst


def main():
    lst = ['apple', 'banana']
    print("The old list is ")
    print(lst)
    print("Now, the new list is: ", add_to_list(lst,"strawberry"))

main()

