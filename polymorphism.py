'''
class A:
    def show(self):
        print("show method of A class")
class B(A):
    def show (self):
        super().show()
        print("Show method of B class")


def main():
    b=B()
    b.show()
    b=A()
    b.show()

main()
    
'''


class A:
    def show(self):
        self.name=input("enter your first name ")

class B(A):
    def show(self):
        super().show()
        self.middle=input("enter your middle name")

class C(B):
    def show(self):
        super().show()
        self.last=input("enter your last name ")

def main():
    c=C()
    c.show()
    c=B()
    c.show()
    b=A()
    b.show()

main()
