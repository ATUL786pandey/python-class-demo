#program where user has input both the height and base of both triangle but
#total came with some error
'''
class Triangle:
    def __init__(self):
        self.base=int(input("Enter the base of triangle =>"))
        self.height=int(input("Enter the height of triangle =>"))
        self.b=int(input("Enetr the base of second triangle =>"))
        self.h=int(input("Enter the height of second Triangle => "))
        self.area=None
        self.area1=None

    def areacal(self):
        self.area=self.base*self.height/2
        self.area1=self.b*self.h/2

    def __add__(self):
        total=self.area+self.area1
        print("total area of triangle is {}".format(total))

    def showdata(self):
        print(self.base)
        print(self.height)
        print(self.b)
        print(self.h)
        print(self.area)
        print(self.area1)
        self.__add__()
        print(self.__add__)

def main():
    t=Triangle()
    t.areacal()
    
    t.showdata()
    
    try:
        self.area+self.area1
    except NameError as ne:
        print(ne)

    except Exception as e:
        print(e)
    print("good morning")
    
main()
'''

class Triangle:
    def __init__(self):
        self.h=int(input("Enter the height =>"))
        self.b=int(input("Enter the base => "))
        self.area=None

    def areacal(self):
        self.area=self.h*self.b/2

    def __add__(self,other):
        total=self.area+other.area
        print("total area of  2 triangle is {}".format(total))

    def showdata(self):
        print(self.h)
        print(self.b)
        print(self.area)

def main():
    t=Triangle()
    t1=Triangle()
    t.areacal()
    t1.areacal()
    t.showdata()
    t1.showdata()

    t+t1

main()






























