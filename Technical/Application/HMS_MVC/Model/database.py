import mysql.connector

dbconnect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Jay4prasanth@',
    database = "hms"
)
hms_cursor = dbconnect.cursor()

'''dbconnect = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='Jay4prasanth@'
)
hms_cursor = dbconnect.cursor()
print(dbconnect)
hms_cursor.execute("CREATE DATABASE hms")
hms_cursor.execute("DROP DATABASE hms")'''

'''try:
    doc = hms_cursor.execute("""CREATE TABLE doctor (  doctor_id INT PRIMARY KEY AUTO_INCREMENT,
					                            first_name VARCHAR(20) not null,
                                                last_name VARCHAR(20) not null,
                                                initial VARCHAR(3) not null,
                                                DOB VARCHAR(20) not null,
                                                age VARCHAR(2) not null,
                                                phone_number VARCHAR(10) not null,
                                                username VARCHAR(20) not null,
                                                passwd VARCHAR(20) not null,
                                                specialist varchar(30),
                                                available VARCHAR(5),
                                                status_ VARCHAR(20),
                                                CHECK (status_ IN ('occupied', 'unoccupied')),
                                                view_appointment VARCHAR(20) default 'null' )""")
    pat = hms_cursor.execute("""CREATE TABLE Patient ( patient_id INT PRIMARY KEY AUTO_INCREMENT,
                                                first_name VARCHAR(20) not null,
                                                last_name VARCHAR(20) not null,
                                                initial VARCHAR(3) not null,
                                                DOB VARCHAR(20) not null,
                                                age VARCHAR(2) not null,
                                                phone_number VARCHAR(10) not null,
                                                username VARCHAR(20) not null,
                                                passwd VARCHAR(20) not null,
                                                reason VARCHAR(30) default 'none',
                                                view_status VARCHAR(10) default 'null',
                                                date_ VARCHAR(10) default 'null',
                                                time_ VARCHAR(10) default 'null')""")
    admin = hms_cursor.execute("""CREATE TABLE Admin ( first_name VARCHAR(20) not null,
                                                last_name VARCHAR(20) not null,
                                                initial VARCHAR(3) not null,
                                                phone_number VARCHAR(10) not null primary key,
                                                username VARCHAR(20) not null,
                                                passwd VARCHAR(20) not null)""")
    
except:  
    dbconnect.rollback()'''

'''
sql="insert into admin(first_name,last_name,initial,phone_number,username,passwd)values(%s,%s,%s,%s,%s,%s)"
val=("jay","prasanth","s","7094834556","jack","Jay4prasanth@")
try:
    cur.execute(sql,val)
    mydb.commit()
except:
    mydb.rollback()'''

