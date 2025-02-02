import math

def is_prime(number):
    if number < 2:
        return False

    for divisor in range(1, math.floor(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True