safe_lst = []

for _ in range(int(input())):
    n = int(input())
    numbers = map(int, input().split())
    len_segment = 0
    all_len_segment = []
    quantity_segments = 0
    min_value = n
    for value in numbers:
        if value < min_value:
            min_value = value
        if value >= (len_segment + 1) and (len_segment + 1) <= min_value:
            len_segment += 1
        else:
            if len_segment > 0:
                all_len_segment.append(len_segment)
                quantity_segments += 1
            len_segment = 1
            min_value = value
    if len_segment > 0:
        all_len_segment.append(len_segment)
        quantity_segments += 1

    safe_lst.append((quantity_segments, all_len_segment))

for quantity, len_segment in safe_lst:
    print(quantity)
    print(*len_segment)