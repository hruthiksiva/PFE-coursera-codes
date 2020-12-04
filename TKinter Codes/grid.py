from tkinter import *

root=Tk()

FirstName = Label(root,text="Hruthik")
LastName = Label(root,text="Sivakumar")

#FirstName = Label(root,text="Hruthik").grid(row=0,column=0)
#LastName = Label(root,text="Sivakumar").grid(row=1,column=1)

FirstName.grid(row=0,column=0)
LastName.grid(row=1,column=1)

root.mainloop()