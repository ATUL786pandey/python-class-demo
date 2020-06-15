#**** WAP gor menu calculator*****
while True:
    print("*****************menu calculator********")
    print("+ for addition")
    print("- for subtarction")
    print("* for multiplication")
    print("/ for division")
    ch=input("Enter your choice => ")

    if ch=='+':
        a=int(input("enter the first value  "))
        b=int(input("enter the second value "))
        c=a+b
        print("value is {}".format(c))
    elif ch=='-':
        a=int(input("enter the first value  "))
        b=int(input("enter the second value "))
        c=a-b
        print("value is {}".format(c))
    elif ch=='*':
        a=int(input("enter the first value  "))
        b=int(input("enter the second value "))
        c=a*b
        print("value is {}".format(c))
    elif ch=='/':
        a=int(input("enter the first value  "))
        b=int(input("enter the second value "))
        c=a/b
        print("value is {}".format(c))
    else:
        print("invalid input")
    ch1=input("Do u want to continue.....(y/n) ")
    ch1=ch1.lower()
    if ch1=='y':
          continue
    elif ch1=='n':
            break
    else:
        print("invalid input")
