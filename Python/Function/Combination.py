def round(n):
    if 0 <= n:
        return int(n + 0.5)
    else:
        return int(n - 0.5)

def combination(n, r):
    if n < r:
        return 0

    if n - r < r:
        r = n - r

    result = 1
    for i in range(1, r + 1):
        result *= (n - r + i) / i

    return round(result)