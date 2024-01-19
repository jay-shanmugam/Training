class display:

    @staticmethod
    def greet():
        print("\n*******Welcome To Hospital*******")

    @classmethod
    def user_option(clas):
        value1=int(input("\nLogin(1) or Signup only for Patient(2) or Logout(3) "))
        return value1
    
    @classmethod
    def option(cls):
        print("\nLogin as Patient(1) or Doctor(2) or Admin(3)")
        val = int(input("Enter Your Option: "))
        return val
    
    @staticmethod
    def log_success():
        print("\n/*/*/*/*Login Successfull*/*/*/*/")

    @classmethod
    def name_print(cls,name):
        print(f"\n:) :) welcome {name} :) :)\n")

    @staticmethod
    def incorrect():
        print("\nEither Username or Password Wrong")
        print("~~Back to Login~\n")

    @staticmethod
    def invalid():
        print("\n :( Invalid option:(")
    