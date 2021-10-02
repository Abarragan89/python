#Class of priviledges
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