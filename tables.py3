n=int(input("Enter the number whose table is to be found: "))                                                                                                                    
f=int(input("Enter the number till where the table is to be found: ")) 
for i in range(1,f+1):
	a=n*i
	print(n, end =" x ")
	print(i, end =" = ")
	print(a)
print("Thanks for using this program!")