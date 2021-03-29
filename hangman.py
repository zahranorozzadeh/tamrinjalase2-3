import random

score = 10
true_chars = []

words = ['tree', 'clock', 'apple', 'python', 'cherry', 'android', 'book', 'happy', 'ali', 'kids', 'moon', 'mobile']

word = random.choice(words)

while True:
    for i in range(len(word)):
        if word[i] in true_chars:
            print(word[i], end='')

        else:
         print('-', end = '')

    char = input ('\n please enter a character')

    if char in word:
        true_chars.append(char)

    else:
        score -= 1

    print(score)

    if score == 0 :
        print('game over')
        break

    

    