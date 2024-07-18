n = int(input())
berries = tuple(((i, int(a), int(b))) for i in range(1, n + 1) for a, b in (input().split(),))

increment_positive = [(i, a, b) for i, a, b in berries if (a - b) >= 0]
if increment_positive:
    max_b_in_positive = max(increment_positive, key=lambda x: x[2])
    increment_positive.remove(max_b_in_positive)
    increment_positive.append(max_b_in_positive)

increment_negative = [(i, a, b) for i, a, b in berries if (a - b) < 0]
if increment_negative:
    max_a_in_negative = max(increment_negative, key=lambda x: x[1])
    increment_negative.remove(max_a_in_negative)
    increment_negative.insert(0, max_a_in_negative)
    
max_height = start = 0
orderlist = []

for i, a, b in increment_positive + increment_negative:
    start += a
    if start > max_height:
        max_height = start
    start -= b
    orderlist.append(i)


print(max_height, ' '.join(str(i) for i in orderlist), sep='\n')