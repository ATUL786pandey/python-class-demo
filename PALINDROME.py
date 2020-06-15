#***WAP TO PRINT PALINDROME***********


while True:
    num=int(input("Enter the no => "))
    rem=0
    rev=0
    temp=num
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    #print("number after reverse process become =>",num)
    print(" reverse is {}".format(rev))


    if temp == rev:
        print("it is palindrome")
    else:
        print ("it is not palindrome")
    ch=input("do u want to continue .....(y/n)")
    ch=ch.lower()
    if ch=='y':
        continue
    elif ch=='n':
         break
    else:
            print("invalid input")
        
