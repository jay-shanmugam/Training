class Authentication:
    def verify(user,passw,filename):
        f=open(filename,"r")
        overall=f.readlines()
        username=[]
        password=[]
        for i in overall:
            username_password=i.split(' ')
            #print(username_password)
            username.append(username_password[4])
            password.append(username_password[5])
            #print(i)
        password=[s.replace('\n','') for s in password]
        #print(password)
        username_flag=False
        password_flag=False
        for i in username:
            if user==i:
                username_flag=True
        for j in password:
            if passw==j:
                password_flag=True        
        if username_flag and password_flag:
            return 1
        else:
            return 0