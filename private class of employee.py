import datetime
class Employee:
    def __init__(self):
        self.__empno=int(input("Enter the employee id no => "))
        self.__empname=input("Enter the Employee Name => ")
        self.__salary=int(input("Enter the amount of salary => "))
        self.__dob=int(input("Enter the birth year=> "))
    def __age(self):
        year=datetime.datetime.now().year
        self.__age=year-self.__dob
    def showdata(self):
        print("Employee no is ",self.__empno)
        print("Employee name is",self.__empname)
        print("Employee salary is ",self.__salary)
        self.__age()
        print("Age of Employee is {} year old  ".format(self.__age))

def main():
    e=Employee()
    e.showdata()

main()
        
