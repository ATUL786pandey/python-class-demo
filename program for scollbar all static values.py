from tkinter import *
from tkinter import ttk

win=Tk()
win.geometry("500x500")
data=[["aaa1","aaa2","aaa3"],
      ["bbb1","bbb2","bbb3"],
      ["ccc1","ccc2","ccc3"],
      ["ddd1","ddd2","ddd3"],
      ["eee1","eee2","eee3"]]


frame=Frame(win)
frame.pack()

tree=ttk.Treeview(frame,column=(1,2,3),height=5,show="headings")
tree.pack(side='left')

tree.heading(1,text="column 1")
tree.heading(2,text="column 2")
tree.heading(3,text="column 3")


tree.column(1,width=100)
tree.column(2,width=100)
tree.column(3,width=100)


scroll=ttk.Scrollbar(frame,orient="vertical",command=tree.yview)
scroll.pack(side = 'right', fill = 'y')


tree.configure(yscrollcommand=scroll.set)

for val in data:
    tree.insert('','end',values=(val[0],val[1],val[2]))

win.mainloop()
