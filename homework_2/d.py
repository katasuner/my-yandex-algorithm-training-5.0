def check_border(x, y, field):
    directions = ((0, -1), (-1, 0), (0, 1), (1, 0))
    perimeter_border = 0
    for dx, dy in directions:
        fx, fy = x + dx, y + dy
        if field[fx][fy] == '*':
            perimeter_border += 1
    return perimeter_border


field_chess = [['*'] * 10 for i in range(10)]
coordinates = [(int(i), int(j)) for _ in range(int(input())) for i, j in (input().split(),)]

for i, j in coordinates:
    field_chess[i][j] = '■'
print(sum(check_border(x, y, field_chess) for x, y in coordinates))