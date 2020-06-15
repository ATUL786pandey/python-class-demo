#  program to print prime no between 1 to 100

prime=[]
for i in range (1,100):
    fact=0
    for j in range(2,i):
        if i%j==0:
            fact=1
            break
    if fact==0:
        prime.append(i)
print("list of prime no",prime)
        
