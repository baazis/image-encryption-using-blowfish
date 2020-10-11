from PIL import Image
import math

im = Image.open("s7.png", "r")
arr = im.load() #pixel data stored in this 2D array
w,h=im.size

def rot(A, n, x1, y1): #this is the function which rotates a given block
    temple = []
    for i in range(n):
        temple.append([])
        for j in range(n):
            temple[i].append(arr[x1+i, y1+j])
    for i in range(n):
        for j in range(n):
            arr[x1+i,y1+j] = temple[n-1-i][n-1-j]


xres = w
yres = h
BLKSZ = int(w /4)#blocksize
for i in range(2, BLKSZ+1):
    for j in range(int(math.floor(float(xres)/float(i)))):
        for k in range(int(math.floor(float(yres)/float(i)))):
            rot(arr, i, j*i, k*i)
for i in range(3, BLKSZ+1):
    for j in range(int(math.floor(float(xres)/float(BLKSZ+2-i)))):
        for k in range(int(math.floor(float(yres)/float(BLKSZ+2-i)))):
            rot(arr, BLKSZ+2-i, j*(BLKSZ+2-i), k*(BLKSZ+2-i))

im.save("s7_scrambled.png")


im1=Image.open("s7_scrambled.png","r")
arr1=im1.load()
x=list(im1.getdata())
#print(x)
x1=" ".join(str(a) for a in x)
#print(x1)

from Crypto.Cipher import Blowfish

INPUT_SIZE = 120*120


def pad_string(str):

	new_str = str
	pad_chars = INPUT_SIZE - (len(str) % INPUT_SIZE)

	if pad_chars != 0:
		for x in range(pad_chars):
			new_str += " "
		

	return new_str

plaintext = x1
crypt_obj = Blowfish.new('11010011110111011101110110101110111011100001101', Blowfish.MODE_ECB)
ciphertext = crypt_obj.encrypt(pad_string(plaintext))

print ("PlainText:")
print (plaintext)
print ("CipherText:")
print (ciphertext)
a=ciphertext.split()
arrr=[]
for i in range(0,h):
    arrr.append([])
    for j in range(0,w):
        arrr[i].append(a[j])
#print(arrr)
im1.save("s7_encrypted.png")
im1.show("s7_encrypted.png")

print ("Retriving Original:")
#print (crypt_obj.decrypt(ciphertext))

x2=x1.split()
#print(x2)

arr2=[]
for i in range(0,h):
    arr2.append([])
    for j in range(0,w):
        arr2[i].append(x2[j])
#print(arr2)
xres = w
yres = h
BLKSZ =int( w/4)#blocksize
for i in range(2, BLKSZ+1):
    for j in range(int(math.floor(float(xres)/float(i)))):
        for k in range(int(math.floor(float(yres)/float(i)))):
            rot(arr2, i, j*i, k*i)
for i in range(3, BLKSZ+1):
    for j in range(int(math.floor(float(xres)/float(BLKSZ+2-i)))):
        for k in range(int(math.floor(float(yres)/float(BLKSZ+2-i)))):
            rot(arr2, BLKSZ+2-i, j*(BLKSZ+2-i), k*(BLKSZ+2-i))

im.save("s7_unscrambled.png")
#im.show("unscrambled.png")