from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras import backend as K

class LeNet:
    """
    Le modèle : Içi c'est l'architecture LetNet qui est un
    classifier d'image à base de Reseau convolutionnel. Il est
    originalement crée pour le classement des caractères numériques
     écrites à la main.
     Son architecture est composé de :
        - 1 couche de neurone convolutionnel
        - 1 Couche de Pooling
        - 1 couche de neurone convolutionnel
        - 1 couche de Pooling
        - 1 couche de neurone complement connected ou Fully-connected layer
        - Afin la couche d'activation
    """
    @staticmethod
    def build(width, height, depth, classes):
        """
        width: largeur de l'image
        height: hauteur de l'image
        depth: nombre de canal de l'image, 1 pour noir et blanc et 3 pour image couleur
        classes: le nombre total de classe a reconnaître (içi c'est 2 (hotdog et pas hotdog) )
        """
        #initialisation du modèle
        model = Sequential()
        inputShape = (height, width, depth)

        if K.image_data_format() == "channels_first":
            inputShape = (depth, height, width)

        #ajout et definition des différentes couches de neurones
        """
        premier couche convolutionnel avec (CONV => RELU => POOL) :
          - 20 filtre avec une dimension 5x5
          - Activation relu
          - Pooling avec maxPool 2x2
        """
        model.add(Conv2D(20, (5,5), padding="same", input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        """
        2ème couche convolutionnel avec (CONV => RELU => POOL) :
          - 50 filtre avec une dimension 5x5
          - Activation relu
          - Pooling avec maxPool 2x2
        """
        model.add(Conv2D(50, (5,5), padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        """
        Fully connected layer avec une couche d'activation RELU
        Ici on prend d'abord la sortie du 2ème couche et on convertisse
        avec la fonction Flatten() en un vecteur pour pouvoir l'utiliser
        dans notre réseau de neurone completement connécté ou Fully connected
        Neural network sur 500 neurones
        On applique par la suite une activation RELU
        """
        model.add(Flatten())
        model.add(Dense(500))
        model.add(Activation("relu"))

        """
        Couche de sortie : Softmax (0, 0) => (1, 0) ou (0, 1) respectivement hotdog ou pas hotdog
        """
        model.add(Dense(classes))
        model.add(Activation("softmax"))

        return model
