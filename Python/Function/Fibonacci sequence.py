def fibonacci_sequence(number):
    sequence = [0, 1]
    for index in range(2, number + 1):
        sequence.append(sequence[index - 1] + sequence[index - 2])

    return sequence