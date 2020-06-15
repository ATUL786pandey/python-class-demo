'''
#***WAP TO FIND THE YEAR IS LEAP YEAR OR NOT ***

year=int(input ("enter the year =>"))
if(year % 4)==0:
    if(year % 100)==0:
        if(year % 400)==0:
            print("{} is a leap year".format(year))
        else:
            print(" {} is not a leap year".format(year))
    else:
         print("{} is a leap year ".format(year))
else:
    print("{} is not a leap year".format(year))
'''


'''
#*** WAP TO CHECK WHEATHER NO IS POSITIVE,NEGATIVE OR ZERO***

num=int(input("enter the no => "))
if num > 0:
    print("number {} is positive ".format(num))
else:
    print("number {} is nagative".format(num))
    if num==0:
        print(" number {} is zero".format(num))
   '''


'''

#***WAP TO CHECK WHEATHER THE NO IS ODD OR EVEN**

num=int(input(" Enter the number =>  "))
if (num % 2)==0:
    print("number {} is even".format(num))
else:
    print(" number {} is odd".format(num))

'''

'''
#*** WAP TO CALCULATE THE INTEREST ON PRINCICAL,YEAR,AND RATE OF INTEREST***

amt=700000
year=5
roi=11.5
smi=amt*year*roi/100
print ("interest on amount = {},year = {},roi = {} is = {}".format(amt,year,roi,amt-smi))
'''


#*** greet the user good morning,good afternoon,good evening depinding on the
#time of the day inside variablehrs input from the user in 24 hrs format***


time=int(input("enter the time=>  "))
if time <= 12:
    print("good morning")
if time >=20:
    print("good afternoo")
if time >= 24:
    print("good evening")







