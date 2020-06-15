#wap program to store Employee detail
#program using oop

class Employee:
    def __init__(self):
        self.empid=input("Enter the Employee ID=> ")
        self.empname=input("Enter the Employee Name=> ")
        self.salary=float(input("Enter the Employee Salary=> "))
        self.designation=input("Enter the Employee Designation=> ")

    def writedata(self):
        try:
            f=open("E:\\Atul1\\employee.csv","a+")
            b=self.empid+','+self.empname+','+str(self.salary)+','+self.designation+'\n'
            f.write(b)
        except Exception as e:
            print(e)
        finally:
            f.close()
    def readdata(self):
        try:
            f=open("E:\\Atul1\\employee.csv")
            listemp=f.readlines()
            for i in listemp:
                print(i)

        except Exception as e:
            print(e)
        finally:
            f.close()


def main():
    while True:
        e=Employee()
        e.writedata()

        ch=input("Do u want to continue (y/n)")
        if ch in ('y','Y'):
            continue
        else:
            e.readdata()
if __name__=='__main__':
    main()
