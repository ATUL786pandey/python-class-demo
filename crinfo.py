crinfo=[]
while True:
    data=[]
    name=input("enter your name :-")
    age=int(input("enter your age :- "))
    gender=input("enter your gender :-")
    data.append(name)
    data.append(age)
    data.append(gender)
    crinfo.append(data)
    del data
    ch=input("do u wnat to continue...@ (y/n)")
    if ch in ('n','N'):
        break
    for i in crinfo:
        print(i)
print(crinfo)
    
