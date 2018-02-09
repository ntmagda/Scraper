from __future__ import division
import cv2
import numpy as np
import os


def get_images_list_from_databse(database_path, format):
    for dir_path, dirs, files in os.walk(database_path):
        files = list(filter(lambda x: x.endswith(format), files))
        return files


def read_image(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    print(np.asarray(img).shape)
    return np.asarray(img)


def get_matrix_representing_1DImages(database_path, format="pgm"):
    img_files_list = get_images_list_from_databse(database_path, format)
    imgs_as_arrays = []
    try:
        for img_file_name in img_files_list:
            img_array_2D = read_image(os.path.join(database_path, img_file_name))
            img_array_1D = img_array_2D.ravel()
            imgs_as_arrays.append(img_array_1D)
        return np.array(imgs_as_arrays)
    except TypeError:
        print("DATABASE path not correct")


print(get_matrix_representing_1DImages("../DATABASE_test"))
