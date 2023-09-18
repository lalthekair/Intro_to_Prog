def check_if_all_digits(val):
    if val.isdigit():
        return True

    return False

def main():
    while True:
        v1 = input("Enter the value")

        if check_if_all_digits(v1) == True:
            print("The string has only digits")
        else:
            print("The string has digits and letters")
            break

main()