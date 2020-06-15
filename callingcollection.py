from collectionfun import *
import collectionfun

while True:
    print("+ for addition ")
    print("- for subtraction ")
    print("a for voting eligibility ")
    print("f for factorial of no ")
    print("e for exit ") 
    ch=input("enter your choice..! ")
    if ch=='+':
        collectionfun.add()
    elif ch=='-':
        collectionfun.sub()
    elif ch=='a':
        collectionfun. chk()
    elif ch=='f':
        print(collectionfun.fact())
    elif ch=='e':
        break
    else:
        print("invalid input ")
