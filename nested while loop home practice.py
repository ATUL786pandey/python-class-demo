#nested while loop
'''
i=1
c=0
while i<=3:
    j=1
    while j<=3:
        c=c+1
        print(c,end="")
        j=j+1
    print()
    i=i+1
'''

'''
i=1
while i<=3:
    j=1
    while j<=i:
        if(i%2)==0:
            print(0,end="")
        else:
            print(1,end="")
        j=j+1
    print()
    i=i+1
    
'''



i=1
while i<=5:
    j=1
    while j<=i:
        if(i%2)==0:
            print("*",end="")
        else:
            print("#",end="")
        j=j+1
    print()
    i=i+1

'''
out put:
*
**
***
****
*****
'''

'''

i=1
while i<=5:
    j=5
    while j>=i:
        if(j%2)==0:
            print("*",end="")
        else:
            print("#",end="")
        j=j-1
    print()
    i=i+1
'''


'''
output:
*****
****
***
**
*
'''

'''
i=1
while i<=5:
    j=1
    while j<=5:
        if(j%2)==0:
            print("*",end="")
        else:
            print("*",end="")
        j=j+1
    print()
    i=i+1
'''
