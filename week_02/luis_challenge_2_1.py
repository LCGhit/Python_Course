"""Game of Rock, Paper, Scissors."""
import random


def mainFunc():
    """Call main menu."""
    score = {'Player': 0, 'Computer:': 0}
    choices = ['Rock', 'Paper', 'Scissor']
    computer_choice = ''
    flag = 'y'
    while (flag == 'y'):
        computer_choice = random.choice(choices)
        player_choice = input(validateInput(choices))
        determine_winner


def validateInput(choices_array):
    """Validate user input according to available choices."""
    flag = 'y'
    clean_input = ''
    while (flag == 'y'):
        clean_input = input('Pick one: ' + ', '.join(choices_array) + ' => ')
        if (clean_input.strip().capitalize() in choices_array):
            flag = 'n'
        else:
            print('You must pick one of the options: ')
            for item in choices_array:
                print(item)
    return clean_input


def determine_winner(pick_a, pick_b):


if __name__ == '__main__':
    mainFunc()
