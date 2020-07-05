import random
import urllib.request
img=str(input("Enter the image address"))
def downloadImage(url):
	name= random.randrange(1,1000)
	fullName= str(name) +".jpg"
	urllib.request.urlretrieve(url, fullName)
downloadImage(img)