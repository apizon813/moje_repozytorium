def metric_distance(n, coord1, coord2):
    if abs(coord1) > n or abs(coord2) > n:
        raise ValueError('coordinates larger than n')
    dist = abs(coord1 - coord2)
    if dist > n:
        return 2 * n + 1 - dist
    return dist


def distance(n, coords1, coords2):
    xdist = metric_distance(n, coords1[0], coords2[0])
    ydist = metric_distance(n, coords1[1], coords2[1])
    return xdist + ydist
