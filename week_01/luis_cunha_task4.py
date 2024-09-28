import re


def inputHandling(message):
    """Validate user input."""
    flag = 'y'
    result = ''
    pattern = '^[a-zA-z]+[a-zA-Z]+$'
    while (flag == 'y'):
        user_input = input(message)
        if (re.match(pattern, user_input)):
            result = user_input.lower()
            flag = 'n'
        else:
            print('Invalid input.'
                  + '\nEnter only letters or numbers (one word).')
    return result


def getInput(types_arr):
    """Retrieve user input for given array of types."""
    input_arr = [''] * len(types_arr)
    for i in range(0, len(types_arr)):
        input_arr[i] = inputHandling(f'Please insert a {types_arr[i]} => ')
    return input_arr


def flagHandling(message):
    """Make sure flag is either 'y' or 'n'."""
    ret_value = input(message)
    while (ret_value != 'y') and (ret_value != 'n'):
        print("Invalid input. Enter 'y' or 'n'.")
        ret_value = input(message)
    return ret_value


def mainMenu():
    """Allow user to play multiple games of mad lib."""
    welcome_msg = """
    ----------------------------------------
    |                Mad Lib               |
    ----------------------------------------
    """
    input_type = ["Proper noun(person's name)", 'Adjective', 'Color', 'Animal',
                  'Place', 'Adjective', 'Magical Creature(Plural)', 'Adjective',
                  'Magical Creature(Plural)', 'Room in a House', 'Noun(Plural)',
                  'Noun', 'Noun', 'Adjective', 'Noun(Plural)', 'Number',
                  'Measure of time', 'Verb(ending in ing)', 'Adjective', 'Noun']

    print(welcome_msg)
    flag = 'y'
    while (flag == 'y'):
        print("Let's start the game!")
        user_input = getInput(input_type)
        story_template = f"""
        Dear {user_input[0]},
        I am writing to you from a {user_input[1]} castle in an enchanted forest. I found myself here one day after
        going for a ride on a {user_input[2]} {user_input[3]} in the {user_input[4]}. There are
        {user_input[5]} {user_input[6]} and {user_input[7]} {user_input[8]} here! In the
        {user_input[9]} there is a pool full of {user_input[10]}. I fall asleep each night on a {user_input[11]} of
        {user_input[12]} and dream of {user_input[13]} {user_input[14]}. It feels as though I have lived here for
        {user_input[15]} {user_input[16]}. I hope one day you can visit, although the only way to get here now is
        {user_input[17]} on a {user_input[18]} {user_input[19]}!!
        """
        print(story_template)
        flag = flagHandling("Would you like to play another round? ('y' 'n') => ")


mainMenu()
