import mysql.connector as conn

try:
    dbconn=conn.connect(host="localhost",
                        user="root",passwd="",
                        database="vehiclemgmt")
    vmodel=input("Enter Vehicle model=> ")
    vprice=float(input("Enter the vehicle price=> "))
    vengine=input("Enter the Engine no=> ")

    sql="insert into vehicle values ('{}','{}','{}')"format(vmodel,vprice,vengine)
    cur=dbconn.cursor()
    cur.execut(sql)
    if row.count>0:
        print("record enter successfully")
    else:
        print("try again statement fail")
    dbconn.comit()
    print("Enter the Query",end=" ")
    sql=input(" ")
    cur.execut(sql)
    data=cur.fetchall()
    for i in data:
        print(i[0],'',i[1],'',i[2])
except Exception as e:
    print(e)

finally:
    dbconn.close()
