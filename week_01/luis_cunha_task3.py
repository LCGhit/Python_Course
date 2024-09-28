def validateNum(start, end, message):
    """Validate number from range(start, end)."""
    flag = 'y'
    result = ''
    while (flag == 'y'):
        user_input = input(message)
        user_input = user_input.strip().lower()
        if (user_input.isdigit()):
            if (int(user_input) in range(start, end)):
                result = int(user_input)
                flag = 'n'
            else:
                print(f'Out of range. Insert a number from {start} to {end-1}')
        elif (user_input == ''):
            flag = 'n'
        else:
            print('Invalid input. Enter a number, please.')
    return result


def menuPick(some_dict, message):
    """Create menu to return a selected value."""
    for key, value in some_dict.items():
        print(list(some_dict).index(key)+1, key, str(value)+'€')
    print(0, 'Next')
    pick = validateNum(0, len(list(some_dict))+1, message)
    if (pick == '') or (pick == 0):
        return 0
    return some_dict[list(some_dict)[int(pick)-1]]


def createOrder():
    """Pick elements from each menu."""
    menu_appetizer = {'Salad': 3, 'Bruschetta': 3, 'Spiedini': 4,
                      'Focaccia': 4.5}
    menu_entree = {'Carbonara': 22, 'Pizza': 20, 'Rizzoto': 25,
                   'Fettuccine Alfredo': 22}
    menu_drinks = {'Water': 3, 'Sparkling Water': 2.5, 'Red Wine': 11.5,
                   'White Wine': 10, 'Soda': 4}
    appetizer_pick = menuPick(menu_appetizer, 'Pick your appetizer => ')
    entree_pick = menuPick(menu_entree, 'Pick your entree => ')
    drink_pick = menuPick(menu_drinks, 'Pick your drink => ')
    return appetizer_pick + entree_pick + drink_pick


def getTotalBill():
    """Calculate tip, total bill and produce goodbye message accordingly."""
    bill = createOrder()
    print(f'Your bill is {bill}€.')
    tip_percent = validateNum(0, 101,
                              'How much would you like to tip? (default 15%) => ')
    tip_comment = ''
    if (tip_percent == ''):
        tip_percent = 15
        tip_comment = 'Thanks, cheapskate!'
    elif (tip_percent in range(0, 21)):
        tip_comment = 'Thanks, cheapskate!'
    elif (tip_percent in range(21, 40)):
        tip_comment = 'Thank you very much!'
    else:
        tip_comment = "I get it, you're rich."
    tip = (int(tip_percent)/100)*bill
    print(f'You tipped {tip:.2f}€.\nThe bill total is {bill+tip:.2f}€.'
          + f'\n{tip_comment}')


getTotalBill()
