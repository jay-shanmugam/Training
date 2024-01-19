from Model.database import hms_cursor, dbconnect
from View.user_view import display_1
import re
passcheck= ("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+]).{8,17}$")

class signup_:

    @classmethod
    def signup(cls,check):
        user_: str =''
        if check==1:
            user_= "patient"
        elif check==2:
            user_= "doctor"
        print(f"\n:) :) Welcome To Sign Up page of {user_} :) :)")
        first_name=input("Enter your First Name: ").capitalize()
        last_name=input("Enter your last name: ").capitalize()
        initial=input("Enter your initial: ").upper()
        loop_=1
        while loop_:
            DOB=input("Enter your DOB(ex: DD-MM-YYYY): ")
            if len(DOB)==10:
                loop=1
                while loop:
                    age=int(input("Enter your age: "))
                    if age<100 and age>0:
                        loop=0
                    else:
                        print("Enter correct age")
                loop_=0
            else:
                print("Enter correct DOB")
        loop=1
        while loop:
            phone_number=int(input("Enter your phone number: "))
            if phone_number>6000000000 and 9999999999>phone_number:
                hms_cursor.execute("select username from %s"%user_)
                result=hms_cursor.fetchall()
                if len(result)==0:
                    user=input("Enter your username: ").lower()
                    while loop:
                        password=input("Enter your password: ")
                        if re.search(passcheck,password):
                            loop=0
                        else:
                            signup_.strong_pass()
                else:
                    for loop in result:
                        val_=1
                        while val_:
                            user=input("Enter your username: ").lower()
                            if user!=loop[0]:
                                loop=1
                                while loop:
                                    password=input("Enter your password: ")
                                    if re.search(passcheck,password):
                                        loop=0
                                    else:
                                        change_.strong_pass()
                                val_=0
                            else:
                                print("\nAlready taken.. Enter another username..")
                        break
                loop=0
            else:
                print("!! Give Valid Phone number !!")

        if check ==1:
            sql = "insert into patient(first_name, last_name, initial, DOB, age, phone_number, username, passwd) values (%s, %s, %s, %s, %s, %s, %s,%s)"
            val=(first_name,last_name,initial,DOB,str(age),str(phone_number),str(user),str(password))
        
            try:
                hms_cursor.execute(sql,val)
                dbconnect.commit()
            except:
                dbconnect.rollback()
            print("\nData updated!")
            return 

        if check ==2:
            specialist=input("Enter the speciality of Doctor: ").upper()
            available=input("Enter availability (ex: yes or no): ").upper()
            status=input("Enter status (ex: occupied or unoccupied): ").lower()
            sql = "insert into doctor(first_name, last_name, initial, DOB, age, phone_number, username, passwd, specialist, available, status_) values (%s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s)"
            val=(first_name,last_name,initial,DOB,str(age),str(phone_number),str(user),str(password),specialist,available,status)
        
            try:
                hms_cursor.execute(sql,val)
                dbconnect.commit()
                return 1
            except:
                dbconnect.rollback()
                return 0
            
class change_:

    @staticmethod
    def strong_pass():
        print("\nUse Caps(1), small(1), number(1), Special Char(1), More than 8 Char")
        print("!! Enter Strong password !!\n")

    @classmethod
    def change_phonenumber(cla,check,password1):
        if check==1:
            name="doctor"
        elif check==2:
            name="patient"
        while True:
            option=display_1.change_phone()
            if option == 1:
                while True:
                    pho=[]
                    hms_cursor.execute("select phone_number from %s"%name)
                    result=hms_cursor.fetchall()
                    for row in result:
                        pho.append(row[0])
                    username_flag=False
                    old_phone=int(input("Enter old Phone number to change: "))
                    old_phone=str(old_phone)
                    for i in pho:
                        if old_phone==i:
                            username_flag=True
                    if username_flag:
                        while True:
                            phone=int(input("\nEnter New number: "))
                            if phone>6000000000 and 9999999999>phone:
                                phone=(phone)
                                if check==1:
                                    hms_cursor.execute("update Doctor set phone_number = %s where passwd=%s",(phone,password1))
                                    dbconnect.commit()
                                    return 1
                                elif check ==2:
                                    hms_cursor.execute("update patient set phone_number = %s where passwd=%s",(phone,password1))
                                    dbconnect.commit()
                                    return 1
                            else:
                                print("\n!! Give Valid Phone number !!\n")
                    else:
                        print("\nEnter correct Number")
            elif option ==2:
                print("Great!!! ")
                return 0
            else:
                display_1.invalid()
    
    @classmethod
    def change_password(cls,check,pass_check):
        if check==1:
            name="doctor"
        elif check==2:
            name="patient"
        while True:
            choice=int(input("\nWant to change password(1) or Not(2) "))
            if choice==1:
                while True:
                    pho=[]
                    pas=[]
                    hms_cursor.execute("select phone_number,passwd from %s"%name)
                    result = hms_cursor.fetchall()
                    for row in result:
                        pho.append(row[0])
                        pas.append(row[1])
                    phone_flag=False
                    password_flag=False
                    phon=int(input("Enter Phone number to change password: "))
                    passw=input("Enter old Password: ")
                    phon=str(phon)
                    for i in pho:
                        if phon==i:
                            phone_flag=True
                    for i in pas:
                        if pass_check==i:
                            password_flag=True
                    if phone_flag:
                        if password_flag:
                            while True:
                                password=input("\nEnter New password: ")
                                if re.search(passcheck,password):
                                    password=str(password)
                                    if check==1:
                                        hms_cursor.execute("update doctor set passwd =%s where phone_number=%s ",(password,phon))
                                        dbconnect.commit()
                                        return 1
                                    elif check ==2:
                                        hms_cursor.execute("update patient set passwd =%s where phone_number=%s ",(password,phon))
                                        dbconnect.commit()
                                        return 1
                                else:
                                    change_.strong_pass()
                        else:
                            print("Enter Correct Old Password to change New Password")
                    else:
                        print("Enter Correct Phone number to change Password")
            elif choice ==2:
                print("Great!!! ")
                return 0
            else:
                display_1.invalid()