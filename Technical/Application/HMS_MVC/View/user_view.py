class display_1:
    
    @classmethod
    def admin_perform(cls):
        val=int(input("""\nWant to Perform: \nAdd Doctor(1) or Remove Doctor(2) or Add Admin(3) or View Doctor Details(4) or 
View Patient Details(5) or Logout(6)  """))
        return val
    
    @classmethod
    def doc_perform(cls):
        val=int(input("""\nList of Patients(1) or Change Availability(2) or view appointment(3)
Change Phone number(4) or Change Password(5) or Logout(6) """))
        return val
    
    @classmethod
    def pat_perform(cls):
        val = int(input(("""\nList of doctors(1) or Make Appointment(2) or View Status(3) or Cancel Appointment(4) or 
Change PhoneNumber(5) or Change Password(6) or Logout(7)  """)))
        return val
    
    @classmethod
    def doc_avail_choice(cls):
        val=int(input("\nWant to change availabilty Yes(1) or No(2) "))
        return val
    
    @classmethod
    def again_login(cls):
        val = int(input("\nAgain login(1) or close the page(2) "))
        return val
    
    @classmethod
    def appoint_pat(cls):
        val = int(input("\nWant to slot the patient(1) or cancel the appointment(2) "))
        return val
    
    @classmethod
    def change_phone(cls):
        val = int(input("\nWant to change phone number(1) or Not(2) "))
        return val
    
    @classmethod
    def change_password(cls):
        val = int(input("\nWant to change password(1) or Not(2) "))
        return val
    
    @classmethod
    def last(cls,val):
        if val==1:
            print("\n:) Take Care of Your Health... :)\n")
            return
        elif val==2:
            print("\n:) :) :) Thank You Doctor :) :) :)\n")
            return
    
    @staticmethod
    def valid_phone():
        print("\n!! Give Valid Phone number !!\n")

    @staticmethod
    def correct_date():
        print("\nEnter correct Date")

    @staticmethod
    def cancel_appoint():
        print("\nYou want to cancel appointment to change availability")

    @staticmethod
    def incorrect():
        print("\nEither Username or Password Wrong")
        print("~~Back to Login~\n")

    @staticmethod
    def incorrect_value():
        print("\n :( Enter correct value:(")

    @staticmethod
    def invalid():
        print("\n :( Invalid option:(")

    @staticmethod
    def close():
        exit()