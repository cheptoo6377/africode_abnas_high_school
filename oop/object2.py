from datetime import date
class user ():
    def __init__(self, username,is_admin = False):
        self.username = username
        self.is_admin = is_admin

        #instance method
    def  get_username(self):
            return self.username
        #class method
    @classmethod#decorator
    def create_admin(cls, username):
            return cls(username, is_admin=True)
# user1 = user("ben")
# print(f"{user1.get_username()} is_admin {user1.is_admin}")
    @classmethod
    def user_age(cls,username, year_of_birth):
        current_year = date.today().year
        age = current_year - year_of_birth
        return cls(username, age)
# user3 = user.user_age("ben", 1990)
# print (f"{user3.get_username()} is {user3.is_admin} and age is {user3.is_admin}")
    @staticmethod
    def is_valid_username( username):
          if len(username) < 5:
                return False  


    @staticmethod
    def add_email(username,email): 
     return f"{username} email is {email}" 
usser5 = user.add_email("ben","rop@gmail")   
print(usser5)        
        