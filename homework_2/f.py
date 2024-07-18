def find_max(n, sectors, a, b, k):
    max_win, max_sector, flag = 0, max(sectors), True
    if a <= k and b <= k:
        return sectors[0]

    for v in range(a, b + 1, k):
        if v <= k:
            max_win = max(sectors[0], max_win)
        if v % k == 0:
            L = v // k
            clockwise_index = (L - 1) % n
            counter_clockwise_index = (n - (L - 1)) % n
            max_win = max(max_win, sectors[clockwise_index], sectors[counter_clockwise_index])
            if max_win == max_sector:
                return max_win
        else:
            L = v // k
            clockwise_index = L % n
            counter_clockwise_index = (n - L) % n
            max_win = max(max_win, sectors[clockwise_index], sectors[counter_clockwise_index])
            if max_win == max_sector:
                return max_win
    return max_win

n = int(input())
sectors = [int(i) for i in input().split()]
a, b, k = map(int, input().split())
print(find_max(n, sectors, a, b, k))
