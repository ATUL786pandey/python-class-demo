#user define exception
#AS A DEVELOPER AS PER YOUR SOFTWARE NEED WE CREATE EXCEPTION
#KNOWN AS USER DEFINE EXCEPTION
# TO CREATE USER DEFINE EXCEPTION WE HAVE TO INHERIT PARENT EXCEPTION CLASS
# NAME AS EXCEPTION


class AgeValidError(Exception):
    pass
class Voiting(AgeValidError):
    Bjp=0
    Congress=0
    AAP=0
    nota=0



    def __init__(self):
        self.name=input("Enter your name => ")
        self.age=int(input("Enter Your Age => "))
        self.aadharno=input("Enter your aadhar card no=> ")

    def vote(self):
        if self.age <=18:
            raise AgeValidError("not Eligible for voiting")
        else:
            print("1 for Bjp\n2 for Congress\n3 for AAP")
            ch=int(input("enter your choice "))
            if ch==1:
                Voiting.Bjp+=1
            elif ch==2:
                Voiting.Congress+=1
            elif ch==3:
                Voiting.AAP+=1
            else:
                Voiting.nota+=1



def main():
    while True:
        try:
            v=Voiting()
            v.vote()
        except AgeValidError as ave:
            print(ave)
        finally :
            print("wait for result")


        ch=input("next votter plz......(y/n)=> ")
        if ch in ('y','Y'):
            continue
        else:
            break
    print("*********************RESULT*************************")
    print("BJP\tCONGRESS\tAAP\tNOTA")
    print(Voiting.Bjp,'\t',Voiting.Congress,'\t\t',Voiting.AAP,'\t',Voiting.nota)
    
    
                
    
