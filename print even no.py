#**** WAP TO PRINT OLY EVEN NO****
while True:
    s=int(input("enter the range of no => "))
    i=1
    while i<=s:
        if (i%2)==0:
            print(i)
            i=i+1
        else:
            i=i+1
        
    
    ch=input("do u want to continue....(y/n)")
    if ch=='y':
        continue
    elif ch=='n':
        break
    else:
        print("invalid input")
    
