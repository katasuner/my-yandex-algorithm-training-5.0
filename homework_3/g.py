def find_point(n, points):
    set_point = set(points)
    min_quantity = 3
    coodinates = ()


    for i in range(n):
        for j in range(i + 1, n):
            A, B = points[i], points[j]
            x1, y1 = A
            x2, y2 = B
            v1 = x1 + x2
            v2 = y1 + y2
            x3 = (v1 - y1 + y2) / 2
            if x3 % 1 == 0:
                y3 = (x1 - x2 + v2) / 2
                x4 = (v1 + y1 - y2) / 2
                y4 = (x2 - x1 + v2) / 2
            else:
                continue

            if (x3, y3) in set_point and (x4, y4) in set_point:
                return 0

            elif (x3, y3) in set_point and (x4, y4) not in set_point:
                min_quantity = 1
                coodinates = (x4, y4)


            elif (x3, y3) not in set_point and (x4, y4) in set_point:
                min_quantity = 1
                coodinates = (x3, y3)

            elif (x3, y3) not in set_point and (x4, y4) not in set_point:
                if 2 < min_quantity:
                    min_quantity = 2
                    coodinates = ((x3, y3), (x4, y4))


    return min_quantity, coodinates


n = int(input())
points = tuple((int(x), int(y)) for _ in range(n) for x, y in (input().split(),))
result = find_point(n, points)
if result == 0:
    print(result)
elif result[0] == 1:
    print(result[0])
    for x in result[1]:
        print(int(x), end=' ')
else:
    print(result[0])
    for x, y in result[1]:
        print(int(x), int(y))