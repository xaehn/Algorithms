def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def irreducible_fraction(num, den):
    g = gcd(num, den)
    return num // g, den // g