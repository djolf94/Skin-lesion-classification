from PIL import Image
from os import listdir

folder = '/home/djole/Downloads/MELANOMA/valid/NO'
lista_slika = listdir(folder)
for adresa_slike in lista_slika:
    slika = Image.open(folder + '/' + adresa_slike).convert('L')
    slika.save(folder + '/' + adresa_slike)