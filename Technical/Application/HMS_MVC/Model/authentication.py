from Model.database import hms_cursor, dbconnect
class access:
    @classmethod
    def verify(cls,username1,password1,profile1):
        user_name=[]
        pass_word=[]
        if profile1==1:
            opt=("Patient")
        elif profile1 ==2:
            opt=("Doctor")
        elif profile1 ==3:
            opt=("Admin")    
        try:
            hms_cursor.execute("select username,passwd from %s"%opt)
            result = hms_cursor.fetchall()
            for row in result:
                user_name.append(row[0])
                pass_word.append(row[1])
        except:
            dbconnect.rollback()

        username_flag=False
        password_flag=False
        for i in user_name:
            if username1==i:
                username_flag=True
        for j in pass_word:
            if password1==j:
                password_flag=True        
        if username_flag and password_flag:
            return 1
        else:
            return 0

   