from login import Login
from admin import call
from signup import sign_up
class greeting:
    def message():
        try:
            value=int(input("\nLogin(1) or Signup(2) "))
            if value ==1:
                print("\nLogin in Patient(1) or Doctor(2) or Admin(3)")
                try:
                    val = int(input("Enter Your Option: "))
                    if val==1:
                        Login.login_(1)
                    elif val == 2:
                        Login.login_(2)
                    elif val==3:
                        print("\n*****WELCOME ADMIN*****")
                        call.admin()
                    else:
                        print(" :( Invalid option:(")
                except ValueError:
                    print(" :( Incorrect value :(")
                    greeting.message()
            elif value == 2:
                sign_up.signup_(1)
            else:
                print(" :( Invalid option :(")
        except ValueError:
            print(" :( Re-run the code :(")
