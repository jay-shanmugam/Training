from View.login_view import display
from Controller.login import Login
from Model.sign_up import signup_
from Model.admin import call

class greeting:

    @classmethod
    def message(cls):
        display.greet()
    
        while True:
            try:
                value = display.user_option()
                if value==1:
                    value1 = display.option()
                    try:
                        if value1 ==1:
                            Login.login_(value1)
                        elif value1 ==2:
                            Login.login_(value1)
                        elif value1 == 3:
                            print("\n*****WELCOME ADMIN*****")
                            call.ad(value1)
                        else:
                            display.invalid()
                    except ValueError:
                        display.invalid()
                
                elif value==2:
                    val=signup_.signup(1)
                    if val ==1:
                        Login.login_(1)

                elif value==3:
                    exit()

                else:
                    display.invalid()
            except ValueError:
                display.invalid()
