from math import *
import datetime
print("What do you want to do(Type the number for the respective operation):")
print("")
print("")
print("")
print("1.Round off a number")
print("")
print("2.Find square root of a number")
print("")
print("3.Find greatest of two numbers")
print("")
print("4.Addition of two numbers")
print("")
print("5.Subtraction of two numbers")
print("")
print("6.Division of two numbers")
print("")
print("7.Multiplication of two numbers")
print("")
print("8.Know the present date and time")
print("")
print("9.Find the table of any number")
print("")
print("10.Find the smaller of two numbers.")
print("")

a=int(input("Enter the operation: "))
if a==1:
	b=float(input("Enter the number: "))
	print(round(b),end=" is the Estimated number.")

elif (a==2):
	c=int(input("Enter the number: "))
	print(sqrt(c),end=" is the square root of")
	print(c)
    

elif (a==3):
	d=int(input("Enter the first number: "))
	e=int(input("Enter the second number: "))
	print(max(d,e),end=" is the largest number")
   

elif (a==4):
	f=int(input("Enter the first number: "))
	g=int(input("Enter the second number: "))
	x=f+g
	print(x,end=" is the sum.")
    
elif (a==5):
	h=int(input("Enter the first number: "))
	i=int(input("Enter the second number: "))
	if h>i:
		print(h-i,end=" is the difference")

	else:
		print(i-h,end=" is the difference")
	
elif (a==6):
	j=int(input("Enter the first number: "))
	k=int(input("Enter the second number: "))
	if j>k:
		print(j/k,end=" is the quotient")
	else:
		print(k/j,end=" is the quotient")

elif (a==7):
	l=int(input("Enter the first number: "))
	m=int(input("Enter the second number: "))
	print(l*m,end=" is the product")
elif (a==8):
	now=datetime.datetime.now()
	print("Date",end=" :")
	print(now.strftime("%Y-%m-%d"))
	print("Time",end=" :")
	print(now.strftime("%H:%M:%S"))
elif (a==9):
	n=int(input("Enter the number:"))
	for j in range(1,10+1):
		p=n*j
		print(n,end=" x ")
		print(j,end=" = ")
		print(p)
elif (a==10):
	o=int(input("Enter the first number: "))
	p=int(input("Enter the second number: "))
	print(min(o,p),end=" is the smaller of the two numbers")


print("THANKS FOR USING THIS PROGRAM!!!!!!")
print("**************************************************************************************")

   
