# Функция для проверки внутренностей прямоугольника
def check_correct_rectangle(left_up_point, right_down_point, field):
    for i in range(left_up_point[0], right_down_point[0] + 1):
        for j in range(left_up_point[1], right_down_point[1] + 1):
            if field[i][j] == '.':
                return False

    return True


# Функция для разделения прямоугольника, в случае если он один
def transformstion_rectangle(m, n, field):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if field[i][j] == 'a':
                if field[i][j + 1] == 'a' and field[i + 1][j] == 'a':
                    for x in range(i, m + 1):
                        for z in range(j + 1, n + 1):
                            if field[x][z] == '.':
                                break
                            field[x][z] = 'b'
                elif field[i][j + 1] == '.' and field[i + 1][j] == 'a':
                    for x in range(i + 1, m + 1):
                        if field[x][j] == '.':
                            break
                        field[x][j] = 'b'
                elif field[i][j + 1] == 'a' and field[i + 1][j] == '.':
                    for x in range(j + 1, n + 1):
                        if field[i][x] == '.':
                            break
                        field[i][x] = 'b'



# Функция для нахождения всех точек прямоугольника
def find_point_and_fill(x, y, m, n, field, symbol, count):
    left_up = (x, y)
    right_up = (0, 0)
    left_down = (0, 0)
    right_down = (0, 0)
    if count == 1:
        # Поиск правого верхнего угла для первого прямоугольника
        for j in range(y, n + 2):
            if field[x][j] == '.':
                break
            else:
                right_up = (x, j)

    elif count == 2:
        # Поиск правого верхнего угла для второго прямоугольника
        for j in range(y, n + 2):
            if field[x][j] == '.':
                break
            elif field[x][j] == 'a':
                continue
            else:
                right_up = (x, j)

    # Поиск нижних углов
    for i in range(x, m + 2):
        if all(cell == '.' for cell in field[i]):
            break
        if field[i][y] == '#' and field[i][right_up[1]] == '#':
            left_down = (i, y)
            right_down = (i, right_up[1])

        else:
            break
    if left_up == right_up and left_down == left_up and left_up == right_down and right_down == right_up:
        if count == 1:
            field[left_up[0]][left_up[1]] = 'a'
            return 0
        else:
            field[left_up[0]][left_up[1]] = 'b'
    if check_correct_rectangle(left_up, right_down, field):
        for i in range(x, right_down[0] + 1):
            for j in range(y, right_down[1] + 1):
                field[i][j] = symbol

    return 1


# Функция для основных манипуляций
def main_function(m, n, field):
    safe_result_func = 0
    count = 0
    barrier = [['.'] * (n + 2) for _ in range(m + 2)]
    # встроим поле в барьер
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            barrier[i][j] = field[i - 1][j - 1]

    # Ищем левые верхние углы прямоугольников
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if barrier[i][j] == '#':
                count += 1
                if count > 2:
                    return False
                # как нашли, запускаем функцию для нахождения других точек
                safe_result_func = find_point_and_fill(i, j, m, n, barrier, 'a' if count == 1 else 'b', count)
                
    if count == 0:
        return False

    if count == 1 and safe_result_func == 1:
        transformstion_rectangle(m, n, barrier)
    elif count == 1 and safe_result_func == 0:
        return False


    return barrier


m, n = map(int, input().split())
field = [[symbol for symbol in input()] for _ in range(m)]



if main_function(m, n, field):
    new_field = main_function(m, n, field)
    print('YES')
    for row in range(1, m + 1):
        for column in range(1, n + 1):
            print(*new_field[row][column], end='')
        print()
else:
    print('NO')
