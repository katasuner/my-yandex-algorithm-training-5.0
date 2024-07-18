def find_min_step(n, coords):
    if len(set(y for _, y in coords)) == 1:
        return 0

    field = [['.'] * n for _ in range(n)]
    for x, y in coords:
        field[x][y] = '*'

    order_column = sorted((y for x, y in coords))

    middle = 0 if len(order_column) == 2 else len(order_column) // 2
    median_column = order_column[middle] if len(order_column) % 2 != 0 else (order_column[middle - 1] + order_column[middle]) // 2
    coordinates = [(x, y) for x, y in coords if y != median_column]
    free_coordinates = [(i, j) for i in range(n) for j in range(median_column, median_column + 1) if field[i][j] != '*']
    count = 0
    for i in range(len(free_coordinates)):
        count += abs(coordinates[i][0] - free_coordinates[i][0]) + abs(coordinates[i][1] - free_coordinates[i][1])

    return count


n = int(input())
coordinates = sorted([(int(x) - 1, int(y) - 1) for _ in range(n) for x, y in (input().split(),)], key=lambda x: (x[0], x[1]))
print(find_min_step(n, coordinates))