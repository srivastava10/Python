from tkinter import *
window=Tk()
window.title("Register")
window.geometry("225x100")
NameVar = StringVar()
PassVar = StringVar()



nameLabel=Label(window,text="Name")
nameLabel.grid(row=0)
nameEntry=Entry(window,textvariable=NameVar)
nameEntry.grid(row=0,column=1)

passwordLabel=Label(window,text="Password")
passwordLabel.grid(row=1)
passwordEntry=Entry(window,textvariable=PassVar)
passwordEntry.grid(row=1,column=1)


def Submission():
	file=open(f"{NameVar.get()}.txt",'w')
	file.write(PassVar.get())
	file.close()
	LabelRegistered=Label(window,text=f"You Have Successfully Registered As {NameVar.get()}",fg="Blue")
	LabelRegistered.grid(row=4,columnspan=4)
RegisterButton=Button(window,text="Register",command=Submission,fg="White",bg="Black")
RegisterButton.grid(row=3,columnspan=2)



window.mainloop()