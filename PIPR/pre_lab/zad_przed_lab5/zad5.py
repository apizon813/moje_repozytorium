def mean_value(list): return sum(list) / len(list)


def count_elements_above_average(list):
    average = mean_value(list)
    return len([m for m in list if m > average])


def collect(list):
    output = []
    for element in list:
        try:
            output.append(count_elements_above_average(element))
        except TypeError:
            output.append('ZŁA WARTOŚĆ')
        except ZeroDivisionError:
            output.append('DZIELENIE PRZEZ ZERO')
    return output


print(collect([[1, 2, 3], [5, 6, 7], [], [3, 4, 5], ['12a', 1, 4]]))
