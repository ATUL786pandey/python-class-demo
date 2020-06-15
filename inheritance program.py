class Student:
    #constructor
    def __init__(self):
        #self repesent to current class object
        #after . are members of class
        self.name=input("Enter your name = ")
        self.rollno=int(input("Enter your Roll No= "))
        #method
    def showdata(self):
        print("\n Name : ",self.name)
        print("roll No :",self.rollno)
def main():
    s1=Student() #bracket complusary as used for calling constructor
    s2=Student()
    s1.showdata()
    s2.showdata()
main()

class Demo:
    def show(self):
        print("GOOD MORNING")

def main():
    d=Demo()
    d.show()
main()



#program 2
class Demo:
    def show(self):
        self.a=100
        self.b=200
        self.c=self.a+self.b
        print(self.c)
        print("GOOD MORNING")
def main():
    d=Demo()
    d.show()
main()

#program 3

class Demo:
    def show(self):
        self.a=100
        self.b=200
        self.c=self.a+self.b
        print(self.c)
        print("GOOD MORNING")
def main():
    d=Demo()
    d.show()

if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------

#static variable and static method of class
'''
static means common data or function for all objects
once it is initilialised ,it will be common for all object
scope of static member is class not object
static member can be used with class name
nameofclass member
static member are also known as class member
'''
#Example
class Student:
    #static variable
    #class variable
    #scope within class common for all object
    college='APSIT'
    #member method or object instance method
    def data(self):
        #instance/object variable
        #scope within object
        self.name=input("Enter your name = ")
        self.rollno=input("Enter your Roll no = ")
    def show(self):
        #instance variable access with current class object , here is it self
        print("Name :",self.name)
        print("Roll no is :",self.rollno)
        #static variable access with class name
        print("College :",Student.college)


        #static method or class method
        #scope within class common for all object
    @staticmethod
    def greeting():
        print("good morning to all student")
def main():
    s1=Student()
    s1.data()
    s1.show()
    s2=Student()
    s2.data()
    s2.show()
if __name__ == '__main__':
    main()



#---------------------------------INHERITANCE in python---------------------------------------------    
'''
inheritance means inherit one class into another class
when we inherit class at that time ,all datamember and member method
will also inherit in child class

inherited class for child,sub class
inherit is parent derived class , parent class base class
'''

class A:#parent class of A
    def msg(self):
        print("I am msg method of class A....")
class B(A):#child class of A
    def message(self):
        print("Iam message method of class B........")
def main():
    b=B()
    b.msg()
    b.message()
main()


#Multilevel Inheritance
'''
A->B->C
'''
#program for multiinheritance
class A:#parent class of A
    def msg(self):
        print("I am msg method of clas A............")
class B(A):#chid class of A
    def message(self):
        print(" I am message method of class B..........")
class C(B):# child class of B
    def m(self):
        print("I am message method of class C...........")

def main():
    c=C()
    c.msg()
    c.message()
    c.m()
main()


print("multiple inheritance")
'''
        A          B
        |          |
        V          V
        -------------
              |
              V
              C
'''

#class B is not derived from A
class A:
    def message(self):
        print("I am Class A")
class B:
    def m(self):
        print("I am class B")
class C(A,B):
    def mg(self):
        print("Iam class c")
def main():
    c=C
    c.message()
    c.m()
    c.mg()
main()


#another example of multiple inheritance
#multiple inheritance

class Bank:
    def roi(self,r):
        print(r)
class ICICI(Bank):
    pass
class SBI(Bank):
    pass
class HDFC(Bank):
    pass
def main():
    icici=ICICI()
    icici.roi(7.5)
    sbi=SBI()
    sbi.roi(8)
    hdfc=HDFC()
    hdfc.roi(9.5)
main()









































































        
    
































    
