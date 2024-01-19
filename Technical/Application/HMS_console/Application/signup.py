import re
from login import Login
passcheck= r'^[a-z to A-Z to 0-9]+[!@#$%^&*()_+]?\w{2,3}$'
class sign_up:
    def signup_(value):
        if value == 1:
            print("\n:) :)Welcome To Sign Up page for Patient :) :)")
            first_name=input("Enter your First Name: ").lower()
            last_name=input("Enter your last name: ").lower()
            initial=input("Enter your initial: ").lower()
            phone_number=int(input("Enter your phone number: "))
            username=input("Enter your username: ").lower()
            password=input("Enter your password: ")
            f=open("patient.txt","a+")
            if phone_number>6000000000 and 9999999999>phone_number:
                phone_number=str(phone_number)
                if re.search(passcheck,password) and len(password)>=8:
                    f.writelines([first_name," ",last_name," ",initial," ",phone_number," ",username," ",password,"\n"])
                else:
                    print("Use Caps(1), small(1), number(1), Special Char(1/2), Must be in 8 Char")
                    print("!! Enter Strong password !!")
                    sign_up.signup_(1)   
            else:
                print("!! Enter Valid Phone number !!")
                sign_up.signup_(1)
            f.close()
            print("\n:) Login :)")
            Login.login_(1)
        if value ==2:
            pass