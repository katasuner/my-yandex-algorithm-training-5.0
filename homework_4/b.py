def total_nott_free_cells(k):
    cells = ((k * (k + 1)) // 2) - 1
    ships = (((k * (k + 1)) // 2) * k) - (((k - 1) * k * (k + 1)) // 3)

    return cells + ships


def binary_search_k(n):
    left, right = 0, n
    while left <= right:
        middle = (left + right) // 2
        if total_nott_free_cells(middle) <= n:
            left = middle + 1
        else:
            right = middle - 1

    return right


n = int(input())
print(binary_search_k(n))
