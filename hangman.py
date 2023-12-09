import random
import time
#import pyinstaller
words = ['mockingbird', 'encore', 'epiphany', 'advisory', 'melody', 'beauty', 'landscape', 'concert', 'performance']
letters = []
correct_ans = []
count = 0
random_word = random.choice(words)
for letter in random_word:
    letters.append(letter)
    count += 1
def hangman_1():
    print(' |-------|\n'
          ' |       |\n'
          ' O       |\n'
         "/|\\      |\n"
          ' |       |\n'
         '/\\       |\n'
          '         |\n'
        '____________\n')
def hangman_2():
    print(' |-------|\n'
          ' |       |\n'
          ' O       |\n'
         "/|\\      |\n"
          ' |       |\n'
         '/         |\n'
          '         |\n'
        '____________\n')
def hangman_3():
    print(' |-------|\n'
          ' |       |\n'
          ' O       |\n'
         "/|\\      |\n"
          ' |       |\n'
         '          |\n'
          '         |\n'
        '____________\n')
def hangman_3():
    print(' |-------|\n'
          ' |       |\n'
          ' O       |\n'
         "/|\\      |\n"
          '         |\n'
         '          |\n'
          '         |\n'
        '____________\n')
def hangman_4():
    print(' |-------|\n'
          ' |       |\n'
          ' O       |\n'
         "/|        |\n"
          '         |\n'
         '          |\n'
          '         |\n'
        '____________\n')
def hangman_5():
    print(' |-------|\n'
          ' |       |\n'
          ' O       |\n'
         " |        |\n"
          '         |\n'
         '          |\n'
          '         |\n'
        '____________\n')
    time.sleep(0.5)
    print("He's almost dead...")
    time.sleep(1)
def hangman_6():
    print(' |-------|\n'
          ' |       |\n'
          ' O       |\n'
         "          |\n"
          '         |\n'
         '          |\n'
          '         |\n'
        '____________\n')
def hangman_7_dead():
    print(' |-------|\n'
          ' |       |\n'
          ' X       |\n'
         "          |\n"
          '         |\n'
         '          |\n'
          '         |\n'
        '____________\n')
print('The word is:')
time.sleep(1)
for dash in range(count):
    print('_', end='  ')
for i in range(2):
    print()
time.sleep(1)
hangman_1()
hangman_state = 0
running = True
while running:
    guess = str(input('Enter you letter or guess: ')).lower()
    if guess in letters:
        time.sleep(0.5)
        print(f'Yes...{guess} is there in the word!')
        if guess not in correct_ans:
            correct_ans.append(guess)
        print(correct_ans)
    elif guess == random_word:
        time.sleep(0.5)
        print(f'Yes!! you got it correct! The word is {random_word}')
        running = False
    else:
        print('Try again! D;')
        hangman_state += 1
        if hangman_state == 1:
            for i in range(2):
                print()
            time.sleep(0.5)
            hangman_2()
            print(correct_ans)
        elif hangman_state == 2:
            for i in range(2):
                print()
            time.sleep(0.5)
            hangman_3()
            print(correct_ans)
        elif hangman_state == 3:
            for i in range(2):
                print()
            time.sleep(0.5)
            hangman_4()
            print(correct_ans)
        elif hangman_state == 4:
            for i in range(2):
                print()
            time.sleep(0.5)
            hangman_5()
            print(correct_ans)
        elif hangman_state == 5:
            for i in range(2):
                print()
            time.sleep(0.5)
            hangman_6()
            print(correct_ans)
        elif hangman_state == 6:
            for i in range(2):
                print()
            time.sleep(0.5)
            hangman_7_dead()
            print(f'ERROR!?!: GAME OVER, the correct word was: {random_word}')
            time.sleep(1)
            print('This Instance is closing in 10s')
            time.sleep(10)
            stopping = input(': ')
            if stopping:
                running = False
        else:
            print(f'Something went wrong...')
            running = False


