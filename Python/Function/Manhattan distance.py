def multidimensional_manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])