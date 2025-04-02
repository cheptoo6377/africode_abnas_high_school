class user :
    def __init__(self, name, phone,is_admin= False,is_logged_in= False):
        self.name = name
        self.phone = phone
        self.is_admin = is_admin
        self.is_logged_in = is_logged_in
    def user_role(self):
        if self.is_logged_in and self.is_admin:
            return "dashboard"
        elif not self.is_logged_in:
            return "login page"
        else:
            return "news feed"
user1 = user("ben","8755",is_logged_in=True ,is_admin=False)
user4 = user("enock","66777",is_logged_in=True,is_admin=True)
print(f"{user1.name} redirected to {user1.user_role()}")
print(f"{user4.name} redirected to {user4.user_role()}")

        