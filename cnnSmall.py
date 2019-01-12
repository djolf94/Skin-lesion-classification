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

folder_u_kome_se_nalazi_dataset_folder = '/home/djole/Downloads/MELANOMA/'

trening_skup = folder_u_kome_se_nalazi_dataset_folder + 'dataset/train'
validacioni_skup = folder_u_kome_se_nalazi_dataset_folder + 'dataset/valid'
test_skup = folder_u_kome_se_nalazi_dataset_folder + 'dataset/test'

#remove color_mode for RGB images
trening_gomila = ImageDataGenerator().flow_from_directory(trening_skup, target_size=(144, 144),
                    classes=['YES', 'NO'], batch_size=32, color_mode='grayscale')
validaciona_gomila = ImageDataGenerator().flow_from_directory(validacioni_skup, target_size=(144, 144),
                    classes=['YES', 'NO'], batch_size=32, color_mode='grayscale')
test_gomila = ImageDataGenerator().flow_from_directory(test_skup, target_size=(144, 144),
                    classes=['YES', 'NO'], batch_size=32, color_mode='grayscale', shuffle = False)


model = Sequential()

#change input shape to (144, 144, 3) for RGB images
model.add(Conv2D(32, (3,3), padding = 'same', input_shape=(144, 144, 1)))
model.add(Activation('relu'))
model.add(Conv2D(32, (3,3), padding = 'same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.1))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.1))


model.add(Conv2D(128, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(256, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.15))

model.add(Conv2D(256, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(512, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.15))

model.add(Flatten())

model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dropout(0.5))


model.add(Dense(2))
model.add(Activation('softmax'))


opt = keras.optimizers.Adam(lr=0.0001)

model.compile(loss = 'categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

model.fit_generator(trening_gomila, steps_per_epoch = 280, validation_data = validaciona_gomila,
                    validation_steps = 30, epochs = 30, verbose = 2)


model.save('melanoma.h5')

test_slike, test_oznake = next(test_gomila)
for i in range(64):
    test_slike1, test_oznake1 = next(test_gomila)
    test_oznake = np.vstack((test_oznake, test_oznake1))

predvidjanja = model.predict_generator(test_gomila, steps = 65, verbose = 2)

test_oznake = test_oznake[:,0]
for i in predvidjanja:
	if i[0] >= i[1]:
		i[0] = 1
	else:
		i[0] = 0
cm = confusion_matrix(test_oznake, predvidjanja[:,0])

#funkcija copy-paste-ovana sa scikit-learn.org
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix'):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest')
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
    plt.show()


cm_plot_oznake = ['YES', 'NO']
plot_confusion_matrix(cm, cm_plot_oznake, title='Matrica konfuzije')



