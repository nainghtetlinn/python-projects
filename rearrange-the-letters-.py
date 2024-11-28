import random
import inquirer

WORDS = "ABCDEFGHJK"

questions = [
  inquirer.List('level',
                message="Choose your move",
                choices=['Easy', 'Hard'],
            ),
]

def gen_words(level):
    if level == 'Easy':
        words = list(WORDS[:5])
    else:
        words = list(WORDS)
    random.shuffle(words)
    return words

def check_ans(ans, correct):
    correct_count = 0
    for i, letter in enumerate(ans):
        if letter == correct[i]:
            correct_count += 1
    return correct_count

def main():
    print("Welcome to letters sorting game!!!")
    level = inquirer.prompt(questions)['level']

    correct_letters = gen_words(level)
    
    for _ in range(10):
        while True:
            ans = input(f'Rearrange {WORDS if level == "Hard" else WORDS[:5]}: ').upper()
            if set(list(ans)) == set(list(correct_letters)):
                break
            else:
                print(f'Invalid input. Please enter letters from {WORDS if level == "Hard" else WORDS[:5]}.')

        result = check_ans(ans, correct_letters)
        
        if result == len(correct_letters):
            print(f"Congraulations! You successfully rearrange the letters {''.join(correct_letters)}.")
            break
        else:
            print(f"\n{result} letters correct.")



if __name__ == '__main__':
    main()