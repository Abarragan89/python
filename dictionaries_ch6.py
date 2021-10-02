# users = {
#     'anthony.bar.89': {
#         'first': 'anthony',
#         'last': 'barragan',
#         'location': 'woodland hills'
#         },
#     'reesie.barragan': {
#         'first': 'reesie',
#         'last': 'barragan',
#         'location': 'woodland hills'
#         },
#     }
#  #loop to display user information   
# for user, user_info in users.items():
#     #display the username
#     print(f"\nUsername: {user}")

#     #get the full name and location in variables
#     fullname = f"{user_info['first'].title()} {user_info['last'].title()}"
#     location = user_info['location'].title()

#     #print the full name and location
#     print(f"\tFull Name: {fullname}")
#     print(f"\tLocation: {location}")


# #END OF THE CHAPTER ACTIVITIES
#   1st 
# #Create three users
# mcdonald = {
#     'username': 'mcdonald', 
#     'email': 'mcdonald.32@gmail.com',
#     'location': 'los angeles'
#     }

# burger_king = {
#     'username': 'burger king', 
#     'email': 'burger_king.32@gmail.com',
#     'location': 'kentucky'
#     }

# taco_bell = {
#     'username': 'taco bell', 
#     'email': 'taco_bell.32@gmail.com',
#     'location': 'new mexico'
#     }
#  #put users in a dictionary
# all_users = {'user1': mcdonald, 'user2': burger_king, 'user3': taco_bell}
# # print(all_users['user1'])

# for user, user_info in all_users.items():
#     print(f"\nUsername: {user_info['username'].title()}")
#     print(f"\tEmail: {user_info['email']}")
#     print(f"\tLocation: {user_info['location'].title()}")

#   Activity#2
#create empty array
pets = []

#make dictionary of pets
pet1 = {
    'breed': 'chihuahua',
    'owner': 'reesie',
    'name': 'stella',
    }
pet2 = {
    'breed': 'german sheppard',
    'owner': 'brian',
    'name': 'hitler',
    }
pet3 = {
    'breed': 'white labrador',
    'owner': 'reesie',
    'name': 'stella',
    }

#append dictionaries to array
pets.append(pet1)
pets.append(pet2)
pets.append(pet3)

#print info on every
# for pet in pets:    
#     print(f"\n{pet['owner'].title()} has a {pet['breed'].title()} named {pet['name'].title()}\n")

#   Activity#3
# favorite_place = {
#     'reesie': ['tokyo', 'mexico', 'ireland'],
#     'stella': ['dog park', 'outside', "someone's face"],
#     'anthony': ['yellowstone', 'switzerland', 'ireland'],
#     }

# for person, places in favorite_place.items():
#     print(f"\n{person.title()} wants to go to:")
#     for place in places: 
#         print(f"\t{place.title()}")

#   Activity #4
#make dictionary of dictionaries about cities
cities = {
    'los angeles': {
        'country': 'united states',
        'state': 'california',
        'fact': 'has a homeless problem',
        },
    'london': {
        'country': 'England',
        'state': 'united kingdom',
        'fact': 'took over most of the world',
        },
    'new orleans': {
        'country': 'america',
        'state': 'louisiana',
        'fact': 'makes great food',
        }, 
    }
#display the information 
# for city, info in cities.items():
#     print(f"\n{city.title()} is in {info['country'].title()}, {info['state'].title()} and {info['fact']}.\n")

\
