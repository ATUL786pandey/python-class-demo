#**** WAP TO PRINT FOR LOOP****
'''
for i in range(10):
    print(i)
'''

'''
for i in range(10,30,2):
    print(i)
'''
'''
s="python language"
c=0
for i in reversed (s):
    print(i,end="")
'''

s=input("enter your name =>")
c=''
for i in reversed(s):
    c=c+i
print("the name is {} and reversed that  is {}".format(i,c))
