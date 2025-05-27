def modular_power(num, exp, mod):
    num %= mod
    result = 1
    while 0 < exp:
        if exp & 1:
            result = (result * num) % mod

        num = (num * num) % mod
        exp >>= 1

    return result

def modular_inverse(n, mod):
    return modular_power(n, mod - 2, mod)

MOD = 10 ** 9 + 7 # default value