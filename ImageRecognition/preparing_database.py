from __future__ import division
import cv2
import numpy as np
import os
from PIL import Image

def get_images_list_from_databse(database_path, format):
    for dir_path, dirs, files in os.walk(database_path):
        files = list(filter(lambda x: x.endswith(format), files))
        return files

def get_shape_of_original_image(file_path):
    # check if images have the same shape
    return read_image(file_path).shape

def read_image(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    return np.asarray(img)

def get_images_as_list_of_arrays_1D(database_path, format="pgm"):
    img_files_list = get_images_list_from_databse(database_path, format)
    imgs_as_arrays = []
    try:
        for img_file_name in img_files_list:
            img_array_2D = read_image(os.path.join(database_path, img_file_name))
            img_array_1D = img_array_2D.ravel()
            imgs_as_arrays.append(img_array_1D)
        return imgs_as_arrays
    except TypeError:
        print("DATABASE path not correct")


def calculate_avarage_face_vector(imgs_as_arrays):
    print(type(imgs_as_arrays))
    return [sum(e) / len(e) for e in zip(*imgs_as_arrays)]

shape = get_shape_of_original_image("test.pgm")
print(shape)

imgs_as_arrays = get_images_as_list_of_arrays_1D("../DATABASE")
average_face = calculate_avarage_face_vector(imgs_as_arrays)
arr2 = np.asarray(average_face).reshape(shape)
img2 = Image.fromarray(arr2)
img2.show()