def get_multiples_count(numbers):
    multiples = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    counts = {multiple: 0 for multiple in multiples}

    for number in numbers:
        for multiple in multiples:
            if number % multiple == 0:
                counts[multiple] += 1

    return counts

numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
counts = get_multiples_count(numbers)
print(counts)