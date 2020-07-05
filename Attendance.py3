import datetime
c=0
onRoll=int(input("Enter the total strength of the class:"))
now=datetime.datetime.now()
a=now.strftime(" Date:- %Y-%m-%d")
b=now.strftime(" Time:- %H:%M:%S")
for i in range(1,onRoll+1):
	Name=str(input("Name:"))
	check=str(input("Present or Absent"))
	if (check=="Present"):
		print(f"{Name} is present")
		c=c+1
	else:
		print(f"{Name} is absent")
ab=onRoll-c

data1=f"Total strength: {onRoll}"
data2=f"Children Present: {c}"
data3=f"Children Absent: {ab}"
file=str(input("Enter the file name where the data has to be saved."))
savefile=open(file,'w')
savefile.write(a)
savefile.write(" ")
savefile.write(b)
savefile.write(" ")
savefile.write(data1)
savefile.write(" ")
savefile.write(data2)
savefile.write(" ")
savefile.write(data3)
savefile.close()
print("The file has been successfully saved!")
