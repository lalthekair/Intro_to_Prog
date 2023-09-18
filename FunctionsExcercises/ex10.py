def findSeven2(str1, str2):
    if str1 in str2:
        return 'The string ' + str1 + " was found"
    if not str1 in str2:
        return 'The string ' + str1 + " was not found"


def main():
    text1 = 'Four'
    text2 = 'Four score and seven years ago'
    print(findSeven2(text1, text2))

main()
