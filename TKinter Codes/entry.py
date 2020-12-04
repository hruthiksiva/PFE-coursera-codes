from tkinter import *

root =Tk()

def myClick():
	#myLabel=Label(root,text=e.get())
	#myLabel=Label(root,text="Hello " +e.get())
	Hello="Hello "+ e.get()
	myLabel=Label(root,text=Hello)
	myLabel.pack()

#e=Entry(root,width=50,bg="blue",fg="white")
e=Entry(root,width=50,borderwidth=5)
e.pack()
e.insert(0, "Enter your name")

click=Button(root,text="Start",command=myClick)
click.pack()

root.mainloop()