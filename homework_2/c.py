N, lenghts = int(input()), tuple(int(num) for num in input().split())
find_max = max(lenghts)
find_sum_other = count = 0
find_sum_other = sum(lenghts) - find_max

if len(lenghts) == 2 and lenghts[0] == lenghts[1]:
    print(find_max * 2)

elif find_sum_other == 0:
    print(sum(lenghts))

elif find_max == find_sum_other:
    print(find_max * 2)

elif find_max > find_sum_other:
    print(find_max - find_sum_other)
    
else:
    print(find_max + find_sum_other)