import random

WHITE = '\033[97m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
LIGHT_GRAY = '\033[37m'
RESET = '\033[0m'

class Printabel_word:
    def __init__(self, word, correct) :
        self.word = word.upper()
        self.correct = correct.upper()

    def __str__(self) -> str:
        result = ""
        for i, char in enumerate(self.word):
            if char == self.correct[i]:
                result += GREEN + char + RESET
            elif char in self.correct:
                result += YELLOW + char + RESET
            else:
                result += LIGHT_GRAY + char + RESET
        return result

def choose_word():
    with open('wordle-dataset.txt') as f:
        return random.choice(f.read().split(' '))

def main():
    print("Welcome to wordle!!!")
    correct_word = choose_word()
    attempts = []

    for _ in range(5):
        while True:
            guess_word = input("Enter your guess: ")
            if len(guess_word) == 5:
                break
            else:
                print('Invalid input. Please enter a 5-letter word.')
    
        word = Printabel_word(guess_word, correct_word)
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