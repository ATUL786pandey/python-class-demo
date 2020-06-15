'''
#WAP  TO CALCULATE THE AGE
age=input("enter the age in dd mm yy")
currentage=datetime.date()
print("your age is ",currentage)
'''

import datetime
year=datetime.datetime.now().year
Dob=int(input("enter your birth year"))
age=year-Dob
print("you are {} year old ".format(age))
