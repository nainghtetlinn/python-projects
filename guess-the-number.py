import random

print('Welcome to guess the number game!!!')
max_number = input('Type a maximum number: ')

if max_number.isdigit():
    max_number = int(max_number)
    if max_number <= 10:
        print('Please enter a number larger than 10.')
        quit()
else:
    print('Invalid input. Try again.')
    quit()

random_number = random.randint(0, max_number)
guess_count = 0

while True:
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guess_count += 1
    else:
        print('Please enter a number.')
        continue

    if user_guess == random_number:
        print('You guessed it right!!!')
        break
    elif user_guess < random_number:
        print('You were below the number.')
    else:
        print('You were above the number.')

print(f'You got it in {guess_count} guesses.')