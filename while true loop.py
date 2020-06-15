while True:
    bal=1000
    ch=input("W for withdrawl and D for deposit => ")
    if ch=='w':
        witd=int(input("enter the amount to withdraw =>"))
        if (witd > bal):
            print("Insufficient Fund")
        elif (witd > 25000):
            print("Max limit for day is 25000 only")
        elif (bal < 1000):
            print("Insufficient Balance")
        else:
            bal=bal-witd
            print("your balance is {}".format(bal))
    if ch=='d':
        dep=int(input("enter the amount to deposit =>"))
        if dep>49000:
            print("Max limit to deposit for day is 49000 only")
        else:
            bal=bal+dep
            print("Balance is :- {}".format(bal))
            
    cho=input("Do U Want to  Continue.......(y/n)")
    cho=cho.lower()
    if cho=='y':
        continue
    elif cho=='n':
        break
    else:
        print("invalid input")

