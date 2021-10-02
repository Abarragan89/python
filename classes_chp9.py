# #       Activity 9-1 and 9-2 and 9-4
# class Restaurant: 
#     """Creating a simple restaurant"""
#     def __init__(self, name, crusine):
#         self.name = name
#         self.crusine = crusine
#         self.number_served = 0
#     """methods"""
#     def open(self):
#         print(f"{self.name} is open for business")
    
#     def describe_restarurant (self):
#         print(f"{self.name} is a restaurant that serves {self.crusine}")
    
#     def set_number_served(self, served):
#         self.number_served = served
#     def increment_served (self, amount_served):
#         self.number_served += amount_served
# #create olive garden
# food_place1 = Restaurant('olive garden', 'italian')
# print(food_place1.number_served)

# food_place1.set_number_served(3)
# print(food_place1.number_served)

# food_place1.increment_served(80)
# print(food_place1.number_served)


#       Activity 9-1 and 9-2 and 9-4
class Restaurant: 
    """Creating a simple restaurant"""
    def __init__(self, name, crusine):
        self.name = name
        self.crusine = crusine
        self.number_served = 0
    """methods"""
    def open(self):
        print(f"{self.name} is open for business")
    
    def describe_restarurant (self):
        print(f"{self.name} is a restaurant that serves {self.crusine}")
    
    def set_number_served(self, served):
        self.number_served = served
    def increment_served (self, amount_served):
        self.number_served += amount_served


#      Activity 9-3
class Users:
    """Creates user profile"""
    def __init__(self, first, last, occupation):
        self.first = first
        self.last = last
        self.occupation = occupation
        self.login_attempts = 0
    
    def summary(self):
        print(f"{self.first} {self.last} is a {self.occupation}")
    
    def greet_user(self):
        print(f"Hello, {self.first} {self.last}")
    
    def increment_log(self):
        self.login_attempts += 1
    def reset_login_attempts (self):
        self.login_attempts = 0

# clair = Users('clair', 'marshall', 'teacher')
# print(clair.login_attempts)
# clair.increment_log()
# clair.increment_log()
# print(clair.login_attempts)
# clair.reset_login_attempts()
# print(clair.login_attempts                                                                                                                                       )
 
# class IceCreamStand(Restaurant):
#      """Creates ice cream instances"""
#      def __init__(self, name, crusine, flavors):
#         super().__init__(name, crusine)
#         self.flavors = flavors
#         """Loop through flavors to display them. """
#      def display_flavors (self):
#         print(f"These are the flavors we have available:")
#         for flavor in flavors:
#             print(f"\n\t-{flavor}")
    
# flavors = ['chocolate', 'vanilla', 'rocky road', 'strawberry']
# my_shop = IceCreamStand('baskin robbins', 'ice cream', flavors)
# print(my_shop.display_flavors())


#Class of priviledges
class Priviledges:
    def __init__(self):
        self.privileges = ['can ban user','can post', 'can delete post','can start thread']

    def show_privileges(self):
        print("These are our privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")  

#       uses priviledges
class Admin(Users):
    """Creating admin profiles"""
    def __init__(self, first, last, occupation):
        super().__init__(first, last, occupation)
        self.privileges = Priviledges()


from random import choice
"""make list of characters, empty winning ticket and my ticket"""
ticket_options = ['2', 's', '3', 'a', 'l','o','8', '6', 'w', '4' ]
winning_ticket = []
my_ticket = ['s']
"""loop condition and counter set to zero"""
activate = True
counter = 0
print(counter) 

while activate:
    """add one to the coutner"""
    counter += 1
    winning_ticket = []
    """make one ticket"""
    while len(winning_ticket) < 1:
        character = choice(ticket_options)
        winning_ticket.append(character)
        if winning_ticket == my_ticket:
            activate = False
            break

print(counter)





