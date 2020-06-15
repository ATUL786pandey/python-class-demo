'''
class Student:
    def __init__(self):#it is constructor
        self.name=input("enter your name ")
        self.rollno=input("enter your roll no")
    def showdata(self):#it is member method
        print("roll no is ",self.rollno)
        print("Name is ",self.name)
def main():
    s=Student()#create variable of class
    s1=Student()
    s.showdata()
    s1.showdata()
'''
class Company:
    def __init__(self):
        self.empid=input("enter employee id ")
        self.designation=input("enter your designation=")
        self.empname=input("enter your name" )
        self.mobileno=input("enter your mobile no" )
    def showdata(self):
        print("empid is :-",self.empid)
        print("Designation is ",self.designation)
        print("employe name is ",self.empname)
        print("mobile ni is ",self.mobileno)
def main():
    c=Company()
    c1=Company()
    c2=Company()
    c3=Company()
    c.showdata()
    c1.showdata()
    c2.showdata()
    c3.showdata()
            
    
