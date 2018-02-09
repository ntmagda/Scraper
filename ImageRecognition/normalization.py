from PIL import Image
from ImageRecognition.preparing_database import read_image, get_matrix_representing_1DImages
import numpy as np
import os
import scipy.misc

# dirpath = "../DATABASE_test"
dirpath_faces = "../DATABASE_faces"
shape_g = (101,101)


def get_shape_of_original_image(file_path):
    # check if images have the same shape
    return read_image(file_path).shape

def calculate_avarage_face_vector(imgs_as_arrays):
    return np.mean(imgs_as_arrays, axis=0)

def show_avarage_face(database, shape=shape_g):
    imgs_as_arrays = get_matrix_representing_1DImages(database)
    average_face = calculate_avarage_face_vector(imgs_as_arrays)
    arr2 = np.asarray(average_face).reshape(shape)
    img2 = Image.fromarray(arr2)
    img2.show()

def show_img_from_1D_vector(vector, shape=shape_g):
    arr2 = np.asarray(vector).reshape(shape)
    img2 = Image.fromarray(arr2)
    img2.show()


def normalize_imgs(img_as_arrays):
     avarage_face = calculate_avarage_face_vector(img_as_arrays)
     normlized_faces = img_as_arrays - avarage_face
     cnt = 0
     for n_face in normlized_faces:
         cnt+=1
         arr2 = np.asarray(n_face).reshape(shape_g)
         scipy.misc.imsave(os.path.join("../DATABASE_normalized", cnt.__str__()+".jpg"), arr2)
     return normlized_faces



# show_avarage_face(dirpath_faces)
# img_as_arrays = get_matrix_representing_1DImages(dirpath_faces)
# normalize_imgs(img_as_arrays)
