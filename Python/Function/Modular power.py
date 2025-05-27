def modular_power(num, exp, mod):
    num %= mod
    result = 1
    while 0 < exp:
        if exp & 1:
            result = (result * num) % mod

        num = (num * num) % mod
        exp >>= 1

    return result