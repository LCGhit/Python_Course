"""Game of Rock, Paper, Scissors."""
import random


def mainFunc():
    """Call main menu."""
    score = {'Player': 0, 'Computer': 0, 'Ties': 0}
    choices = ['Rock', 'Paper', 'Scissor']
    computer_choice = ''
    flag = 'y'

    while (flag == 'y'):
        computer_choice = random.choice(choices)
        player_choice = validateInput(choices)
        round_outcome = determine_winner(player_choice, computer_choice)
        print('RESULT: \nComputer: ', computer_choice,
              '\nPlayer: ', player_choice, '\n')
        print(f'rount outcome: {round_outcome}')
        if (round_outcome == player_choice):
            score['Player'] += 1
        elif (round_outcome == computer_choice):
            score['Computer'] += 1
        else:
            score['Ties'] += 1
        print(f"SCORE: \nPlayer: {score['Player']} \n"
              + f"Computer: {score['Computer']}\n"
              + f"Ties: {score['Ties']}\n")
        print('Would you like to play another round?')
        flag = validateInput(['Y', 'N']).lower()

    if (score['Player'] > score['Computer']):
        print('Congratulations, you won!')
    elif (score['Computer'] > score['Player']):
        print('The computer wins. Better luck next time!')
    else:
        print('Tie. Could be worse!')


def validateInput(choices_array):
    """Validate user input according to available choices."""
    flag = 'y'
    clean_input = ''
    while (flag == 'y'):
        clean_input = input('Pick one: ' + ', '.join(choices_array)
                            + ' => ').strip().capitalize()
        if (clean_input in choices_array):
            flag = 'n'
        else:
            print('You must pick one of the options: ')
            for item in choices_array:
                print(item)
    return clean_input


def determine_winner(pick_a, pick_b):
    """Return winning value."""
    if ((pick_a == 'Rock' and pick_b == 'Scissor') or (pick_a == 'Scissor'
                                                       and pick_b == 'Rock')):
        return 'Rock'
    elif ((pick_a == 'Rock' and pick_b == 'Paper')
          or (pick_a == 'Paper' and pick_b == 'Rock')):
        return 'Paper'
    else:
        return 'Scissor'


if __name__ == '__main__':
    mainFunc()
