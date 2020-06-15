#WAP FOR BANK CUSTOMER USING MYSQL DATABASE
import mysql.connector as conn
try:
    dbconn=conn.connect(host="localhost",
                        user="root",
                        passwd="",
                        database="customermgmt")

    custid=input("Enter customer id=> ")
    custname=input("Enter customer name => ")
    custmobile=int(input("Enter customer mobile no=> "))
    custemail=input("Enter customer Email id=> ")

    sql="insert into customer values('{}','{}','{}','{}')"format(custid,custname,custmobile,custemail)
    cur=dbconn.cursor()
    cur.execut(sql)
    if row.count>0:
        print("record enter Successfully")
    else:
        print("try again statement fail")
    dbconn.comit()
    print("Enter the Query",end=" ")
    sql=input(" ")
    cur.execut(sql)
    data=cur.fetchall()
    for i in data:
        print(i[0],' ',i[1],'',i[2],'',i[3])

except Exception as e:
    print(e)
finally:
    dbconn.close()
    
