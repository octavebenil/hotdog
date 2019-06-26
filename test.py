from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import imutils
import cv2
import argparse

model_path = "./models/hotdogs_not_hotdogs.model"

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--test", required=True,
	help="Chemin de l'image à évaluer")

args = vars(ap.parse_args())

image_test = args["test"]

#on charge l'image
image = cv2.imread(image_test)
orig = image.copy()

image = cv2.resize(image, (28, 28))
image = image.astype("float") / 255.0
image = img_to_array(image)
#on ajoute une dimension a notre image de façon à avoir (1, width, height, 3) paramètres necessaire au fonction predict de notre modèle
image = np.expand_dims(image, axis=0)

#on charge le modèle
print("Chargement du modèle....")
model = load_model(model_path)

#classification de notre image
(nothotdog, hotdog) = model.predict(image)[0]

print((nothotdog, hotdog))

#preparation du label
label = "HotDog" if hotdog > nothotdog else "Not Hot Dog"
proba = hotdog if hotdog > nothotdog else nothotdog
label = "{}: {:.2f}%".format(label, proba*100)

# on affiche les images
output = imutils.resize(orig, width=400)
cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)

cv2.imshow("Prediction", output)
cv2.waitKey(0)
