from tkinter import *
from tkinter.filedialog import *

def openFile():
    file=askopenfile(mode='r',filetypes=
                     [('Python Files','*.py'),
                      ('All Files','*.*'),
                      ('Text File','*.txt')])

    if file is not None:
        content=file.read()
        print(content)
        win.title(file.name)
        
        t.insert(1.0,END)


def file_save():
    f=asksaveasfile(mode='w',defaultextension=".txt",
                    filetype=(("Text File","*.txt"),
                                ("All file","*.*")),
                     title="Save as file")
    if f is None:
        return
    win.title(f.name)
    text2save=str(t.get(1.0,END))
    f.write(text2save)
    f.close()




def newFile():
    win.title("new Notepad")
    file=None
    t.delete(1.0,END)
    
def cut():
    t.event_generate("<<Cut>>")

def copy():
    t.event_generate("<<Copy>>")


def paste():
    t.event_generate("<<Paste>>")


win=Tk()
win.geometry("500x500")
win.title("notepad")
menu=Menu(win)
win.config(menu=menu)

filemenu=Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=newFile)
filemenu.add_command(label='open',command=openFile)
filemenu.add_command(label='save',command=file_save)
filemenu.add_separator()
filemenu.add_command(label='Exit',command = win.destroy)


edit=Menu(menu)
menu.add_cascade(label='Edit',menu=edit)
edit.add_command(label='copy',command=copy)
edit.add_command(label='cut',command=cut)
edit.add_command(label='paste',command=paste)

helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')


t=Text(win,width="500",height="500")
t.pack()
win.mainloop()
