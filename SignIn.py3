from tkinter import *

root=Tk()
root.title("Sign In")
root.geometry("225x100")
nameVar = StringVar()
passVar = StringVar()

NameLabel=Label(root,text="Name")
NameLabel.grid(row=0)
NameEntry=Entry(root,textvariable=nameVar)
NameEntry.grid(row=0,column=1)

PasswordLabel=Label(root,text="Password")
PasswordLabel.grid(row=1)
PasswordEntry=Entry(root,textvariable=passVar)
PasswordEntry.grid(row=1,column=1)


def ReadFile():
	file=open(f"{nameVar.get()}.txt",'r')
	if (file.read()==passVar.get()):
		labelVerified=Label(root,text=f"You are Verified {nameVar.get()}",fg="Blue")
		labelVerified.grid(row=4,columnspan=3)
	else:
		labelNotVerified=Label(root,text=f"You are Not Verified {nameVar.get()}",fg="Red")
		labelNotVerified.grid(row=4,columnspan=3)


SubmitButton=Button(root,text="Sign In",command=ReadFile,bg="Black",fg="White")
SubmitButton.grid(row=3,column=0)



root.mainloop()