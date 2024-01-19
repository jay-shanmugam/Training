from Model.database import hms_cursor, dbconnect
from View.user_view import display_1
from Model.sign_up import change_

from prettytable import PrettyTable
import datetime

class Patient:
    @classmethod
    def welcome(cls,username,password):
        hms_cursor.execute("select date_,time_,view_status,reason from patient where username=%s",([username]))
        pat_date=hms_cursor.fetchall()
        date=[]
        time=[]
        for loop in pat_date:
            date.append(loop[0])
            time.append(loop[1])
        pat_date_=str(''.join(date))
        pat_time=str(''.join(time))
        try:
            if pat_date!="null" and pat_time!="null":
                pat_=pat_date_ +" " +pat_time
                dat_ = datetime.datetime.strptime(pat_, "%Y-%m-%d %H:%M")
                today = datetime.datetime.now()
                if dat_<today:
                    pat_reason=str("null")
                    p_status=str("null")
                    p_date=str("null")
                    p_time=str("null")
                    hms_cursor.execute("update patient set reason=%s,view_status=%s,date_=%s,time_=%s where username=%s",(pat_reason,p_status,p_date,p_time,username))
                    dbconnect.commit()
        except:
            dbconnect.rollback()

        while True:
            option = display_1.pat_perform()
            if option==1:
                hms_cursor.execute("select first_name,phone_number,specialist,available from Doctor order by first_name")
                result = hms_cursor.fetchall()
                table = PrettyTable(["Name","Phone Number","Specialist","Availability"])
                for loop in result:
                    table.add_row([loop[0],loop[1],loop[2],loop[3]])
                print(table)

            elif option== 2:
                hms_cursor.execute("select view_status,reason from patient where username=%s",([username]))
                check=hms_cursor.fetchall()
                for loop in check:
                    check2=loop[0]
                    check3=loop[1]
                if ((check2=="not" or check2=="null") and (check3=="none" or check3=="not" or check3=="null")):
                    if check2!="pending":
                        hms_cursor.execute("select view_appointment from doctor")
                        check_=hms_cursor.fetchall()
                        for cir_ in check_:
                            if username==cir_[0]:
                                print("You already having appointment with other doctor")
                                Patient.welcome(username,password)
                            else:
                                Patient.make_appoint(username,password)
                    else:
                        print("\nYour appointment is pending with other doctor")
                else:
                    print("\nFirst cancel your appointment to make with other")
            
            elif option== 3:
                hms_cursor.execute("select reason,view_status,date_,time_ from patient where username=%s",([username]))
                view=hms_cursor.fetchall()
                for loop in view:
                    reason_=loop[0]
                    status=loop[1]
                    date=loop[2]
                    time=loop[3]
                if status=="accepted":
                    print(f"""\nYour having appoinment on 
DATE : {date}
TIME : {time}""")
                elif status=="not":
                    print("\nYour appointment get cancelled !!!")
                    print("\nYou can make another Appointment ")
                    Patient.welcome(username,password)
                elif status=="pending":
                    print("\nYour appointment is Still Pending")
                    Patient.welcome(username,password)
                elif (reason_=="null" or reason_=="none") and status =="null":
                    print("\nYou have to make appointment First")
                    Patient.welcome(username,password)
            
            elif option==4:
                hms_cursor.execute("select username,view_appointment from doctor")
                check_=hms_cursor.fetchall()
                can_=int(input("Confirm to cancel(1) or not(2) "))
                if can_==1:
                    for cir_ in check_:
                        if username==cir_[1]:
                            reason_=str("null")
                            d_=str("null")
                            t_=str("null")
                            pat_sta=str("null")
                            doc_sta=str("unoccupied")
                            doc_app=str("no_patient")
                            doc_name=str(cir_[0])
                            hms_cursor.execute("update patient set reason=%s,view_status=%s,date_=%s,time_=%s where username=%s",(reason_,pat_sta,d_,t_,username))
                            hms_cursor.execute("update doctor set view_appointment=%s,status_=%s where first_name=%s",(doc_app,doc_sta,doc_name))
                            dbconnect.commit()
                            print("Your appointment successfully cancelled...")
                            Patient.welcome(username,password)
                    print("\nYou have to make appointment first!!")
                else:
                    Patient.welcome(username,password)

            elif option==5:
                change_phone = change_.change_phonenumber(2,password)
                if change_phone==1:
                    print("\n!!!Phone Number Updated!!!")
                    Patient.welcome(username,password)
            
            elif option == 6:
                change_password=change_.change_password(2,password)
                if change_password==1:
                    print("\n!!!New Password Updated!!!")
                    Patient.welcome(username,password)

            elif option == 7:
                while True:
                    valu_=display_1.again_login()
                    if valu_==1:
                        Patient.welcome(username,password)
                    elif valu_==2:
                        display_1.last(1)
                        break
                    else:
                        display_1.incorrect_value()
                display_1.close()
            else:
                display_1.invalid()

    @classmethod
    def make_appoint(cls,user_name,password_):
        while True:
            print("""\nThese are the Specialist in our hospital: 
1. MBBS
2. Cardio
3. ENT""")
            role=input("\nWhich Specialist you seek (ex: mbbs): ").upper()
            if role=="MBBS" or role=="CARDIO" or role=="ENT":
                hms_cursor.execute("select first_name,available from doctor where specialist = %s order by first_name",([role]))
                res=hms_cursor.fetchall()
                while True:
                    val=int(input("\nWant view specialist of doctors(1) or go back(2) "))
                    if val==1:
                        name=[]
                        table = PrettyTable(["Doctor","Availability"])
                        for loop_ in res:
                            table.add_row([loop_[0],loop_[1]])
                            name.append(loop_[0])
                        print(table)
                        appoint=input("\nWhich Doctor you want to make appoint: ").capitalize()
                        for loop in name:
                            if appoint == loop:
                                hms_cursor.execute("select available,status_ from doctor where first_name = %s",([appoint]))
                                result=hms_cursor.fetchall()
                                for rot in result:
                                    doc_avail_=rot[0]
                                    doc_status_=rot[1]
                                if doc_avail_=="NO":
                                    print("\nDoctor is not Available")
                                    break
                                elif doc_avail_=="YES" and doc_status_=="occupied":
                                    print("\nDoctor having Appointment")
                                    break
                                elif doc_avail_=="YES" and doc_status_=="unoccupied":
                                    while True:
                                        deal=int(input("\nYou can make appointment with this doctor(1) or not(2) "))
                                        if deal==1:
                                            stat=str("occupied")
                                            stat_=str("pending")
                                            name_=str(user_name)
                                            reason=str(input("Enter your problem: "))
                                            hms_cursor.execute("update patient set reason=%s,view_status=%s where username=%s",(reason,stat_,name_))
                                            hms_cursor.execute("update doctor set view_appointment=%s,status_=%s where first_name=%s",(name_,stat,appoint))
                                            dbconnect.commit()
                                            print(f"""\nYour appointment is slotted with {appoint}.
Check view status option for updated appointment.""")
                                            Patient.welcome(user_name,password_)
                                        elif deal==2:
                                            break
                        
                    elif val==2: Patient.welcome(user_name,password_)
                    else: display_1.invalid()
            else:
                print("Enter correct Specialist")