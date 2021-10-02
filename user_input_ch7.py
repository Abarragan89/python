# #set counter to zero
# counter = 0
# #set empty object
# person = []

# #array of questions
# questions = ['what is your name? ', 'what is your age ', 'what is your email ']

# #set a while look to ask the questions
# while counter < len(questions):
#     for question in questions:
#         answer = input(question)
#         person.append(answer)
#         counter +=1

# #display information
# print(person)

#   Parrot Program
# message = ''
# while message != 'quit':
#     message = input("Type something and I'll repeat it. \nEnter 'quit' to stop program  ")
#     if message != 'quit':
#         print(message)



# #set the empty array and counter to zero
# counter = 0
# total_price = []

# #determine number of guests
# guest_count = input('How many people will be viewing today?  ')
# guest_count = int(guest_count)

# #loop as many times are there are guests. Add totals according to age
# while counter < guest_count:
#     counter += 1
#     guest = input(f"How old is guest #{counter}?  ") 
#     guest = int(guest)
#     if guest < 3:
#         print("Children under 3 are free!")
#         continue
#     if guest < 12:
#         print("Kids are $10. $10 will be added to your total")
#         total_price.append(10)
#         continue
#     if guest > 12:
#         print("Adult are $15. $15 will be added to your total")
#         total_price.append(15)

# #determine the total and display
# total = sum(total_price)
# print(f"Your total will be ${total}")


#       End of chapter activites
#   7-8 & 7-9
# sandwich_orders = ['meatball', 'pastrami', 'turkey', 'ham', 'pastrami', 'pepperoni', 'pastrami']

# finished_orders = []
# print("The deli has ran out of pastrami")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
    
#     made_sandwich = sandwich_orders.pop()
#     print(f"I made your {made_sandwich} sandwich")
#     finished_orders.append(made_sandwich)

# print("These sandwiches have been made")
# for sandwich in finished_orders:
#     print(sandwich)

#   7-10

dream_vacations = {}
activate = True

while activate:
    name = input("What is your name? (Enter 'quit' to stop) ")
    if name == 'quit':
        activate = False
        break
    response = input("What is your dream vacation?  ")
    dream_vacations[name] = response

print(dream_vacations)