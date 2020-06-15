#user define  function example which will be call by other program
def add():
    x=int(input("enter the no of x " ))
    y=int(input ("enter the no of y "))
    sum=x+y
    print("sum of {} +{} is {}".format(x,y,sum))

def sub():
    a=int(input("enter the value of a "))
    b=int(input(" enter the value of b "))
    c=a-b
    #print("sub of {}- {} is {}".format(a,b,c))
    return c


#paramter but no return type
def chk():
    age=int(input ("enter the age "))
    if age>18:
        print("eligible for voiting")
    else:
        print("not eligible for voiting")

#parameter & return type:
def fact():
    
    n=int(input("enter the no to get factorial "))
    f=1
    for i in range (n,1,-1):
        f=f*i
        
    return f 





'''
#calling function
add()
# calling return function 
c=sub()
print(c)
#calling parameter but no return type
chk()

#calling parameter & return type
print(fact())
'''
