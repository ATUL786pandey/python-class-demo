#**** WAP FOR LEAP YEAR****

year=int(input("enter the year => "))
if (year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print("Enter year {} is leap year".format(year))
        else:
            print("Enter year {} is not leap year".format(year))
    else:
        print("Enter year {} is leap year".format(year))

else:
    print("Enter year {} is not leap year ".format(year))
