class Facebook:
    username = None
    password = None

    def __init__(self):
        self.username = str(input("Please enter the Username\n"))
        self.password = str(input("Please enter the Password\n"))

    def login(self):
        if self.username == "pavan@gmail"and self.password == "pass@123":
            print("Welcome sir")
        else:
            print("Sorry sir")



login_ref = Facebook()
login_ref.login()

#Password is not secured
print(login_ref.password)

