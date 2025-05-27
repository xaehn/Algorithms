def modular_power(num, exp, mod):
    num %= mod
    result = 1
    while 0 < exp:
        if exp & 1:
            result = (result * num) % mod

        num = (num * num) % mod
        exp >>= 1

    return result

def modular_combination(n, r, mod):
    if n < r:
        return 0

    if n - r < r:
        r = n - r

    fact = (n + 1) * [1]
    for i in range(1, n + 1):
        fact[i] = (i * fact[i - 1]) % mod

    inv_fact = (n - r + 1) * [1]
    inv_fact[n - r] = modular_power(fact[n - r], mod - 2, mod)
    for i in range(n - r - 1, -1, -1):
        inv_fact[i] = ((i + 1) * inv_fact[i + 1]) % mod

    return (((fact[n] * inv_fact[r]) % mod) * inv_fact[n - r]) % mod

MOD = 10 ** 9 + 7 # default value