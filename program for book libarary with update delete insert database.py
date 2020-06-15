import mysql.connector as conn
class Book:
    def __init__(self):
        self.bid=None
        self.bname=None
        self.bprice=None
        self.bauthor=None
        self.bpub=None
    def openconn(self):
        self.db=conn.connect(host="localhost",user="root",
                             passwd="",database="libmgmtsys")

    def closeconn(self):
        self.db.close()

    def insertrec(self):
        self.bid=int(input("Enter the book id:- "))
        self.bname=input("Enter book Name :- ")
        self.bprice=float(input("Enter the price:- "))
        self.bauthor=input("Enter the Author:- ")
        self.bpub=input("Enter book publication:- ")
        sql="insert into book values('{}','{}','{}','{}','{}')".format(self.bid,self.bname,self.bprice,self.bauthor,self.bpub)
        cur=self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        self.closeconn()
        if cur.rowcount>0:
            return True
        else:
            return False
    
    def updaterec(self,bid):
        sel.openconn()
        bname=input("Enter new Name:- ")
        bprice=float(input("Enter the new price:- "))
        bauthor=input("Enter new author:- ")
        bpub=input("Enter new publication:- ")
        sql="update book set bname='{}',bprice='{}',bauthor='{}',bpub='{}' where bid ={}".format(bname,bprice,bauthor,bpub,bid)
        cur=self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        self.closeconn()
        if cur.rowcount>0:
            return True
        else:
            return False

    def deleterec(self,bname):
        self.openconn()
        sql="select * from book where bname='{}'".formate(bname)
        cur=self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        self.closeconn()
        if cur.rowcount>0:
            return True
        else:
            return False

    def searchrec(self,bname):
        self.openconn()
        sql="select * from book where bname='{}'".format(bname)
        cur=self.db.cursor()
        cur.execute(sql)
        data=cur.fetchone()
        print("bid\tbnsme\tbprice\tbauthor\tbpub")
        for i in data:
            print(i,end="\t")
            self.closeconn()



    def showallrec(self):
        sel.openconn()
        sql="select * from book "
        cur=self.db.cursor()
        cur.execute(sql)
        data=cur.fetchall()
        for i in data:
            print(i[0],' ',i[1],' ',i[2],' ',i[3],' ',i[4])
        print("\n\n\n\n\n")
        self.closeconn()

def main():
    while True:
        b=Book()
        print("\n\n\n1 Insert\n2 Update\n3 Delete\n4 search Book\n5 Showall")
        ch=int(input("Enter your Choice :  "))
        if ch==1:
            if b.insertrec():
                print("Record add sucessfully !")
            else:
                print("Try Again")

        elif ch==2:
            bid=int(input("Enter book Id : "))
            if b.udaterec(bid):
                print("updated successfully")

        elif ch==3:
            bid=int(input("Enter book id you want to delete: "))
            if b.deleterec(bid):
                print("Record deleted Successfully..0 errors")
            else:
                print("try again")
        elif ch==4:
            bname=input("Enter the book name you want to search: ")
            b.searchrec(bname)

        elif ch==5:
            b.showallrec()

main()
           
