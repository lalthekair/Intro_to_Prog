def add_to_list_at_index(lst, val, i):
    lst.insert(i, val)
    return lst


def main():
    lst = [100,500, 90, 'apple']
    print("The old list is ", lst)
    print("The length of the old list is ", len(lst))
    print("I will add 'orange' after 500")
    print(add_to_list_at_index(lst, 'orange', 2))
    print("The length of the new list is ", len(lst))



main()

