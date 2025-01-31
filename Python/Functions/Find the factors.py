import math

def find_the_factors(number):
    factors = set()
    for divisor in range(1, math.floor(number ** 0.5) + 1):
        if number % divisor == 0:
            factors.add(divisor)
            factors.add(number // divisor)