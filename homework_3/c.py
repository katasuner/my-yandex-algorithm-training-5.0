def find_min_deleted(n, numbers):
    if n == 1:
        return 0

    numbers.sort()
    frequencies = {}
    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1
        
    max_group = 0
    numbers_unique = sorted(set(numbers))
    for i in range(len(numbers_unique)):
        current = frequencies[numbers_unique[i]]
        if i < len(numbers_unique) - 1 and numbers_unique[i + 1] == numbers_unique[i] + 1:
            current += frequencies[numbers_unique[i + 1]]
        max_group = max(max_group, current)

    return n - max_group


n = int(input())
number = [int(i) for i in input().split()]
print(find_min_deleted(n, number))
