from tkinter import *
import datetime

window=Tk()
topFrame=Frame(window)
topFrame.pack()
bottomFrame=Frame(window)



now = datetime.datetime.now()


a=now.strftime("Current Date:- %Y-%m-%d")
b=now.strftime("Current Time:- %H:%M:%S")


def printDate():
	w=Label(window,text=a)
	w.pack()

def Time():
	l=Label(window,text=b)
	l.pack()
button1 = Button(topFrame, text="Know The Date", command=printDate, fg="Blue")
button2 = Button(topFrame, text="Know The Time", command=Time, fg="Red")
button1.pack()
button2.pack()


window.mainloop()
