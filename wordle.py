import random

WHITE = '\033[97m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
LIGHT_GRAY = '\033[37m'
RESET = '\033[0m'

class Printable_word:
    def __init__(self, word, correct) :
        self.result = ""
        for i, char in enumerate(word):
            if char == correct[i]:
                self.result += GREEN + char + RESET
            elif char in correct:
                self.result += YELLOW + char + RESET
            else:
                self.result += LIGHT_GRAY + char + RESET

    def __str__(self) -> str:
        return self.result

def choose_word():
    with open('wordle-dataset.txt') as f:
        return random.choice(f.read().split(' '))

def main():
    print("Welcome to wordle!!!")
    correct_word = choose_word()
    attempts = []

    for _ in range(10):
        while True:
            guess_word = input("Enter your guess: ")
            if len(guess_word) == 5:
                break
            else:
                print('Invalid input. Please enter a 5-letter word.')
    
        word = Printable_word(guess_word.upper(), correct_word.upper())
        attempts.append(word)

        print()
        for i, attempt in enumerate(attempts):
            print(f"Try {i + 1}: {attempt}")

        if guess_word == correct_word:
            print(f"Congratulations! You guessed the word {correct_word.upper()} in {len(attempts)} attempts.")
            break

    else:
        print('\nGame Over!!! Try again. The correct word was: ' + correct_word.upper())

if __name__ == '__main__':
    main()