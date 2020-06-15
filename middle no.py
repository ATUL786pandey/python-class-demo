#*** WAP TO PRINT MIDDLE NO ****

a=int(input("enter the first no => "))
b=int(input("enter the second no => "))
c=int(input("enter the third no => "))
if (b < a and b > c) or (b > a and b < c):
    print(" {} is middle".format(b))
elif (a < b and a > c) or(a > b and a < c):
    print("{} is middle".format(a))
else:
    print(" {} is middle ".format(c))
