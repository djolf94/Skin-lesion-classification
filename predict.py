import numpy as np 
import keras
from keras import backend as K 
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense, Flatten, Dropout, Activation
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
from matplotlib import pyplot as plt 
from sklearn.metrics import confusion_matrix
import itertools
from keras.models import load_model
import cv2
from PIL import Image
from resizeimage import resizeimage

adresa = input('Unesite adresu slike: ')

fd_img = open(adresa, 'rb')
img = Image.open(fd_img)
img = resizeimage.resize_cover(img, [144, 144])
img.save(adresa, img.format)
fd_img.close()
img = cv2.imread(adresa)

print('Ucitavamo model.....')
model = load_model('melanoma.h5')

img = np.expand_dims(img, axis=0)
predvidjanje = model.predict(img)
if predvidjanje[0][0] >= predvidjanje[0][1]:
	predvidjanje = 'YES'
else:
	predvidjanje = 'NO'

print('Rezultat predvidjanja: ' + predvidjanje)







