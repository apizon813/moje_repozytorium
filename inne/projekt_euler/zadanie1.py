def sum_35_div(n, list):
    sum = 0
    for n in range(n):
        is_div = False
        for number in list:
            if n % number == 0:
                is_div = True
        if is_div:
            sum += n
    return sum










print(sum_35_div(1000, (3, 5)))
