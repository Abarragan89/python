from random import choice
"""make list of characters, empty winning ticket and my ticket"""
ticket_options = ['2', 's', '3', 'a', 'l','o','8', '6', 'w', '4' ]
winning_ticket = []
my_ticket = ['s', '3']
"""loop condition and counter set to zero"""
activate = True
counter = 0
print(counter) 

while activate:
    """add one to the coutner"""
    counter += 1
    winning_ticket = []
    """make one ticket"""
    while len(winning_ticket) < 2:
        character = choice(ticket_options)
        winning_ticket.append(character)
        if winning_ticket == my_ticket:
            activate = False
            break

print(counter)