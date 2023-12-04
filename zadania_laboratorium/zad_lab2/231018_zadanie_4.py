def middlepoint(start, end):
    start_x, start_y = start
    end_x, end_y = end
    midx = (start_x + end_x) / 2
    midy = (start_y + end_y) / 2
    return (midx, midy)


print(middlepoint((3, 7), (2, 4)))
