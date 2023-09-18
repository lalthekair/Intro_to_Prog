def findSeven(str):
    if "seven" in str:
        return 'The string "seven" was found'
    if not "seven" in str:
        return 'The string "seven" was not found'


def main():
	text = 'Four score and seven years ago'

	print(findSeven(text))
main()
