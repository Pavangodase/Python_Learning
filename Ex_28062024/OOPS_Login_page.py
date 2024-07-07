class Instalogin:
    username = None
    password = None

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self):
        if self.username == "pavan@gmail.com" and self.password == "Pass@123":
            print("Your Welcome Sir")
        else:
            print("Fuck Off Shravan")


login_ref = Instalogin(username = "pavan@gmail.com", password = "Pass@123")
login_ref.login()
login_ref = Instalogin(username = "shravan@gmail.com" , password = "Minal@123")
login_ref.login()

