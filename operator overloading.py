#WAP PROGRAM FOR OPERATOR OVERLOADING
'''
class Student:
    def __init__(self,rollno,name,he):
        
        self.rollno=rollno
        self.name=name
        self.he=he

    def check(self,other):
        if self.he > other.he:
            print(self.name ,"heighted then ",other.name)
        else:
            print(other.name ,"heighted then ",self.name)

    def __gt__(self,other):
        if self.he > other.he:
            print(self.name,"heighted then ",other.name)
        else :
            print(other.name,"heighted then ",self.name)

def main():
    prasad=Student(100,"prasad",float(170.00))#height in centimeter
    ganesh=Student(105,"ganesh",float(180.34))#height in centimeter
    prasad > ganesh

main()
'''

class Student:
    '''

        hi how r u

    '''    
    def __init__(self,rollno,name,he):
        self.rollno=rollno
        self.name=name
        self.he=he

    def chk(self,other):
        if self.he>other.he:
            print(self.name,"highted then ",other.name)
        else :
            print(other.name,"highted then ",self.name)

    def __gt__(self,other):
        if self.he>other.he:
            print(self.name,"heighted then",other.name)
        else:
            print(other.name,"heighted then ",self.name)
    @staticmethod
    def attributeshow():
        print("name",Student.__name__)
        print("commented area",Student.__doc__)
        print("all member detail",Student.__dict__)
        print("module",Student.__module__)
        print("base",Student.__bases__)


def main():
    prasad=Student(100,"prasad",float(170.00))
    ganesh=Student(150,"ganesh",float(180.34))
    prasad>ganesh
    Student.attributeshow()

main()
