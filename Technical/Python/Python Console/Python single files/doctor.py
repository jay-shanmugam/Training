class Doctor:
    def welcome():
        while True:
            values=int(input("List of Patients(1) or Logout(2) "))
            if values==1:
                print("\nList of Patients: ")
                f=open("Patient.txt",'r')
                find=f.readlines()
                pat_name=[]
                ph_num=[]
                for i in find:
                    username_password=i.split(' ')
                    pat_name.append(username_password[0])
                    ph_num.append(username_password[3])
                length=len(pat_name)
                print("\nName   ","Phone Number")
                for i in range(length):
                    print(pat_name[i] ,ph_num[i])
                print("\n")
            if values==2:
                print("Thank You Doctor :) :)")
                break
