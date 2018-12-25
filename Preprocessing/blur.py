import cv2
import numpy as np 
from matplotlib import pyplot as plt 
from os import listdir
import os
import random

folder = '/home/djole/Downloads/MELANOMA/train/NO'
lista_slika = listdir(folder)
for adresa_slike in lista_slika:
    x = random.randint(1, 100)
    if x < 34:
        slika = cv2.imread(folder + '/' + adresa_slike)
        blurovana_slika = cv2.GaussianBlur(slika,(5,5),0)
        os.remove(folder + '/' + adresa_slike)
        cv2.imwrite(folder + '/' + adresa_slike, blurovana_slika)
    else:
        continue

