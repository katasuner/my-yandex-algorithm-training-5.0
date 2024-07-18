def standardize_match(x1, y1, x2, y2):
    """ Функция для стандартизирования направлений спичек"""

    # вертикальная спичка направленная снизу вверх
    if x1 == x2 and y1 < y2:
        return x1, y1, x2, y2

    # Вертикальная спичка направленная сверху вниз(меняем направление)
    elif x1 == x2 and y2 < y1:
        return x2, y2, x1, y1

    # Горизонтальная спичка направленная слева направо

    elif y1 == y2 and x1 < x2:
        return x1, y1, x2, y2

    # Горизонтальная спичка направленная справа налево (меняем направление)
    elif y1 == y2 and x2 < x1:
        return x2, y2, x1, y1

    elif x1 < x2 and y1 < y2:
        return x1, y1, x2, y2

    elif x2 < x1 and y2 < y1:
        return x2, y2, x1, y1

    elif x1 > x2 and y1 < y2:
        return x1, y1, x2, y2

    elif x1 < x2 and y2 < y1:
        return x2, y2, x1, y1


def find_vector(a, b):
    """ Функция для нахождения вектора параллельного переноса"""
    return (b[0] - a[0], b[1] - a[1])



shifts = {}
n = int(input())
matches_A = [standardize_match(int(x1), int(y1), int(x2), int(y2)) for _ in range(n) for x1, y1, x2, y2 in [input().split()]]
matches_B = {standardize_match(int(x1), int(y1), int(x2), int(y2)) for _ in range(n) for x1, y1, x2, y2 in [input().split()]}

for a in matches_A:
    for b in matches_B:
        v = find_vector(a, b)
        shift = (a[0] + v[0], a[1] + v[1], a[2] + v[0], a[3] + v[1])

        if shift == b:
            shifts[v] = shifts.get(v, 0) + 1

max_shift = max(shifts.values(), default=0)
print(n - max_shift)
