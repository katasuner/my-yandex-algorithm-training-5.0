coordinates = [(int(x), int(y)) for _ in range(int(input())) for x, y in (input().split(),)]

left_corner_x = min(x for x, y in coordinates)
left_corner_y = min(y for x, y in coordinates)
right_corner_x = max(x for x, y in coordinates)
right_corner_y = max(y for x, y in coordinates)


print(left_corner_x, left_corner_y, right_corner_x, right_corner_y)