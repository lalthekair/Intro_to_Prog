def findSeven(str):
    res = str.find('seven')

    if not res == -1:
        return 'The string "seven" was found'
    if res == -1:
        return 'The string "seven" was not found'


def main():
	text = 'Four score and seven years ago'

	print(findSeven(text))
main()

