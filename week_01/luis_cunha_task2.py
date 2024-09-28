import random


def validateNum():
    """Validate number input from user."""
    while (True):
        user_input = input('Try to guess the number from 1 to 100 => ')
        user_input = user_input.strip().lower()
        if (user_input.isdigit()):
            if (int(user_input) in range(1, 101)):
                return int(user_input)
            else:
                print('Input out of range.')
        else:
            print('Invalid input.')


def pickRandNum():
    """User attempts to guess number from 1 to 100 in illimited attempts."""
    possibilities = range(1, 101)
    correct_num = random.choice(possibilities)
    attempts = 0
    while (True):
        guess = validateNum()
        if (correct_num == guess):
            print(f'You guessed right! The correct number is {guess}!')
            break
        elif (correct_num < guess):
            attempts += 1
            print(f'{guess} is too high! Guess again.' +
                  f"\nYou're guess count: {attempts}\n")
        else:
            attempts += 1
            print(f'{guess} is too low! Guess again.' +
                  f"\nYou're guess count: {attempts}\n")


pickRandNum()
