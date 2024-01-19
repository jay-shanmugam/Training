from Model.authentication import access
from Model.sign_up import signup_
from Model.database import hms_cursor, dbconnect
from View.user_view import display_1
from prettytable import PrettyTable

class call:
    @classmethod
    def ad(cls,prof):
        username=input("\nEnter your username: ").lower()
        password=input("Enter your Password: ")
        try:
            validate=access.verify(username,password,prof)
            call.admin_fun(validate)
        except IndexError:
            display_1.incorrect_value()

    @classmethod
    def admin_fun(cls,val):
        while True:
            if val:
                value = display_1.admin_perform()
                try:
                    if value==1:
                        success = signup_.signup(2)
                        if success == 1:
                            print("\nData updated!")
                            call.admin_fun(1)
                        else:
                            print("\nData not updated")
                            call.admin_fun(1)

                    elif value == 2:
                        username=input("\nEnter Doctor username: ").lower()
                        password=input("Enter password to Delete: ")
                        validate=access.verify(username,password,2)
                        passw=[]
                        passw.append(password)
                        if validate:
                            try:
                                hms_cursor.execute("delete from doctor where passwd = %s",(passw))
                                dbconnect.commit()
                                print("\nData removed from hospital database")
                            except:
                                dbconnect.rollback()
                            call.admin_fun(1)
                        else:
                            print("\nGiven data is not in List")
                            call.admin_fun(1)
                    
                    elif value == 3:
                        print("\n       <<<<<<<<<<<|| You have rights BUT... Sorry ||>>>>>>>>>>>>       ")
                        call.admin_fun(1)
                    
                    elif value == 4:
                        hms_cursor.execute("select * from doctor order by first_name")
                        result = hms_cursor.fetchall()
                        table = PrettyTable(["Name","DOB","Phone Number","username","password","Specialist","Available","Status"])
                        for loop in result:
                            table.add_row([loop[1],loop[4],loop[6],loop[7],loop[8],loop[9],loop[10],loop[11]])
                        print(table)
                        call.admin_fun(1)

                    elif value == 5:
                        hms_cursor.execute("select * from patient order by first_name")
                        result = hms_cursor.fetchall()
                        table = PrettyTable(["Name","DOB","Phone Number","username","password"])
                        for loop in result:
                            table.add_row([loop[1],loop[4],loop[6],loop[7],loop[8]])
                        print(table)
                        call.admin_fun(1)

                    elif value == 6:
                        while True:
                            try:
                                choice=display_1.again_login()
                                if choice == 1:
                                    call.ad(3)
                                elif choice == 2:
                                    print("\n :) :) Come Another Time :) :)\n")
                                    display_1.close()
                                else:
                                    display_1.invalid()
                            except ValueError:
                                display_1.incorrect_value()
                                call.admin_fun(1)

                    else:
                        display_1.incorrect_value()

                except ValueError:
                    display_1.invalid()

            else:
                display_1.incorrect()
                call.ad(3)
