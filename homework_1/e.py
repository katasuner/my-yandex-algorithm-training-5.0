n, k, d = map(int, input().split())
change = False
count_days = 0

for day in range(d):
    if int(n) % k == 0 or k == 1:
        n = f'{n}{'0' * (d - count_days)}'
        change = True
        break
    for num in range(10):
        new = f'{n}{num}'
        if int(new) % k == 0:
            count_days += 1
            change = True
            n = new
            break

print(n if change else -1)