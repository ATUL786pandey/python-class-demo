from tkinter.messagebox import *
from  tkinter import *
def saverec():
    f=open("Studentinfo1.csv","a+")
    s=fnametxt.get()+','+lnametxt.get()+','+gender.get()+'\n'
    f.write(s)
    f.close()
    showinfo(title="save",message="Record Save Successfully")
    
win=Tk()
win.geometry("500x500+250+70")
win.title("Employee info")
fnamelbl=Label(win,text="First Name",bg="yellow",fg="blue",font=("italic",10))
fnamelbl.grid(column="0",row="0")

lnamelbl=Label(win,text="Last name",bg="yellow",fg="blue",font=("italic",10))
lnamelbl.grid(column="0",row="1")

fnametxt=Entry(win,fg="blue",font=("italic",10))
fnametxt.grid(column="1",row="0")

lnametxt=Entry(win,fg="blue",font=("italic",10))
lnametxt.grid(column="1",row="1")


gender=StringVar()

male=Radiobutton(win,text="male",value="male",variable=gender)
male.grid(column="0",row="2")
female=Radiobutton(win,text="female",value="female",variable=gender)
female.grid(column="1",row="2")

save=Button(win,text="SAVE",bg="red",font=("italic",10),command=saverec)
save.grid(column="1",row="4")



win.mainloop()
