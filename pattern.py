import time
n=int(input("Enter a number: "))
for i in range(1,n+1):
	for j in range(1,i+1):
		for k in range(1,j+1):
			time.sleep(0.1)
			print('*',end="")
		print(j)
	print('')