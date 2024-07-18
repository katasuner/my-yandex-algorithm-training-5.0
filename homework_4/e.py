def find_fraction(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 < n:
            left = mid + 1
        else:
            right = mid

    diagonal = left
    num_in_diagonal = n - (diagonal * (diagonal - 1) // 2)

    if diagonal % 2 == 1:
        numerator = num_in_diagonal
        denominator = diagonal - num_in_diagonal + 1
    else:
        numerator = diagonal - num_in_diagonal + 1
        denominator = num_in_diagonal

    return f'{numerator}/{denominator}'


n = int(input())
print(find_fraction(n))