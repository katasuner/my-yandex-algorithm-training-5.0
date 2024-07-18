G1, G2 = map(int, input().split(':'))
G1_1, G2_2 = map(int, input().split(':'))
n = int(input())

if n == 1:
    total_first, total_second = G1 + G1_1, G2 + G2_2
    if total_first > total_second:
        print(0)
    elif total_first == total_second:
        if G1_1 > G2:
            print(0)
        else:
            print(1)
    else:
        add_point = total_second - total_first
        G1_1 += add_point
        if G1_1 <= G2:
            print(add_point + 1)
        else:
            print(add_point)

else:
    total_first, total_second = G1 + G1_1, G2 + G2_2
    if total_first > total_second:
        print(0)
    elif total_first == total_second:
        if G1 > G2_2:
            print(0)
        elif G1 == G2_2:
            print(1)
        else:
            print(total_second - G2_2 - G1)
    else:
        add_point = total_second - total_first
        if G1 <= G2_2:
            print(add_point + 1)
        else:
            print(add_point)