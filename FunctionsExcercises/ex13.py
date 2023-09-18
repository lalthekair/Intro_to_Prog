def test_if_all_digits(str):
    if str.isdigit():
        return "string1, 'contains only digits"
    else:
        return "string1, 'contains characters other than digits.’ "

def main():
	text = '1200'
	print(test_if_all_digits(text))
main()
