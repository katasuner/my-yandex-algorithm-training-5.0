n, numbers = int(input()), [int(i) for i in input().split()]
result = ''

previous_num = numbers[0]
for i in range(1, n):
    current_num = numbers[i]
    if previous_num % 2 and current_num % 2:
        result += 'x'
        previous_num = 1
    else:
        result += '+'
        previous_num += current_num

print(result)