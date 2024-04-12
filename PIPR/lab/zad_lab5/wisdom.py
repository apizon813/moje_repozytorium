def answer():
    return 42


if __name__ == "main":
    print("Hello world")
    print('the answer is ' + answer())
else:
    print("module was imported and not run as main!")
    print(f"__name__ is {__name__}")
