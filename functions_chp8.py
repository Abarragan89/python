# def full_name(first, last, middle=''):
#     """takes first and last names to make a full name"""
#     name = f"{first} {middle} {last}"
#     return name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("enter 'q' to quit")

#     f_name = input("First Name:")
#     if f_name == 'q':
#         break
#     l_name = input("Last Name: ")
#     if l_name == 'q':
#         break

#     proper_name = full_name(f_name, l_name)
#     print(f"\nHello, {proper_name}")


#       Activity 8-6
def dic_builder (artist, album, songs=None):
    artist_info = {'artist': artist, 'album': album, 'number_of_songs': songs}
    return artist_info

# nirvana = dic_builder('nirvana', 'nevermind', 12)
# soad = dic_builder('system of a down', 'hypnotized')
# gday = dic_builder('green day', 'dookie')

# print(f"\nNirvana: \n{nirvana}")
# print(f"\nSystem of a Down: \n{soad}")
# print(f"\nGreen Day: \n{gday}")

# activate = True
# while activate:
    
#     artist = input("\nEnter an artist: ")
#     if artist == 'q':
#         activate = False

#     album = input("\nEnter an album: ")
#     if artist == 'q':
#         activate = False

#     songs = input("\nNumber of songs: ")
#     if artist == 'q':
#         activate = False
        
#     artist_object = dic_builder(artist, album, songs)

#     print(f"\n{artist_object}")

#   Activity 8-9

#   Activity 8-12
# order1= ['lettuce', 'cheese', 'buns']
# def sandwich_types(*toppings):
#     print("Your sandwich will include:")
#     for topping in toppings:
#         print(f"\n-{topping}\n")

# sandwich_types(order1)

#   Activity 8-13
# def user_profile (first, last, **kwargs):
#     kwargs['first_name'] = first.title()
#     kwargs['last_name'] = last.title()
#     return kwargs

# user1 = user_profile('tony', 'barragan', occupation="teacher", age=12, married="yes")

# print(user1)


#       Activity 8-14

def make_car (manufacturer, model, **kwargs ):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car1 = make_car('infinity', 'q40', drivetrain='rwd', mpg='23')
print(car1)