def matrix_multiply(a, b, mod = None, size = None):
    if size == None:
        size = len(a)

    result = [size * [0] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            val = 0
            for k in range(size):
                val += a[i][k] * b[k][j]

            result[i][j] = val % mod

    return result

def matrix_modular_power(matrix, exp, mod, size = None):
    if size == None:
        size = len(matrix)

    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    while 0 < exp:
        if exp & 1:
            result = matrix_multiply(result, matrix, mod, size)

        matrix = matrix_multiply(matrix, matrix, mod, size)
        exp >>= 1

    return result

# application : fibonacci sequence
def fibonacci_sequence(num, mod = None):
    if num == 0:
        return 0

    base = [[1, 1], [1, 0]]
    result = matrix_modular_power(base, num - 1, mod, size = 2)
    return result[0][0]