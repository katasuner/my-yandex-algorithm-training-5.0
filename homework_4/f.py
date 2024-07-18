def find_min_witdh(w, h, broked_tiles):
    broked_tiles.sort()  # Сортируем трещинные плитки по координате x
    y = [tile[1] for tile in broked_tiles]  # Извлекаем координаты y

    # Найдем префиксные и суффикные суммы
    prefix_total_min = [0] * len(y)
    prefix_total_max = [0] * len(y)
    suffix_total_min = [0] * len(y)
    suffix_total_max = [0] * len(y)

    prefix_total_min[0] = prefix_total_max[0] = y[0]
    for i in range(1, len(y)):
        prefix_total_min[i] = min(prefix_total_min[i - 1], y[i])
        prefix_total_max[i] = max(prefix_total_max[i - 1], y[i])

    suffix_total_min[-1] = suffix_total_max[-1] = y[-1]
    for i in range(len(y) - 2, -1, -1):
        suffix_total_min[i] = min(suffix_total_min[i + 1], y[i])
        suffix_total_max[i] = max(suffix_total_max[i + 1], y[i])

    left, right = 1, min(w, h) + 1
    while left < right:
        middle = (left + right) // 2
        possible = False

        left_index = 0
        for r in range(len(broked_tiles)):
            while broked_tiles[r][0] - broked_tiles[left_index][0] >= middle:
                left_index += 1

            max_y = max(prefix_total_max[left_index - 1] if left_index > 0 else -1,
                        suffix_total_max[r + 1] if r + 1 < len(broked_tiles) else -1)
            min_y = min(prefix_total_min[left_index - 1] if left_index > 0 else h + 1,
                        suffix_total_min[r + 1] if r + 1 < len(broked_tiles) else h + 1)

            if min_y == -1 or max_y - min_y + 1 <= middle:
                possible = True
                break

        if possible:
            right = middle
        else:
            left = middle + 1

    return left


w, h, n = map(int, input().split())
broken_tiles = [(int(x), int(y)) for _ in range(n) for x, y in (input().split(),)]

print(find_min_witdh(w, h, broken_tiles))

