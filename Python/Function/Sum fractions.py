def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def irreducible_fraction(num, den):
    g = gcd(num, den)
    return num // g, den // g

def sum_fractions(num1, den1, num2, den2):
    l = lcm(den1, den2)
    num = num1 * (l // den1) + num2 * (l // den2)
    return irreducible_fraction(num, l)