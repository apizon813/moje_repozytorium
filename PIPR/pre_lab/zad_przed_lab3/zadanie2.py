def select(list):
    index = len(list) - 2
    selected_list = []
    while index > 0:
        selected_list.append(list[index])
        index -= 3
    return selected_list


LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(select(LIST))
