# filename = 'practice_python/readme.txt'

# with open(filename, 'a') as file:
#     activate = True
#     while activate:
#         name = input(f"Why do you like programming?\n(Enter 'q' to quit) ")
#         if name == 'q':
#             activate = False
#             break
#         file.write(f"{name} visited \n")

def addition ():
    """takes two numbers from user and adds them"""
    print("Choose two numbers and I will add them .")
    """Takes their numbers"""
    try:
        num_1 = input("Enter your first number: ")
        num_1 = int(num_1)
        num_2 = input("Enter your second number number: ")
        num_2 = int(num_2)
    
        """adds the two numbers"""
    
        answer = num_1 + num_2
        print(answer)
    except ValueError:
        pass

active = True
while active:
    addition()


