#***WAP TO PRINT GREATER NO****

a=int(input("enter the first no => "))
b=int(input("enter the second no => "))
c=int(input("enter the third no => "))

if a>b and a>c:
    print(" {} is graeter ".format(a))
elif b>a and b>c:
    print(" {} is greater".format(b))
else:
    print(" {} is greater".format(c))
