#***********WAP  A PROGRAM FOR ARMSTRONG NO**********

num=int(input("enter the no => "))
temp=num
arm=0
while num!=0:
    rem=num%10
    arm=rem**3+arm
    num=num//10
if temp == arm:
    print("it is armstrong")
else:
    print("it is not armstrong")
