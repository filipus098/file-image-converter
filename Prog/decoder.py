import pandas as pd
from PIL import Image


def selectVal(colour):
 for index, row in coloursFrame.iterrows():
     if row[2] == colour[0] and row[3] == colour[1] and row[4] == colour[2]:
         return index


coloursFrame = pd.read_csv("pxls.space palette.csv")

decoded = open("decoded.jpg", 'wb')
image = Image.open("image.png",'r')

string = ''
vals = []
for x in image.getdata():
    val = selectVal(x)
    try:
        binval = bin(val)
        vals.append(binval)
    except TypeError:
        print("end of file")

# TODO fix picutre format errors (decoded picture not being able to be shown)
for x in range(0, len(vals), 2):
    vals[x] = vals[x][2:]
    while len(vals[x]) < 4:
        vals[x] = "0" + vals[x]
    vals[x + 1] = vals[x + 1][2:]
    while len(vals[x + 1]) < 4:
        vals[x + 1] = "0" + vals[x + 1]

    byte = int((vals[x] + vals[x + 1]), 2)
    byte = chr(byte)
    byte = str.encode(str(byte))
    decoded.write(byte)
