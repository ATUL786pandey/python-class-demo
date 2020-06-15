#*****WAP TO PRINT REVERSE OF NO******
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
    
