def find_min_max(lst):
    minimum = min(lst)
    maximum = max(lst)
    return "The minimum value is " + str(minimum) + " and the maximum value is " + str(maximum)


def main():
    l1 = [4,3,1]
    l2 = ['b', 'a', 'z', 'c']

    print("Passing l1")
    print(find_min_max(l1))

    print("Passing l2")
    print(find_min_max(l2))
main()