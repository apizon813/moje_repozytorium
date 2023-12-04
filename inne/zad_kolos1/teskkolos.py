def count_symbols(arr):
    dict = {}
    for lin in arr:
        for char in lin:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    return dict



array = [['a', 'c', 'o'], ['a', 'a', 'c'], ['c', 'b', 'a']]
print(count_symbols(array))

