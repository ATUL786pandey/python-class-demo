import mysql.connector as conn
#create connection between python and mysql
try:
    dbconn=conn.connect(host="localhost",
                        user="root",
                        passwd="",
                        database="employeemgmt")
    eid=input("Enter Employee Id=> ")
    ename=input("Enter the employee name=> ")
    salary=float(input("Enter the Salary=> "))
    designation=input("Enter the Designation=> ")

    sql="insert into emp value('{}','{}','{}','{}')"format(eid,ename,salary,designation)
    cur=dbconn.cursor()
    cur.execute(sql)
    if cur.rowcount>0:
        print("record inserted Successfully ")
    else:
        print("try again statement fail ")
    dbconn.comit()
    print("Enter the query",end="")
    sql=input(" ")
    cur.execut(sql)
    data=cur.fetchall()
    for i in data:
        print(i[0],' ',i[1],' ',i[2],' ',i[3])

except Exception as e:
    print(e)

finally:
    dbconn.close()
