#WAP FOR STUDENTMGMT WITH MYSQL DATABASE
import mysql.connector as conn
try:
    dbconn=conn.connect(host="localhost",
                        user="root",
                        passwd=" ",
                        database="studentmgmt")
    srollno=input("Enter the Student rollno => ")
    sname=input("Enter the Student name=> ")
    scourse=input("Enter the Student course=> ")
    smobile=int(input("Enter the Student mobile no=> "))

    sql="insert into student value('{}','{}','{}','{}')"format(srollno,sname,scourse,smobile)
    cur=dbconn.cursor()
    cur.execut(sql)
    if row.count>0:
        print("record Enter Successfully")
    else:
        print("try again statement fail")
    dbconn.comit()
    print("Enter the Query",end=" ")
    sql=input(" ")
    cur.execte(sql)
    data=cur.fetchall()
    for i in data:
        print(i[0],' ',i[1],' ',i[2],' ',i[3])

except Exception as e:
    print(e)

finally:
    dbconn.close()
    
