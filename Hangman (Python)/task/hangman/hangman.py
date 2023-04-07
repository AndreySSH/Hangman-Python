import random
import string

from hangman_ascii import HANGMAN

select = ''
wins = 0
losts = 0

WORDS = ('python', 'java', 'swift', 'javascript')


def game() -> str:
    word = random.choice(WORDS)
    word_hidden = '-' * (len(word))
    attempts = 8
    all_letters = []

    while True:
        while True:
            print()
            print(word_hidden)

            letter = input(f'Input a letter: > ')
            print(letter)
            if len(letter) != 1:
                print('Please, input a single letter.')
            elif letter in string.ascii_lowercase:
                if letter in all_letters:
                    print("You've already guessed this letter.")
                else:
                    break
            else:
                print('Please, enter a lowercase letter from the English alphabet.')

        all_letters.append(letter)

        if letter in word:
            index = -1
            while True:
                try:
                    index = word.index(letter, index + 1)
                except ValueError:
                    break
                else:
                    word_hidden = word_hidden[0:index] + letter + word_hidden[index+1:]
        else:
            print("That letter doesn't appear in the word.")
            attempts -= 1

        if word == word_hidden:
            print(f'You guessed the word {word}!')
            print('You survived!')
            return 'win'

        if attempts < 8:
            print()
            print(HANGMAN[attempts])

        if attempts == 0:
            print('\nYou lost!')
            return 'lost'


if __name__ == '__main__':
    print('H A N G M A N')
    while True:
        select = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > ')
        if select == 'exit':
            break
        elif select == 'results':
            print(f'You won: {wins} times.')
            print(f'You lost: {losts} times.')
        elif select == 'play':
            result = game()
            if result == 'win':
                wins += 1
            elif result == 'lost':
                losts += 1
        else:
            pass
