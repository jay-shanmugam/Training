from Model.authentication import access
from View.login_view import display
from Model.patient import Patient
from Model.doctor import Doctor

class Login:

    @classmethod
    def login_(cls,profile):
        username = input("\nEnter your Username: ").lower()
        Password = input('Enter your password: ')

        if(profile==1):
            validate=access.verify(username,Password,profile)
            if(validate):
                display.log_success()
                display.name_print(username)
                Patient.welcome(username,Password)
            else:
                display.incorrect()
                Login.login_(1)

        if(profile==2):
            validate=access.verify(username,Password,profile)
            if(validate):
                display.log_success()
                display.name_print(username)
                Doctor.welcome(username,Password)
            else:
                display.incorrect()
                Login.login_(2)
                
