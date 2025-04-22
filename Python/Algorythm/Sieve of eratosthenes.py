def sieve_of_eratosthenes(n):
    prime_numbers = []
    sieve = [False, False] + (n - 1) * [True]
    for number in range(2, n + 1):
        if sieve[number]:
            prime_numbers.append(number)
            for index in range(2 * number, n + 1, number):
                sieve[index] = False

    return prime_numbers