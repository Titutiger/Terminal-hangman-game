import random
import time
import nltk
from nltk.corpus import words


nltk.download('words')

count = 0

letters = []
correct_ans = []
tries = []

random_ = words.words()
random_word = random.choice(random_)

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

def hangman_4():
    print(' |-------|\n'
          ' |       |\n'
          ' O       |\n'
         "/|\\      |\n"
          '         |\n'
         '          |\n'
          '         |\n'
        '____________\n')

def hangman_5():
    print(' |-------|\n'
          ' |       |\n'
          ' O       |\n'
         "/|        |\n"
          '         |\n'
         '          |\n'
          '         |\n'
        '____________\n')

def hangman_6():
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

def hangman_7():
    print(' |-------|\n'
          ' |       |\n'
          ' O       |\n'
         "          |\n"
          '         |\n'
         '          |\n'
          '         |\n'
        '____________\n')

def hangman_8_dead():
    print(' |-------|\n'
          ' |       |\n'
          ' X       |\n'
         "          |\n"
          '         |\n'
         '          |\n'
          '         |\n'
        '____________\n')

print('The word is:')
time.sleep(2)

for dash in range(count):
    print('_', end='  ')

for i in range(2):
    print()

time.sleep(3)
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
        if guess not in tries:
            tries.append(guess)
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
                hangman_8_dead()

                print(f'GAME OVER! The correct word was: {random_word}')
                time.sleep(1)
                stopping = input(': ')

                if stopping:
                    running = False

            else:
                print(f'Something went wrong...')
                running = False

        else:
            print(f'You have already guessed - {guess}')



