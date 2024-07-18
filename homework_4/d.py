def fill_side(part, w):
    height = 1
    current_width = 0

    for word_len in part:
        if word_len > w:  # Слово не может поместиться на строку вообще
            return float('inf')

        if current_width == 0:  # Первое слово в строке
            current_width = word_len
        elif current_width + word_len + 1 <= w:  # Следующее слово помещается с пробелом
            current_width += word_len + 1
        else:  # Необходим новый ряд
            height += 1
            current_width = word_len

    return height


def find_optimal_split(n, m, a, b, w):
    left, right = 1, w

    while left < right:
        mid = (left + right) // 2

        left_length = fill_side(a, mid)
        right_length = fill_side(b, w - mid)

        if left_length <= right_length:
            right = mid
        else:
            left = mid + 1


    final_left_length = fill_side(a, left)
    final_right_length = fill_side(b, w - left)
    final_length = max(final_left_length, final_right_length)

    if left > 1:
        left_length_minus_one = fill_side(a, left - 1)
        right_length_minus_one = fill_side(b, w - left + 1)
        final_length_minus_one = max(left_length_minus_one, right_length_minus_one)
        final_length = min(final_length, final_length_minus_one)

    return final_length


w, n, m = map(int, input().split())
part_one = list(map(int, input().split()))
part_two = list(map(int, input().split()))

print(find_optimal_split(n, m, part_one, part_two, w))

