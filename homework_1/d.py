def check_cell_ladya(x, y, field):
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        fx, fy = x + dx, y + dy
        while 0 <= fx < 8 and 0 <= fy < 8:
            cell = field[fx][fy]
            if cell == '*':
                field[fx][fy] = '.'
                count += 1
            elif cell == '.':
                fx, fy = fx + dx, fy + dy
                continue
            else:
                break
            fx, fy = fx + dx, fy + dy

    return count


def check_cell_elephant(x, y, field):
    count = 0
    directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    for dx, dy in directions:
        fx, fy = x + dx, y + dy
        while 0 <= fx < 8 and 0 <= fy < 8:
            cell = field[fx][fy]
            if cell == '*':
                count += 1
                field[fx][fy] = '.'
            elif cell == '.':
                fx, fy = fx + dx, fy + dy
                continue
            else:
                break
            fx, fy = fx + dx, fy + dy
    return count

field = [[cell for cell in input() if cell != " "] for row in range(8)]
count_free = 64

for row in range(8):
    for column in range(8):
        if field[row][column] == 'R':
            count_free -= check_cell_ladya(row, column, field) + 1
        elif field[row][column] == 'B':
            count_free -= check_cell_elephant(row, column, field) + 1


print(count_free)