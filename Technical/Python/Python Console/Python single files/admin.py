from authentication import Authentication
from signup import sign_up
class call:
    def admin():
        username=input("Enter your username: ").lower()
        password=input("Enter your Password: ")
        try:
            access=Authentication.verify(username,password,"admin.txt")
            val=True
            call.admin_fun(access,val)
        except IndexError:
            print("\n???Enter Correct Values???\n")
    def admin_fun(access,val):
        while val:
            if access:
                value=int(input("\nWant to Perform: \nAdd Doctor(1) delete Doctor(2) or Logout(3)"))
                if value==1:
                    print("Signup for Doctor")
                    first_name=input("Enter Doctor First Name: ").lower()
                    last_name=input("Enter last name: ").lower()
                    initial=input("Enter initial: ").lower()
                    phone_number=input("Enter phone number: ")
                    username=input("Enter Username for Doctor: ").lower()
                    password=input("Enter Password for Doctor: ")
                    role=input("Enter the speciality of Doctor: ")
                    is_there=input("Enter availability yes or no: ")
                    f=open("doctor.txt","a+")
                    f.writelines([first_name," ",last_name," ",initial," ",phone_number," ",username," ",password," ",role," ",is_there,"\n"])
                    f.close()
                    call.admin_fun(1,True)
                if value==2:
                    username=input("Enter Doctor username: ").lower()
                    password=input("Enter password to Delete: ")
                    access=Authentication.verify(username,password,"doctor.txt")
                    if access:
                        f=open("doctor.txt",'r')
                        store=[]
                        store=f.readlines()
                        #print(store)
                        f.close()
                        pass_=[]
                        for j in store:
                            username_=j.split(' ')
                            pass_.append(username_[5])
                        for i in range(len(pass_)):
                            if password == pass_[i]:
                                index=i
                        f=open("doctor.txt",'w')
                        for line in store:
                                if line.strip("") !=store[index]:
                                    f.write(line)
                        f.close()
                        call.admin_fun(1,True)
                    else:
                        print("Given data is not in List")
                        call.admin_fun(1,True)
                if value==3:
                    print(" :) :) Come Another Time :) :)")
                    exit()
                else:
                    print("???Enter valid Option???")
            else:
                print("Either Username or Password Wrong\n")
                print("~~Back to Login~\n")
                call.admin()