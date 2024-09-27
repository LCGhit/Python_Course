"""Addition, subtraction, multiplication and division calculator."""


def additionFunc(num_1, num_2):
    """Addition operation."""
    return num_1 + num_2


def subtractionFunc(num_1, num_2):
    """Subtraction operation."""
    return num_1 - num_2


def multiplicationFunc(num_1, num_2):
    """Multiplication operation."""
    return num_1 * num_2


def divisionFunc(num_1, num_2):
    """Division operation. Error if divided by 0."""
    if (num_2 == 0):
        print('Cannot divide by 0')
        return num_1
    else:
        return num_1 / num_2


def validateNum():
    """Validate number input from user."""
    flag = 'y'
    picked_opt = ''
    while (flag == 'y'):
        user_input = input("Enter a number ('q'->quit | 'c'->clean) => ")
        user_input = user_input.strip().lower()
        if (user_input.isdigit()):
            flag = 'n'
            picked_opt = int(user_input)
        elif (user_input == 'q'):
            flag = 'n'
            picked_opt = 'q'
        elif (user_input == 'c'):
            flag = 'n'
            picked_opt = 'c'
        else:
            print('Invalid input. Please enter a number' +
                  " ('q'->quit | 'c'->clean) => ")
    return picked_opt


def validateOp():
    """Validate operation input from user."""
    flag = 'y'
    picked_opt = ''
    op_input_msg = "Enter an operator + - * / ('q'->quit | 'c'->clean) => "
    valid_operations = ['+', '-', '*', '/']
    while (flag == 'y'):
        user_input = input(op_input_msg)
        user_input = user_input.strip()
        if (user_input in valid_operations):
            flag = 'n'
            picked_opt = user_input
        elif (user_input == 'q'):
            flag = 'n'
            picked_opt = 'q'
        elif (user_input == 'c'):
            flag = 'n'
            picked_opt = 'c'
        else:
            print('Invalid input. ' + op_input_msg)
    return picked_opt


def mainMenu():
    """Menu to make calculations."""
    starting_message = """
    ----------------------------------------
    |          Simple Calculator           |
    ----------------------------------------
        Just like your pocket calculator
    """
    goodbye_message = """
    \n----------See you soon!----------\n
    """

    print(starting_message)
    current_total = 0
    current_operation = ''
    while (True):
        if (current_total == 0):
            current_total = validateNum()
            if (current_total == 'q'):
                print(goodbye_message)
                return
            elif (current_total == 'c'):
                current_total = 0
                print('SCREEN:', current_total, '\n')
        current_operation = validateOp()
        if (current_operation == 'q'):
            print(goodbye_message)
            return
        elif (current_operation == 'c'):
            current_total = 0
            print('SCREEN:', current_total, '\n')
            continue
        print('SCREEN:', current_total, current_operation, '\n')
        new_value = validateNum()
        if (new_value == 'q'):
            print(goodbye_message)
            return
        elif (new_value == 'c'):
            current_total = 0
            print('SCREEN:', current_total, '\n')
            continue
        match(current_operation):
            case '+':
                current_total = additionFunc(current_total, new_value)
            case '-':
                current_total = subtractionFunc(current_total, new_value)
            case '*':
                current_total = multiplicationFunc(current_total,
                                                   new_value)
            case '/':
                current_total = divisionFunc(current_total, new_value)
        print('SCREEN:', current_total, '\n')


mainMenu()
