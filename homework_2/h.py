n, m = map(int, input().split())
characters = [[int(c) for c in input().split()] for _ in range(n)]

max_value, index_row, index_column = 0, 0, 0
powers =[]

# УЗНАТЬ ИНДЕКС МАКСИМАЛЬНОГО ЗНАЧЕНИЯ В МАТРИЦЕ (ij)

for i in range(n):
    for j in range(m):
        value = characters[i][j]
        if value > max_value:
            max_value = value
            index_row = i
            index_column = j


# УДАЛЯЕМ СТРОКУ И ИЩЕМ МАКСИМАЛЬНОЕ ЗНАЧЕНИЕ В МАТРИЦЕ БЕЗ СТРОКИ
max_without_row, j_r = 0, 0
for i in range(n):
    if i == index_row:
        continue
    for j in range(m):
        value = characters[i][j]
        if value > max_without_row:
            max_without_row = value
            j_r = j

# Удаляем и строку и столбец и ищем максимальную силу героя
max_power_first = 0

for i in range(n):
    if i == index_row:
        continue
    for j in range(m):
        if j == j_r:
            continue
        value = characters[i][j]
        if value > max_power_first:
            max_power_first = value

# Добавляем для сравнения кортеж из значений(сила героя, удаленная строка, удаленный столбец)
powers.append((max_power_first, index_row + 1, j_r + 1))

# УДАЛЯЕМ СТОЛБЕЦ И ИЩЕМ МАКСИМАЛЬНОЕ ЗНАЧЕНИЕ В МАТРИЦЕ БЕЗ СТОЛБЦА
max_without_column, i_r = 0, 0

for i in range(n):
    for j in range(m):
        if j == index_column:
            continue
        value = characters[i][j]
        if value > max_without_column:
            max_without_column = value
            i_r = i

#УДАЛЯЕМ И СТРОКУ И СТОЛБЕЦ И ИЩЕМ МАКСИМАЛЬНУЮ СИЛУ ГЕРОЯ
max_power_second = 0

for i in range(n):
    if i == i_r:
        continue
    for j in range(m):
        if j == index_column:
            continue
        value = characters[i][j]
        if value > max_power_second:
            max_power_second = value

powers.append((max_power_second, i_r + 1, index_column + 1))

find_better = min(powers, key=lambda x: x[0])

print(find_better[1], find_better[2])