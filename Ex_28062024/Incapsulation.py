class Facebook:
    #username = None
    #password = None

    def __init__(self):
        self.__username = str(input("Please enter the Username\n"))
        self.__password = str(input("Please enter the Password\n"))

    def login(self):
        if self.__username == "pavan@gmail"and self.__password == "pass@123":
            print("Welcome sir")
        else:
            print("Sorry sir")



login_ref = Facebook()
login_ref.login()



#Password is  secured
#print(login_ref.__password)

