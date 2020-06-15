#wriite a program to store vehicle  detail
#use oop for program

class Vehicle:
    def __init__(self):
        self.vcompany=input("Enter the vehicle company  name => ")
        self.vmodel=input("Enter the model no => ")
        self.vengine=input("Enter the Engine no=> ")
        self.vprice=float(input("Enter the Price of vehicle=> "))

    def writedata(self):
        try:
            f=open("E:\\Atul1\\vehicledetail.csv","a+")
            b=self.vcompany+','+self.vmodel+','+self.vengine+','+str(self.vprice)+'\n'
            f.write(b)

        except Exception as e:
            print(e)
        finally:
            f.close()

    def readdata(self):
        try:
            f=open("E:\\Atul1\\vehicledetail.csv")
            listvehicle=f.readlines()
            for i in listvehicle:
                print(i)
        except Exception as e:
            print(e)
        finally:
            f.close()

def main():
    while True:
            v=Vehicle()
            v.writedata()

            ch=input("Do u want to continue (y/n)")
            if ch in ('y','Y'):
                continue
            else:
                v.readdata()


if __name__=='__main__':
    main()
