""" Nested while 2
i=1
c=0
while i<=3:
    j=1
    while j<=3:
        c+=1
        print(c,end=" ")
        j+=1
    print("\n")
    i+=1
"""
''' Nested while program 3
i=1
while i<=4:
    j=1
    while j<=i:
        if i%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
        j+=1
    print("\n")
    i+=1
o/p
1 
                                                                  
0 0 

1 1 1 

0 0 0 0 

'''
''' Nested while program 3
i=1
while i<=4:
    j=1
    while j<=i:
        if j%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
        j+=1
    print("\n")
    i+=1
o/p
1 

1 0 

1 0 1 

1 0 1 0
'''
