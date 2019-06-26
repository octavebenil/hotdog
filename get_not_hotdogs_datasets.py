from imutils import paths
import requests
import os
import cv2

output = "./datasets/nothotdogs/"
url_list_filename = "./urls_not_hotdogs.txt"
total = 0
with open(url_list_filename, 'rt') as f:
    raws = f.read().strip().split("\n")

if len(raws) > 0:
    for url in raws:
        try:
            #on télécharge l'image
            r = requests.get(url, timeout=60)

            img_path = os.path.sep.join([output, "{}.jpg".format(str(total).zfill(8))])

            f = open(img_path, "wb")
            f.write(r.content)
            f.close()

            print("Image {} téléchargé".format(img_path))
            total += 1
        except:
            print('Url mort.')

#on ouvre les images et on efface les corrompus
for imagePath in paths.list_images(output):
    delete = False

    try:
        image = cv2.imread(imagePath)

        if image is None:
            delete = True
    except:
        print('Erreur, continuons..')
        delete = True

    if delete:
        print("Effacement de {}".format(imagePath))
        os.remove(imagePath)
