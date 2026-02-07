from functions.run_python_file import run_python_file


def main():
    print("Result for lorem txt file")
    print(run_python_file("calculator", "lorem.txt"))
    print()

    print("Result for calculator main file")
    print(run_python_file("calculator", "main.py"))
    print()

    print("Result for calculator main file")
    print(run_python_file("calculator", "../main.py"))
    print()

    print("Result for calculator logic file")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print()

    print("Result for '/bin/cat' directory:")
    print(run_python_file("calculator", "tests.py"))
    print()

    print("Result for 'pkg does not exist:")
    content = run_python_file("calculator", "nonexistent.py")
    print(f"content: {content}")


if __name__ == "__main__":
    main()