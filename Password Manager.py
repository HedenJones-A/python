#connection


import mysql.connector as m
con=m.connect(host='localhost',user='root',passwd='root',database='password_manager')
cur=con.cursor()


#-------------------------------------------------------------------------------------------------------



#functions
def sp():

    web=input("Enter the WEBSITE NAME :: ")
    user=input("Enter the USER NAME :: ")
    email=input("Enter the EMAIL :: ")
    password=input("Enter the PASSWORD :: ")
    
    

    cur.execute("insert into passwords values('{}','{}','{}','{}')".format(web,user,email,password))
    con.commit()
        
def gp():

    getweb=input("Enter the website name :: ")

    query="select password from passwords where website='{}'".format(getweb)

    cur.execute(query)
    x=cur.fetchone()
    z=x[0]
    return z
    

#-----------------------------------------------------------------------------------------------------



passwd='user'

while True:
    print("******************** WELCOME ********************")
    #print("               !PASSWORD MANAGER!")
    print()
    print()

    getpasswd=input("enter the password [PRESS Q TO EXIT] :: ")
    # if getpasswd=='Q' or 'q':
    #     print()
    #     print("THANK YOU")
    #     print("***VISIT ONCE AGAIN***")
    #     break
    if getpasswd==passwd:
        print()
        print("1.Store password")
        print("2.Get password")
        print()
        ch=int(input("Enter the above choice ::"))
        if ch==1:
            x=sp()
        else:
            y=gp()
            print()
            print()
            print("**YOUR PASSWORD IS** :: ",y)
    

    
    elif getpasswd!=passwd:
        print()
        print("!!!WARNING!!!")
        print("invalid input TRY AGAIN")

    
    

 
