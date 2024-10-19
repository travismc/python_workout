# Create a new constant dict, called MENU, representing the possible items you can order at a restaurant. The keys will be strings, and the values will be prices (i.e., integers). You should then write a function, restaurant, that asks the user to enter an order:

# If the user enters the name of a dish on the menu, the program prints the price and the running total. It then asks the user again for their order.
# If the user enters the name of a dish not on the menu, the program scolds the user (mildly). It then asks the user again for their order.
# If the user enters an empty string, the program stops prompting and prints the total amount.

MENU = {'sandwich': 10, 'tea': 7, 'salad': 9, 'soda': 6, 'pie': 8}


def restaurant():
    order = []
    total = []
    if True:
        if (input('Type "y" if you would like to add an item. Otherwise type "n".')) == 'y':
            order.append(
                input(f'What would you like to order? Choices are: {MENU.values}'))
    for item in order:
        total.append(order[item])

    print(f'Your total is {sum(total)}')


restaurant()
