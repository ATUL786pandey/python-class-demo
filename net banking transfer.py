#WAP TO MONEY TRANSFFER TO OTHER CUSTOMER
#CREATE A PROGARM FOR NET BANKING


class Customer:
    def __init__(self):
        self.__balance=1000
        self.__accountno=input("Enter your account no=> ")
        self.__pin=input("Enter your pin => ")

    def transfer(self,other):
        if self.__validate():
            print("login sucessfully !")
            amount=float(input("Enter the amount to transfer => "))
            self.__balance=self.__balance-amount
            other.__balance=other.__balance+amount
            print("Amount transfer sucessfully !")
            
    def __validate(self):
        
        p=input("Enter your pin => ")
        if p==self.__pin:
            return True
        else:
            return False


    def showdata(self):
        print("Account no ",self.__accountno)
        print("Balance is ",self.__balance)

def main():
    atul=Customer()
    atul.showdata()
    amol=Customer()
    amol.showdata()
    atul.transfer(amol)
    atul.showdata()
    amol.showdata()

main()
