def nth_fibonacci(num):
    if num == 1 or num == 2:
        return 1
    return nth_fibonacci(num - 1) + nth_fibonacci(num - 2)


NUMBER = int(input("Select a number: "))
print(nth_fibonacci(NUMBER))
