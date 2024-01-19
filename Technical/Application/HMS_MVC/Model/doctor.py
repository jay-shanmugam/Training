from Model.database import hms_cursor, dbconnect
from View.user_view import display_1
from Model.sign_up import change_

from datetime import date
from datetime import datetime
from prettytable import PrettyTable

class Doctor:

    @classmethod
    def welcome(cls,username,password):
        while True:
            try:
                value = display_1.doc_perform()
                if value == 1:
                    hms_cursor.execute("select first_name,phone_number,reason,view_status from Patient")
                    result = hms_cursor.fetchall()
                    table = PrettyTable(["Name","Phone Number"])
                    sample=0
                    for loop in result:
                        if loop[2] !="none" and loop[3] == "pending":
                            sample+=1
                            table.add_row([loop[0],loop[1]])
                    if sample!=0:   print(table)
                    else:   print("\nNo patients are there in appointment")

                elif value == 2:
                    hms_cursor.execute("select status_ from doctor where username=%s",([username]))
                    name=hms_cursor.fetchall()
                    for i in name:
                        name_=i[0]
                    if name_=="unoccupied":
                        choice=display_1.doc_avail_choice()
                        if choice==1:
                            avail=str("YES")
                            Doctor.doc_avail(avail,password)
                        elif choice ==2:
                            avail=str("NO")
                            Doctor.doc_avail(avail,password)
                        else:
                            display_1.invalid()
                    else:
                        display_1.cancel_appoint()


                elif value == 3:
                    hms_cursor.execute("select view_appointment from doctor where username=%s",([username]))
                    pat=hms_cursor.fetchall()

                    hms_cursor.execute("select reason,first_name from patient where username=%s",(pat[0]))
                    doc_=hms_cursor.fetchall()

                    pat_name=[]
                    reason_=[]
                    for k in doc_:
                        pat_name.append(k[1])
                        reason_.append(k[0])
                    pat_=''.join(pat[0])
                    if pat_!="no_patient" and pat_!="null":
                        print(f"""\nYour have patient appointment
Patient name : {''.join(pat_name)}
Reason       : {''.join(reason_)}""")
                        while True:
                            slot = display_1.appoint_pat()
                            if slot==1:
                                clas=str(''.join(pat[0]))
                                Doctor.appoinment_datetime(username,password,clas)
                            elif slot==2:
                                stat_=str("unoccupied")
                                status_=str("not")
                                clas=str(''.join(pat[0]))
                                s="null"
                                reason1="null"
                                t_am_pm="null"
                                doc_app="no_patient"
                                can_=int(input("\nMake sure you want to cancel the appointment(1) or not(2)"))
                                if can_==1:
                                    Doctor.pat_appointment(s,t_am_pm,status_,reason1,clas)
                                    Doctor.doc_table_update(stat_,doc_app,username)
                                    print("\nAppointment Cancelled Successfully.")
                                    Doctor.welcome(username,password)
                                elif can_==2:
                                    Doctor.welcome(username,password)
                                else:
                                    display_1.incorrect_value()
                            else:
                                display_1.incorrect_value()
                    else:
                        print("\nNo Patient Appointment YET...")


                elif value == 4:
                    change_phone = change_.change_phonenumber(1,password)
                    if change_phone==1:
                        print("\n!!!Phone Number Updated!!!")
                        Doctor.welcome(username,password)

                elif value == 5:
                    change_password=change_.change_password(1,password)
                    if change_password==1:
                        print("\n!!!New Password Updated!!!")
                        Doctor.welcome(username,password)

                elif value == 6:
                    while True:
                        try:
                            choice1=display_1.again_login()
                            if choice1 == 1:
                                Doctor.welcome(username,password)
                            elif choice1 == 2:
                                display_1.last(2)
                                break
                            else:
                                display_1.invalid()
                        except ValueError:
                            display_1.incorrect_value()
                    display_1.close()

                else:
                    display_1.incorrect_value()
            except:
                display_1.invalid()

    @classmethod
    def doc_avail(cls,avail,password):
        hms_cursor.execute("update Doctor set available = %s where passwd=%s",(avail,password)) 
        print("\nUpdated!\n")
        dbconnect.commit()

    @classmethod
    def pat_appointment(cls,appoint_date,appoint_time,pat_status,reason2,patient_name):
        hms_cursor.execute("update patient set date_= %s ,time_= %s ,view_status= %s,reason= %s where username=%s",(appoint_date,appoint_time,pat_status,reason2,patient_name))
        dbconnect.commit()

    @classmethod
    def doc_table_update(cls,doc_status,appoint_status,doctor_name):
        hms_cursor.execute("update doctor set status_= %s,view_appointment=%s where username= %s",(doc_status,appoint_status,doctor_name))
        dbconnect.commit()

    @classmethod
    def appoinment_datetime(cls,username1,password1,patient):
        doc_appoint=str("no_patient")
        doc_stat_=str("unoccupied")
        status_=str("accepted")
        reason_=str("null")
        while True:
            try:
                date_=input("Enter Appointment date(ex:YYYY-MM-DD): ").split('-')
                year, month, day = [int(item) for item in date_]
                d=date(year, month, day)
                s=str(d)
                appoint_Date= d.day
                appoint_month=d.month
                now = date.today()
                now_date=now.day
                now_month=now.month
                if now_date <= appoint_Date and now_month<=appoint_month:
                    try:
                        while True:
                            time_=input("Enter Appointment time(ex: 15:00): ")
                            t_obj = datetime.strptime( time_, '%H:%M')
                            t_am_pm = t_obj.strftime('%H:%M')
                            hour_=t_obj.strftime('%H:%M').split(":")
                            hour, minute=[int(item_) for item_ in hour_]

                            if hour>=8 and hour<=20:
                                Doctor.pat_appointment(s,t_am_pm,status_,reason_,patient)
                                Doctor.doc_table_update(doc_stat_,doc_appoint,username1)
                                print(f"\nAppointment successfully sloted with {patient}")
                                Doctor.welcome(username1,password1)

                            else:
                                option=int(input("\nYour time is Over Time appointment yes(1) or no(2) "))
                                if option==1:
                                    Doctor.pat_appointment(s,t_am_pm,status_,reason_,patient)
                                    Doctor.doc_table_update(doc_stat_,doc_appoint,username1)
                                    print(f"\nAppointment successfully sloted with {patient}")
                                    Doctor.welcome(username1,password1)
                                elif option==2:
                                    Doctor.welcome(username1,password1)
                                else:
                                    display_1.incorrect_value()
                    except:
                        print("Enter correct Time")
                else:
                    display_1.correct_date()
            except ValueError:
                display_1.correct_date()
