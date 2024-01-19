class Patient:
    def welcome():
        while True:
            option=int(input(("View doctors(1) or Logout(2) ")))
            if option==1:
                print("List of Doctors: \n")
                f=open("doctor.txt",'r')
                find=f.readlines()
                doc_name=[]
                ph_num=[]
                role=[]
                for i in find:
                    username_password=i.split(' ')
                    doc_name.append(username_password[0])
                    ph_num.append(username_password[3])
                    role.append(username_password[6])
                    role=[s.replace('\n','') for s in role]
                length=len(doc_name)
                print("Name   ","Phone Number","Speciality\n")
                for i in range(length):
                    print(doc_name[i] ,ph_num[i] ,role[i])
                print("\n")
            elif option==3:
                appoint=int(input(("Want to make Appointment(1) or not(0)")))
                if appoint:
                    pass
            elif option==2:
                print("\n:) Take Care of Your Health... :)")
                break
            else:
                print("\n:( Enter Valid Option :(")