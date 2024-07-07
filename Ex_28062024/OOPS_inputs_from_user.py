class Facebook:
    username = None
    password = None

    #def __init__(self,username,password):
    #    self.username = username
    #    self.password = password

    def login(self):
        username = str(input("Please enter the Username\n"))
        password = str(input("Enter the Password\n"))
        if username == "pavan@gmail"and password == "pass@123":
            print("Welcome sir")
        else:
            print("Sorry sir")



login_ref = Facebook()
login_ref.login()

