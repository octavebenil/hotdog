#on stock tous les figures sur le disk
import matplotlib
matplotlib.use("Agg")

from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
from lenet import LeNet
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import random
import cv2
import os

dataset = './datasets/'
model_path = './models/hotdogs_not_hotdogs.model'
plot = 'plot.png'

#INITIALIZATION
epochs = 25
#Tolérence aux eurreurs ou learning rate
init_lr = 1e-3
batch_size = 32

data = []
labels = []

#on  recupères les images dans le repertoire datasets et on les melanges
imagePaths = sorted(list(paths.list_images(dataset)))
random.seed(42)
random.shuffle(imagePaths)

"""
Traitement des images :
 -on parcours le dossier datasets
 -on ouvre chaque image et on change sa taille en 28x28 px pour que les
 correspondents aux tailles des inputs dans le modèle LeNet
 -on ajoute l'image dans notre tableau data
 -Le nom du dossier parent de l'image correspond aux labels de l'images
 donc hotdogs ou nothotdogs
"""
for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (28,28))
    image = img_to_array(image)
    data.append(image)

    #extraction du label
    label = imagePath.split(os.path.sep)[-2]
    print(label)
    #le label est 1 si le nom du dossier parent de l'image est hotdogs et 0 sinon
    label = 1 if label == "hotdogs" else 0
    labels.append(label)

"""
on va maintenant modifier notre datasets en divisant chaque valeur
du tenseur par 255.0 de façon à avoir des valeurs qui sont comprisent
dans l'intervalle [0, 1]. Ceci pour reduire la taille des valeurs à calculer.
En effet, il serait plus aiser de faire des calculs <=1

On va, par la suite, séparer notre données d'entraitement aux données des tests
"""
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

#repartition en train et test (ici le test represente 25% de notre données)
(trainX, testX, train_labels, test_labels) = train_test_split(data, labels, test_size=0.25, random_state=42)

#on convertisse les labels en vecteurs de type one hote (ie [1 0] ou [0 1] respectivement hotdogs et nothotdogs) avec les nombres de classe à classifier
train_labels  = to_categorical(train_labels, num_classes=2)
test_labels = to_categorical(test_labels, num_classes=2)

"""
Pour augmenter notre datasets, nous allons utiliser le technique du data augmentation
"""
aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
      height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
      horizontal_flip=True, fill_mode="nearest")

"""
PREPARATION DE L'ENTRAINEMENT
"""
"""
initialisation du modèle
Nous allons utiliser le classe LeNet que nous avons crée précedement
Ici l'image à une taille de 28x28 en couleur donc depth=3 et nous avons
deux (02) classes

L'optimiseur que nous alons utiliser durant l'apprentissage est Adam
La fonction de perte est binary_crossentropy puisqu'on a que 02 classes (si > 2)
on utilise plutot categorical_crossentropy

PS: LeNet est un petit réseau de neurone convolutionnel donc plus facile à comprendre
 pour le debutant. Il ne demande pas aussi des GPU pour l'entrainement
"""
print('Compilation du modèle.....')
model = LeNet.build(width=28, height=28, depth=3, classes=2)
#initialisation de l'optimiseur
opt = Adam(lr=init_lr, decay=init_lr/epochs)
model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])

"""
entrainement du réseau
on met paramètre les données augmenter de tout à l'heure
"""
print("Entrainement du réseau")
H = model.fit_generator(aug.flow(trainX, train_labels, batch_size=batch_size),
    validation_data=(testX, test_labels), steps_per_epoch=len(trainX) // batch_size,
    epochs=epochs, verbose=1)

#on enregistre le modèle dans le disk
print("Enregistrement du modèle.....")
model.save(model_path)

#on affiche les différentes information sur l'apprentissage
plt.style.use("ggplot")
plt.figure()
N = epochs
plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, N), H.history["acc"], label="train_acc")
plt.plot(np.arange(0, N), H.history["val_acc"], label="val_acc")
plt.title("Perte et précision de l'apprentissage")
plt.xlabel("Epoch #")
plt.ylabel("Perte/Précision")
plt.legend(loc="lower left")
plt.savefig(plot)
