import keras
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import imageio
import matplotlib.pyplot as plt
from PIL import Image
from os import listdir
import os
import random

transformacija = ImageDataGenerator(rotation_range=359, width_shift_range=-0.1, height_shift_range=-0.1,
                                    zoom_range = 0.1, fill_mode='nearest', horizontal_flip=True,
                                    vertical_flip=True)

folder = '/home/djole/Downloads/MELANOMA/valid/NO'
lista_slika = listdir(folder)
for adresa_slike in lista_slika:
	x = random.randint(1, 100)
	if x <= 66:
		slika = np.expand_dims(imageio.imread(folder + '/' + adresa_slike), 0)
		nove_slike = transformacija.flow(slika)
		augmentovane_slike = [next(nove_slike)[0].astype(np.uint8) for i in range(1)]
		os.remove(folder + '/' + adresa_slike)
		for i in range(1):
		        imageio.imwrite(folder + '/' + adresa_slike, augmentovane_slike[i]) 
	else:
		continue;
