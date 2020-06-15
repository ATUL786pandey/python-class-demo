#WAP FOR BOOK MANAGEMENT USING MYSQL DATABASE
import mysql.connector as conn
try:
    dbconn=conn.connect(host="localhost",
                        user="root",passwd="",database="bookmgmt")

    bid=input("Enter the book id=> ")
    bname=input("Enter the book name=> ")
    bprice=float(input("Enter the price of book=> "))
    bauthor=input("Enter book Author=> ")
    bpublish=input("Enter the publish year of book =>")
    sql ="insert into book values('{}','{}','{}','{}','{}')"format(bid,bname,bprice,bauthor,bpublish)
    cur=dbconn.cursor()
    cur.execut(sql)
    if row.count>0:
        print("record Enter Successfully")
    else:
        print("try again statement fail"
    dbconn.comit()
    print("Enter the Query",end=" ")
    sql=input(" ")
    cur.execut(sql)
    data=cur.fetchall()
    for i in data:
              print(i[0],'',i[1],'',i[2],'',i[3],'',i[4])

except Exception as e:
              print(e)
finally:
    dbconn.close()
              
              
              
