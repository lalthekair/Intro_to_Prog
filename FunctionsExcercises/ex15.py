
def identifyFileType(file_name):
    if file_name.endswith(".txt"):
        return "That is the name of a text file."
    elif file_name.endswith(".docx"):
        return "That is the name of a word processing document."
    elif file_name.endswith(".py"):
        return "That is the name of a Python source file."
    else:
        return "'Unknown file type."


def main():
    filename = input('Enter the filename: ')
    res = identifyFileType(filename)
    print("Checking the type of ", filename)
    print(res)

main()