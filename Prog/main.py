import bitio
import os
from PIL import Image
import numpy as np
import scipy.misc as smp
import pandas as pd
print("NOTE: you need to have a few python packages installed for this to worked, PIL (or pillow) numpy scipy and pandas")
print("Please put in the path to your file (relative or full both work)")
fileName=input()
coloursFrame = pd.read_csv("pxls.space palette.csv")
print(coloursFrame)

f = open(fileName, 'rb')

# read one byte
string=""
# convert the byte to an integer representation
for i in range(os.path.getsize(fileName)):
    byte = f.read(1)
    print(str(int(i/os.path.getsize(fileName)*100)) + ' % byte converted')
    try:
     byte = ord(byte)
    except:
     byte= 0
    # now convert to string of 1s and 0s
    byte = bin(byte)[2:].rjust(8, '0')
    # now byte contains a string with 0s and 1s
    #TODO maybe a better solution
    for bit in byte:
        string +=bit
w, h = int(np.ceil(np.sqrt(len(string)/4))),int(np.ceil(np.sqrt(len(string)/4)))
data = np.zeros((h, w, 3), dtype=np.uint8)
j=0
#TODO performance improvement
for i in range(0,len(string),4):
    toBinString = string[i:i+4]
    value = int(toBinString,2)
    print(str(int((i+1)*100/len(string))) + " % done")
    if(i/4-j*w>=h):
        j+=1

    data[j,int(i/4)-j*w]=[coloursFrame.iloc[value]["R"],coloursFrame.iloc[value]["G"],coloursFrame.iloc[value]["B"]]

img = Image.fromarray(data,'RGB')       # Create a PIL image

print("where do you want your image saved (just the path)?")
print("WARNING if you have another image.png in your path its going to get overriden")
img.save(input()+"image.png")
img.show()
print("Done! the picture view should pop up and show up in your path, as a tip  recommend viewing it in paint or other editing programms because upscaling works weirdly with small pictures")
