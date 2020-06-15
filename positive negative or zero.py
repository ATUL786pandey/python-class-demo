#*** WAP TO CHECK WHEATHER NO IS POSITIVE,NEGATIVE OR ZERO***

num=int(input("enter the no => "))
if num > 0:
    print("number {} is positive ".format(num))
else:
    print("number {} is nagative".format(num))
    if num==0:
        print(" number {} is zero".format(num))
