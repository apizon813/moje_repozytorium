def fibonacci(max):
    fib = [1, 1]
    n = 1
    while True:
        if fib[n] + fib[n - 1] >= max:
            return fib
        else:
            fib.append(fib[n] + fib[n - 1])
        n += 1

def sum_even(list):
    output = 0
    for number in list:
        if number % 2 == 0:
            output += number
    return output


print(sum_even(fibonacci(4000000)))