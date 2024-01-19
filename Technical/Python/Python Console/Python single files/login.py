from authentication import Authentication
from patient import Patient
from doctor import Doctor
class Login:
    def login_(profile):
        username = input("Enter your Username: ").lower()
        Password = input("Enter your password: ")
        if(profile==1):
            access=Authentication.verify(username,Password,"patient.txt")
            if(access):
                print("\n/*/*/*/*Login Successfull*/*/*/*/")
                print(f":) :) welcome {username} :) :)")
                Patient.welcome()
            else:
                print(" :( Enter Correct Values :(")
                Login.login_(1)
        if(profile==2):
            access=Authentication.verify(username,Password,"doctor.txt")
            if(access):
                print("\n/*/*/*/*Login Successfull*/*/*/*/")
                print(f"\n:) :) welcome {username} :) :)")
                Doctor.welcome()
            else:
                print(" :| Enter Correct Values :|")
                Login.login_(2)