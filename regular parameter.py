'''
#regular parameter
def add(a,b):
    return a+b
print(add(10,20))


# default parameter
def add(a,b=0):
    return a+b
print(add(100))


#named or key word parameter

def add (a,b):
    return a+b
print(add(b=32,a=10.5))



#variable len argumnet parameter
def add (*x):
    s=0
    for i in x:
        s=s+i
    print(s)
add(10,20,30,40,50,60,70,80)
'''
def add(**x):
    for i in x.items():
        print("name",i[0],"value",i[1])
add(lastname="pandey",firstname="atul")
