from tkinter.messagebox import *
from tkinter import *
win=Tk()
win.geometry("500x500+250+70")
win.title("Student info")
namelbl=Label(win,text="Student Name",font=("italic",10))
namelbl.grid(column="0",row="0")

nametxt=Entry(win,font=("italic",10))
nametxt.grid(column="1",row="0")

courselbl=Label(win,text="Course Name",font=("italic",10))
courselbl.grid(column="0",row="1")

coursetxt=Entry(win,font=("italic",10))
coursetxt.grid(column="1",row="1")

doblbl=Label(win,text="Date of Birth",font=("italic",10))
doblbl.grid(column="0",row="2")

dobtxt=Entry(win,font=("italic",10))
dobtxt.grid(column="1",row="2")

moblbl=Label(win,text="Mobile no",font=("italic",10))
moblbl.grid(column="0",row="3")

mobtxt=Entry(win,font=("italic",10))
mobtxt.grid(column="1",row="3")

addlbl=Label(win,text="Address",font=("italic",10))
addlbl.grid(column="0",row="4")

Textbox=Text(win,height=5,width=20,font=("italic",10))
Textbox.grid(column="1",row="4")

emaillbl=Label(win,text="Email Id",font=("italic",10))
emaillbl.grid(column="0",row="5")

emailtxt=Entry(win,font=("italic,bold",10))
emailtxt.grid(column="1",row="5")

save=Button(win,text="Save",font=("italic",10))
save.grid(column="0",row="6")

update=Button(win,text="update",font=("italic",10))
update.grid(column="1",row="6")

delete=Button(win,text="Delete",font=("italic",10))
delete.grid(column="2",row="6")

clear=Button(win,text="Clear",font=("italic",10))
clear.grid(column="3",row="6")




win.mainloop()
