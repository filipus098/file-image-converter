
import os
import threading
import time

import numpy as np
import pandas as pd
from PIL import Image


def showProgress():
    global threadsStarted
    while (int(threadsStarted / int(leng)) * 100) < 100:
        print(str(int((threadsStarted / int(leng)) * 100)) + "% threads started")
        time.sleep(1)


def evalPxl(i):
    j = 0
    toBinString = string[i:i + 4]
    i = i / 4
    while i >= h:
        j += 1
        i = i - w
    value = int(toBinString, 2)
    data[j, int(i)] = [coloursFrame.iloc[value]["R"], coloursFrame.iloc[value]["G"], coloursFrame.iloc[value]["B"]]


print("NOTE: you need to have a few python packages installed for this to worked, PIL (or pillow) numpy and pandas")
print("Please put in the path to your file (relative or full both work)")
fileName = input()
coloursFrame = pd.read_csv("pxls.space palette.csv")

f = open(fileName, 'rb')

# read one byte
string = ""
# convert the byte to an integer representation
# TODO Threads would be good but effort
for i in range(os.path.getsize(fileName)):
    byte = f.read(1)
    print(str(int(i/os.path.getsize(fileName)*100)) + ' % byte converted')
    try:
        byte = ord(byte)
    except:
        byte = 0
    # now convert to string of 1s and 0s
    byte = bin(byte)[2:].rjust(8, '0')
    # now byte contains a string with 0s and 1s
    #TODO a better solution
    for bit in byte:
        string += bit
w, h = int(np.ceil(np.sqrt(len(string)/4))),int(np.ceil(np.sqrt(len(string)/4)))
data = np.zeros((h, w, 3), dtype=np.uint8)

#TODO performance improvement

threadsStarted = 0
leng = int(len(string) / 4)
progress = threading.Thread(target=showProgress)
progress.start()

for i in range(0,len(string),4):
    curr = threading.Thread(target=evalPxl, args=[i])
    curr.start()
    threadsStarted += 1

while threading.active_count() != 1:
    print(str(int(threading.active_count())) + " threads alive")
    time.sleep(2)
img = Image.fromarray(data, 'RGB')  # Create a PIL image

print("where do you want your image saved (just the path)?")
print("WARNING if you have another image.png in your path its going to get overriden")
img.save(input()+"image.png")
img.show()
print("Done! the picture view should pop up and show up in your path,"
      " as a tip  recommend viewing it in paint or other editing programms "
      "because upscaling works weirdly with small pictures")
