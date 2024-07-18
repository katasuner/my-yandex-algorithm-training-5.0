first_word, second_word = {}, {}

for char in (input()):
    first_word[char] = first_word.get(char, 0) + 1
for char in (input()):
    second_word[char] = second_word.get(char, 0) + 1

print('YES' if first_word == second_word else 'NO')
