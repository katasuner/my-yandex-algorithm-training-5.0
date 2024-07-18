dictionary = {key: key for key in sorted(input().split(), key=len)}
text = input().split()

for word in text:
    char = 0
    len_word = len(word)
    while char <= 101 and char < len_word:
        contraction = word[0:char + 1]
        if contraction in dictionary:
            print(dictionary[contraction], end=' ')
            break
        char += 1
    else:
        print(word, end=' ')