from PIL import Image
from resizeimage import resizeimage
from os import listdir



folder = '/home/djole/Downloads/MELANOMA/valid/NO'
lista_slika = listdir(folder)
for adresa_slike in lista_slika:
    fd_img = open(folder + '/' + adresa_slike, 'rb')
    img = Image.open(fd_img)
    img = resizeimage.resize_cover(img, [144, 144])
    img.save(folder + '/' + adresa_slike, img.format)
    fd_img.close()