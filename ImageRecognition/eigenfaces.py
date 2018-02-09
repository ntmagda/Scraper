from ImageRecognition.normalization import normalize_imgs, get_matrix_representing_1DImages, show_img_from_1D_vector
import numpy as np
from numpy import linalg as LA
import scipy.misc
import os

imgs_as_arrays = get_matrix_representing_1DImages("../DATABASE_faces")
normalized_imgs_as_arrays = normalize_imgs(imgs_as_arrays)

def calculate_eignenfaces(matrix):
    eigenvalues, eigenvector = LA.eig(np.dot(matrix.T,matrix))
    return eigenvalues, eigenvector


def save_eigenfaces_to_dir(normalized_imgs_as_arrays):
    (eigenvalues, eigenvector) = calculate_eignenfaces(normalized_imgs_as_arrays)
    cnt = 0
    for eigenface in eigenvector.T:
        cnt+=1
        eigenface = eigenface.real
        eigenface *= (255.0/eigenface.max())
        arr2 = np.asarray(eigenface).reshape((101,101))
        scipy.misc.imsave(os.path.join("../EIGENFACES", cnt.__str__() + ".jpg"), arr2)

save_eigenfaces_to_dir(normalized_imgs_as_arrays)
# show_img_from_1D_vector(v)
# print(eigenvalues)
