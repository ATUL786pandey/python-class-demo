#wap to store the name of cricketer

cr={}
while True:
    name=input("enter the name=>")
    age=int(input ("enter the age=>"))
    cr[name]=age
    y_n=input("Do  u wnat to continue...!(y/n)")
    if y_n in ('y','Y'):
        continue
    else:
        break
for i in cr.items():
    print(" ",i[0], ":",i[1])
