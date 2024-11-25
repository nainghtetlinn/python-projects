import random
import inquirer

moves = ['Rock', 'Paper', 'Scissors']
wins = 0
draws = 0

print('Welcome to rock-paper-scissors game!!!')
rounds = input('Number of rounds: ')

if rounds.isdigit():
    rounds = int(rounds)
    if rounds <= 0:
        print('Please enter a number larger than 0.')
        quit()
else:
    print('Invalid input. Try again.')
    quit()

questions = [
  inquirer.List('move',
                message="Choose your move",
                choices=moves,
            ),
]

def check(player, computer):
    if player == computer:
        return 0
    elif (player == 'Rock' and computer == 'Scissors') or (player == 'Paper' and computer == 'Rock') or (player == 'Scissors' and computer == 'Paper'):
        return 1
    else:
        return -1

for i in range(1, rounds + 1):
    print(f'\n===== Round {i} =====')
    computer = random.choice(moves)
    player = inquirer.prompt(questions)['move']

    print(f"Player: {player} vs Computer: {computer}")
    result = check(player, computer)

    if result == 0:
        print('Draw!')
        draws += 1
    elif result == 1:
        print(f"You win round {i}.")
        wins += 1
    else:
        print(f"You lose round {i}.")

if wins > rounds - wins - draws:
    print(f'You win the game with {wins} wins out of {rounds} rounds!')
else:
    print(f'You lose the game with {wins} wins out of {rounds} rounds!')
    




