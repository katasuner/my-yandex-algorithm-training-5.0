def find_prefix_sum(array, n):
    array_prefix_sum = [0]
    for i in range(n):
        array_prefix_sum.append(array_prefix_sum[-1] + array[i])
    return array_prefix_sum
def binary_search(length, target, array, n):
    left, right = 0, n - length
    while left <= right:
        middle = (left + right) // 2
        current_sum = array[middle + length] - array[middle]
        if current_sum == target:
            return middle + 1
        elif current_sum < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1





n, m  = map(int, input().split())
orcs_in_rgt = [int(num) for num in input().split()]
rgt_and_orcs = [tuple(map(int, input().split())) for _ in range(m)]

array_for_solve = find_prefix_sum(orcs_in_rgt, n)

for length, target in rgt_and_orcs:
    print(binary_search(length,target, array_for_solve, n))