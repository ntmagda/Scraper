import cv2
import os
import matplotlib.pyplot as plt
from ImageRecognition.preparing_database import get_images_list_from_databse

dirpath = "../DATABASE_test"
files = get_images_list_from_databse(dirpath, "pgm")

def detect_faces_in_database(dirpath_in, dirpath_out):
    faces_counter = 0
    #TODO fix mw mh
    (mw, mh) = calculate_avarage_size_of_face(dirpath_in)
    print("dupa")
    print(mw,mh)
    for f in files:
        face = detect_face(os.path.join(dirpath, f))
        faces_counter += len(face)
        if len(face) != 1:
            path = os.path.join(dirpath, f)
            os.unlink(path)
        else:
            img = cv2.imread(os.path.join(dirpath, f))
            [x, y, w, h] = face[0]
            crop_img = img[y:y + h, x:x + w]
            resize_image = cv2.resize(crop_img, (50, 50))
            cv2.imwrite(os.path.join(dirpath_out, f), resize_image)
    return faces_counter/len(files)


def calculate_avarage_size_of_face(dirpath_in):
    h_buffer = 0
    w_buffer = 0
    face_counter = 0
    for f in files:
        faces = detect_face(os.path.join(dirpath_in, f))
        if len(faces) == 1:
            [_, _, h, w] = faces[0]
            face_counter += 1
            h_buffer += h
            w_buffer += w
        else:
            print("not correct amount of faces on the picture")
            print(f)
            break
    mean_h = h_buffer/face_counter
    mean_w = w_buffer/face_counter
    return (int(mean_h), int(mean_w))



def detect_face(image_path):
    test1 = cv2.imread(image_path)
    gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray_img, cmap='gray')

    cv2.CascadeClassifier()
    lbp_face_cascade = cv2.CascadeClassifier('lpb_frontalface')
    faces = lbp_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);
    print('Faces found: ', len(faces))
    return faces

#calculate percentage of face detection correctnes::

def mark_detected_face(image_path, faces):
    test1 = cv2.imread(image_path)
    for (x, y, w, h) in faces:
        cv2.rectangle(test1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    plt.imshow(test1)
    plt.show()

# image_path = "../DATABASE_test/BioID_0256.pgm"
# mark_detected_face(image_path, detect_face(image_path))

dirpath_out = "../DATABASE_faces_50"
print(detect_faces_in_database(dirpath, dirpath_out))
# print(calculate_avarage_size_of_face(dirpath))