def permutation(n, r):
    if n < r:
        return 0

    result = 1
    for i in range(n, n - r, -1):
        result *= i

    return result