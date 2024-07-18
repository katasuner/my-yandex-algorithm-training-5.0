def find_repeat_number_distance_k(k, numbers):
    tracking = set()
    for i, num in enumerate(numbers):
        if num in tracking:
            return "YES"
        tracking.add(num)
        if len(tracking) > k:
            tracking.remove(numbers[i - k])
    return "NO"


n, k = map(int, input().split())
number = [int(num) for num in input().split()]

print(find_repeat_number_distance_k(k, number))