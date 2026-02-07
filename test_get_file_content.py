from functions.get_file_content import get_file_content


def main():
    print("Result for lorem txt file")
    print(get_file_content("calculator", "lorem.txt"))
    print()

    print("Result for calculator main file")
    print(get_file_content("calculator", "main.py"))
    print()

    print("Result for calculator logic file")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    print("Result for '/bin/cat' directory:")
    print(get_file_content("calculator", "/bin/cat"))
    print()

    print("Result for 'pkg does not exist:")
    content = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"content: {content}")


if __name__ == "__main__":
    main()