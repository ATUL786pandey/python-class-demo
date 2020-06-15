
#*** WAP TO PRINT MARKSHEET OF THE STUDENT****
name=input("Enter your name => ")
course=input("Enter your course detail => ")
cls=input("Enter your class name => ")
e=int(input("enter mark obtain in English => "))
h=int(input("enter mark obtain in Hindi =>"))
m=int(input("enter mark obtain in Marathi =>"))
mths=int(input("enter mark obtain in Maths =>"))
sc=int(input("enter mark obtain in Science =>"))
co=int(input("enter mark obtain in Computer =>"))

total=e+h+m+mths+sc+co
per=(total/600)*100

if per >=40 and per <=50:
    grade="pass class"
elif per>50 and per <60:
    grade= "second class"
elif per >60 and per <70:
    grade="first class"
elif per >70 and per <75:
    grade="distinct"
elif per > 75 and per <=100:
    grade="super distinct"
else:
    grade="fail"

print("***************MarkSheet*********************")
print("Name:- {} \t".format(name))
print("Course:-{} \t".format(course))
print("Class:- {}\t".format(cls))
print("**************Mark obtain in  subject********")
print("English \t 100 \t\t{}".format(e))
print("Hindi   \t 100 \t\t{}".format(h))
print("Marathi \t 100 \t\t{}".format(m))
print("Maths   \t 100 \t\t{}".format(mths))
print("Science \t 100 \t\t{}".format(sc))
print("Computer\t 100 \t\t{}".format(co))
print("********************************************")
print("Total \t\t 600 \t\t{}".format(total))
print("Percentage {:.2f}".format(per))
print("Result :- {} ".format(grade))
