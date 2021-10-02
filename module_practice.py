from module2 import Users
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