age = int(input("Enter your age to know whether you can vote or not: "))
name = str(input("Enter your name: "))
if age>=18:
	print("You can vote ",name)
	print("Congrats!")
else:
	print("You can not vote ",name)
	print("So sad!!")
