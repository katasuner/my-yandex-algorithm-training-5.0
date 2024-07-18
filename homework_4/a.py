def left_b(n, numbers, target):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def right_b(n, numbers, target):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


n = int(input())
numbers = [int(x) for x in input().split()]
numbers.sort()

for request in range(int(input())):
    L, R = map(int, input().split())
    less = left_b(n, numbers, L)
    greater_equal = right_b(n, numbers, R)
    print(greater_equal - less, end=' ')