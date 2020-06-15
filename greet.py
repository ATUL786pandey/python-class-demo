#***WAP TO PRINT GOOD MORNING,AFTERNOON,EVENING*****
hrs=int(input("enter the time => "))
if hrs >= 8 and hrs <= 12:
    print("good morning".format(hrs))
if hrs > 12 and hrs <=16:
    print("good afternoon".format(hrs))
if hrs > 16 and hrs <=20:
    print("good evening".format(hrs))

