import datetime
custdata=[]
class Bank:
    
    def __init__(self):
        data=[]
        self.name=input("Enter your name := ")
        self.account=input("Enter your account no :=")
        self.balance=1000
        self.panno=input("Enter your pan no:=")
        self.trdate=datetime.datetime.today()
        data.append(self.name)
        data.append(self.account)
        data.append(self.balance)
        data.append(self.panno)
        data.append(self.trdate)
        custdata.append(data)
        del data 
    def deposit(self):
        data1=[]
        amt=int(input("enter the amount to deposit := "))
        self.balance=self.balance+amt
        self.trdate=datetime.datetime.today()
        data1.append(self.balance)
        data1.append(self.trdate)
        custdata.append(data1)
        del data1
    def withdraw(self):
        data2=[]
        amt=int(input("Enter the amount to withdraw := "))
        self.balance=self.balance-amt
        self.trdate=datetime.datetime.today()
        data2.append(self.balance)
        data2.append(self.trdate)
        custdata.append(data2)
        del data2
'''   
    def showdata(self):
        print (self.name)
        print(self.account)
        print(self.balance)
        print(self.panno)
        print(self.trdate)
'''
def main():
        b1=Bank()
        b1.deposit()
        b1.withdraw()
        b2=Bank()
        b2.deposit()
        b2.withdraw()
        #b1.showdata()



        for i in custdata:
            print(i)
        
print(custdata)
main()

