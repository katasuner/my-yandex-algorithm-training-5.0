n_1, numbers_1 = int(input()), set(int(num) for num in input().split())
n_2, numbers_2 = int(input()), set(int(num) for num in input().split())
n_3, numbers_3 = int(input()), set(int(num) for num in input().split())

common12 = numbers_1.intersection(numbers_2)
common23 = numbers_2.intersection(numbers_3)
common31 = numbers_3.intersection(numbers_1)

print(*sorted(common12.union(common23).union(common31)))