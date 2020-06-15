import datetime
class Employee:
    def __init__(self):
        self.__empno=input("Enter the employee  id no ")
        self.__empname=input("Enter the Employee Name")
        self.__salary=int(input("Enter the Employee Salary  "))
        self.__dob=int(input("Enter the  birth of year "))

    def __age(self):
       year=datetime.datetime.now().year
       self.__age=year-self.__dob

    def showdata(self):
        print(self.__empno)
        print(self.__empname)
        print(self.__salary)
        self.__age()
        print(self.__age)

def main():
    e=Employee()
    e.showdata()

main()
