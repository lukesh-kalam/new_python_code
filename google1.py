import builtins
from tkinter import *
import webbrowser

win=Tk()
win.title("Search Bar")

def search() :
    url=Entry.get()
    webbrowser.open(url)

label1 = Label(win,text="Enter URL here   : " ,font=("arial",10,"bold"))

label1.grid(row=0,column=0)

Entry = Entry(win,width=30)
Entry.grid(row=0,column=1)

button = Button(win,text="search",command=search)
button.grid(row=1,column=0,columnspan=2,pady=10)

win.mainloop()
