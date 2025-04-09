def combination(n, r):
    if n - r < r:
        r = n - r

    result = 1
    for i in range(1, r + 1):
        result *= (n - r + i) // i

    return result