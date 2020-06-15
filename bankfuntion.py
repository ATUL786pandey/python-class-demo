def collectuser(usr,pwd):
    use={"usr":usr,"pwd":pwd}
    return use
    
def validateuser(usr,pwd,use):
    if usr in use.values()== True  and  pwd in use.values() == True:
        return True
    else :
        return False
def corebanking():
    bal=1000
    print("w for withdraw\nd for deposit\nb for balance\ne for exit")
    ch=input("enter your choice.... ")
    while True:
            if ch=='w':
                    withd=int(input("enter the amount to withdraw"))
                    if(bal<=0):
                        print("insufficent fund")
                        continue
                    elif (withd>bal):
                        print("your balance is low aginst withdrawl")
                        continue
                    else:
                        bal=bal-withd
                        print("amount withdraw is {}and balance is {}",withd,bal)
            elif ch=='d':
                    dep=int(input("enter the amount to deposit"))
                    if dep>49000:
                        print("max deposit for day is 49000 only")
                        continue
                    else:
                        bal=bal+dep
                        
            elif ch=='b':
                    print("balance is ",bal)
                    
                                       
                    
            elif ch=='e':
                    break
            else:
                print("invalid input ")
            ch1=input("Do u want to continue ....(y/n)")
            ch1=ch1.lower()
            if ch1=='y':
                continue
            elif ch1=='n':
                break
            else:
                print("invalid input")
                
                
        
    


  
