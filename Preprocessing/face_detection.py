import os
import cv2
import matplotlib.pyplot as plt

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

images =[]
for root, dirs, files in os.walk('images'):
    for filename in files:
        images.append(filename)

for image_filename in images:
    try:
        test1 = cv2.imread('images/%s' % image_filename)
        gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
        cv2.CascadeClassifier()
        lbp_face_cascade = cv2.CascadeClassifier('lpb_frontalface')
        faces = lbp_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

        if len(faces) > 0:
            print('Faces found: ', len(faces))
            for (x, y, w, h) in faces:
                cv2.rectangle(test1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                plt.imshow(convertToRGB(test1))
                plt.show()
    except:
        print(image_filename)
        pass