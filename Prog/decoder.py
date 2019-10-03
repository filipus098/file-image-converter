import bitio
import os
from PIL import Image
import numpy as np
import scipy.misc as smp
import pandas as pd

def selectVal(colour):
 for index, row in coloursFrame.iterrows():
    if(row[2]==colour[0], row[3]==colour[1], row[4]==colour[2]):
        return coloursFrame.index[row[0]]


coloursFrame = pd.read_csv("pxls.space palette.csv")

decoded = open("decoded", 'wb')
image = Image.open("image.png",'r')


for x in image.getdata():
    val = selectVal(x)
    print(val)
#TODO finish decoder