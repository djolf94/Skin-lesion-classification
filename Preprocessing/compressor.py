import os
from os import listdir
from PIL import Image

folder = '/home/djole/Downloads/MELANOMA/test/NO'
lista_slika = listdir(folder)
for adresa_slike in lista_slika:
        info = os.stat(folder + '/' + adresa_slike);
        if info.st_size > 1000000 and info.st_size <= 5000000:
            slika = Image.open(folder + '/' + adresa_slike)
            os.remove(folder + '/' + adresa_slike)
            slika.save(folder + '/' + adresa_slike, quality = 65, optimize=True)
        elif info.st_size > 5000000 and info.st_size <= 10000000:
            slika = Image.open(folder + '/' + adresa_slike)
            os.remove(folder + '/' + adresa_slike)
            slika.save(folder + '/' + adresa_slike, quality = 55, optimize=True)
        elif info.st_size > 10000000 and info.st_size <= 15000000:
            slika = Image.open(folder + '/' + adresa_slike)
            os.remove(folder + '/' + adresa_slike)
            slika.save(folder + '/' + adresa_slike, quality = 45, optimize=True)
        elif info.st_size > 15000000:
            slika = Image.open(folder + '/' + adresa_slike)
            os.remove(folder + '/' + adresa_slike)
            slika.save(folder + '/' + adresa_slike, quality = 35, optimize=True)

brojac = 0
for adresa_slike in lista_slika:
    info = os.stat(folder + '/' + adresa_slike)
    if info.st_size > 600000:
        os.remove(folder + '/' + adresa_slike)
        brojac += 1
print('Izbrisali smo ' + str(brojac) + ' slika koje su bile vece od 600kB')
