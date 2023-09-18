def x(v1, v2):

    len1 = len(v1)
    len2 = len(v2)

    if len1 == len2:
        return "both values have the same length"

    elif len1 > len2:
        if v1.islower():
            return v1.upper()
        elif v1.isupper():
            return v1.lower()
        else:
            return


    else:
        if v2.islower():
            return v2.upper()
        elif v2.isupper():
            return v2.lower()
        else:
            return



def main():
    print(x("a", "bb"))
    print(x("salma", 'a'))

main()