L, x1, v1, x2, v2 = map(int, input().split())

k = 0
t1 = t2 = -1

if x1 == x2:
    print(f'YES\n{0:.10f}')

elif v1 == 0 and v2 == 0:
    print('NO')

elif v1 == v2:
    t1 = (L * k - x1 - x2) / (v1 + v2)
    while t1 < 0:
        k += 1
        t1 = (L * k - x1 - x2) / (v1 + v2)
    print(f'YES\n{t1:.10f}')

elif v1 == -v2:
    t1 = (L * k - x1 + x2) / (v1 - v2)
    while t1 < 0:
        k += 1
        t1 = (L * k - x1 + x2) / (v1 - v2)
    print(f'YES\n{t1:.10f}')

elif x1 > x2 and (v1 < 0 and v2 >= 0):
    print(f'YES\n{(L * (0) - x1 + x2) / (v1 - v2):.10f}')

elif x1 > x2 and (v1 == 0 and v2 >= 0):
    print(f'YES\n{(L * (1) - x1 - x2) / (v1 + v2):.10f}')



elif x1 < x2 and (v1 <= 0 and v2 >= 0):
    print(f'YES\n{(L * (-1) - x1 + x2) / (v1 - v2):.10f}')

elif x1 < x2 and (v1 >= 0 and v2 < 0):
    print(f'YES\n{(L * (1) - x1 - x2) / (v1 + v2):.10f}')


elif x1 < x2 and (v1 >= 0 and v2 == 0):
    print(f'YES\n{(L * (0) - x1 + x2) / (v1 - v2):.10f}')

elif x1 > x2 and (v1 >= 0 and v2 < 0):
    print(f'YES\n{(L * (-1) - x1 - x2) / (v1 + v2):.10f}')

elif x1 > x2 and (v1 >= 0 and v2 == 0):
    print(f'YES\n{(L * (1) - x1 - x2) / (v1 + v2):.10f}')



elif v1 > v2:
    for k in range(2 * L):
        if t1 < 0:
            t1 = (L * k - x1 - x2) / (v1 + v2)
        if t2 < 0:
            t2 = (L * k - x1 + x2) / (v1 - v2)
        if t1 >= 0 and t2 >= 0:
            print(f'YES\n{min(t1, t2):.10f}')
            break

else:
    for k in range(2 * L):
        t1 = (L * k - x1 - x2) / (v1 + v2)
        t2 = (L * k - x1 + x2) / (v1 - v2)
        if t1 >= 0 and t2 >= 0:
            print(f'YES\n{min(t1, t2):.10f}')
            break
        elif t1 >= 0:
            print(f'YES\n{t1:.10f}')
            break
        elif t2 >= 0:
            print(f'YES\n{t2:.10f}')
            break