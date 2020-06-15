from bankfuntion import*
use={}
while True:
        print("1 for create new user\n2 Login for Existing user\n3 Exit")
        ch=int(input("enter your choice "))
        if ch==1:
            while True:
                usr=input("enter the user name :-")
                pwd=input("enter the password :-")
                if (usr in use.values())== True :
                    print("user name already created ! please try for another")
                    continue
                else:
                    print("account created Sucessfully Thank  ")
                    use=collectuser(usr,pwd)
                    break
        elif ch==2:
            while True :
                usr=input("enter your user name :- ")
                pwd=input("enter your password :- ")
                val=validateuser(usr,pwd,use)
                if (val==True):
                    print("Login Sucessfully")
                    corebanking()
                else:
                    print("Invalid User Name or Password...!")
                    break
        elif ch==3:
            break
        ch1=input("Do u Want to continue...!(y/n)").lower()
        
        if ch1=='y':
            continue
        elif ch1=='n':
            break
        else:
            print("Invalid Input")
        
