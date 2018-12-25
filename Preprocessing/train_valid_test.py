import os
from os import listdir
from shutil import copyfile
import random

folder = '/home/djole/Downloads/MELANOMA/NO'
lista_slika = os.listdir(folder)

for adresa_slike in lista_slika:
    src = folder + '/' + adresa_slike
    x = random.randint(1, 100)
    if x <= 75:
        dest = '/home/djole/Downloads/MELANOMA/train/NO'
    elif x > 75 and x <= 83:
        dest = '/home/djole/Downloads/MELANOMA/valid/NO'
    elif x > 83:
        dest = '/home/djole/Downloads/MELANOMA/test/NO'
    dest = dest + '/' + adresa_slike
    copyfile(src, dest)


