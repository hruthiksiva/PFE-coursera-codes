from tkinter import *

root = Tk()

def myClick():
	Hello=Label(root,text="I clicked the button")
	Hello.pack()

#Start=Button(root,text="Start",state=DISABLED,fg="blue",bg="red")
Start=Button(root,text="Start",padx=50,pady=50,command=myClick)
Start.pack()

root.mainloop()