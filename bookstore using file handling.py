#wrtite a program to store book information into .cvs file
#use oop for this program

class Bookinfo:
    def __init__(self):
        self.bid=input("Enter the book id => ")
        self.bname=input("Enter the book Name=> ")
        self.bprice=float(input("Enter the book price=> "))

    def writedata(self):
        try:
            f=open("E:\\Atul\\bookinfo.csv","a+")
            b=self.bid+','+self.bname+','+str(self.bprice)+'\n'
            f.write(b)
        except Exception as e:
            print(e)
        finally:
            f.close()

    def readdata(self):
        try:
            f=open("E:\\Atul\\bookinfo.csv")
            listbook=f.readlines()
            for i in listbook:
                print(i)
        except Exception as e:
            print(e)
        finally:
            f.close()

def main():
    while True:
        b1=Bookinfo()
        b1.writedata()

        ch=input("Do u want to continue (y/n) ")
        if ch in ('y','Y'):
            continue
        else:
            b1.readdata()

if __name__=='__main__':
    main()
        
