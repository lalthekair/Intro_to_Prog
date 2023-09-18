def findSeven(str1, str2):
    res = str2.find(str1)

    if not res == -1:
        return 'The string ' + str1 + ' was found'
    if res == -1:
        return 'The string ' + str1 + ' was not found'


def main():
    text1 = "Four"
    text2 = 'Four score and seven years ago'

    print(findSeven(text1, text2))
main()
