import mysql.connector as conn

class Employee:
    def __init__(self):
        self.empid=None
        self.empname=None
        self.designation=None
        self.salary=None

    def openconn(self):
        self.db=conn.connect(host="localhost",user="root",passwd="",
                             database="Employeemgmt")

    def closeconn(self):
        self.db.close()

    def insertrec(self):
        self.openconn()
        self.empid=input("Enter Employee Id :- ")
        self.empname=input("Enter Employee Name:- ")
        self.designation=input("Enter designation of employee:-")
        self.salary=float(input("Enter Salary of employee:- "))
        sql="insert into employee values('{}','{}','{}','{}')".format(self.empid,self.empname,self.designation,self.salary)
        cur=self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        self.closeconn()
        if cur.rowcount>0:
            return True
        else:
            return False


    def updaterec(self,empid):
        self.openconn()
        empname=input("Enter Name to update:- ")
        designation=input("Enter Designation to  update:- ")
        salary=float(input("Enter salary to update:-"))
        sql="update employee set empname='{}',designation='{}',salary='{}' where empid='{}'".formate(empname,designation,salary,empid)
        cur=self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        self.closeconn()
        if cur.rowcount>0:
            return True
        else:
            return  False

    def deleterec(self,empid):
        self.openconn()
        sql="delete from employee where empid='{}'".format(empid)
        cur=self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        self.closeconn()
        if cur.rowcount>0:
            return True
        else:
            return False

    def searchrec(self,empname):
        self.openconn()
        sql="select * from employee where empname='{}'".format(empname)
        cur=self.db.cursor()
        cur.execute(sql)
        data=cur.fetchone()
        print("\empid\tempname\tdesignation\tsalary")
        for i in data:
            print(i,end="\t")
        self.closeconn()

    def showallrec(self):
        self.openconn()
        sql="select * from employee "
        cur=self.db.cursor()
        cur.execute(sql)
        data=cur.fetchall()
        for i in data:
            print(i[0],' ',i[1],' ',i[2],' ',i[3])
            print("\n\n\n\n")
        self.closeconn()


def main():
    while True:
        e=Employee()
        print("\n\n\n1 insert record\n2 udate record\n3 delte record\n4 search employee\n5 showall employee")
        ch=int(input("Enter the choice:- "))
        if ch==1:
            if e.insertrec():
                print("Record enter successfully !")
            else:
                print("Try again.... !")

        elif ch==2:
            empid=int(input("Enter employee id:-  "))
            if e.updaterec(empid):
                print("Record update Successfully ...! ")
            else:
                print("Try again....!")

        elif ch==3:
            empid=int(input("Enter employee id :- "))
            if e.deleterec(empid):
                print("Record delted successfully....!")
            else:
                print("Try Again....!")

        elif ch==4:
            empname=input("Enter employee Name to search :- ")
            e.searchrec(bname)

        elif ch==5:
            e.showallrec()

main()
                
            
        
