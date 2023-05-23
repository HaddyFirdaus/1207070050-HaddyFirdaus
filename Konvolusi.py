import matplotlib.pyplot as plt#mengimpor library Matplotlib
#%matplotlib inline

from skimage import data#mengimpor modul data dari library scikit-image (skimage)
from skimage.io import imread#mengimpor fungsi imread dari modul skimage.io dalam paket scikit-image
from skimage.color import rgb2gray #engimpor fungsi rgb2gray dari modul skimage.color dalam paket scikit-image. 
import numpy as np#mengimpor library NumPy,
import cv2#mengimpor library OpenCV 

citra1 = cv2.imread("satoru.jpg",cv2.IMREAD_GRAYSCALE)#Membaca citra dengan nama file "satoru.jpg" dalam mode grayscale menggunakan fungsi cv2.imread() dari OpenCV
print(citra1.shape)#Menampilkan dimensi citra citra1 menggunakan atribut shape. 

plt.imshow(citra1, cmap='gray')#Menampilkan citra grayscale citra1 menggunakan plt.imshow() dari matplotlib.

kernel = np.array([[-1, 0, -1], 
                   [0, 4, 0], 
                   [-1, 0, -1]])#Mendefinisikan kernel atau filter yang akan digunakan dalam operasi filter linear. Kernel ini merupakan matriks 3x3 yang memiliki nilai tertentu. 

citraOutput = cv2.filter2D(citra1, -1, kernel)#

fig, axes = plt.subplots(1, 2, figsize=(12, 12))#untuk membuat grid subplot dengan ukuran 1x2 dan mengatur ukuran total gambar menjadi 12x12 inci.
ax = axes.ravel()#meratakan array dari subplots menjadi satu dimensi menggunakan fungsi ravel() dari NumPy

ax[0].imshow(citra1, cmap = 'gray')# Menampilkan citra asli (citra1) dalam axes pertama (ax[0]) menggunakan imshow() dari matplotlib. 
ax[0].set_title("Citra Input")#Mengatur judul untuk axes pertama (ax[0]) menjadi "Citra Input" menggunakan set_title() dari matplotlib.
ax[1].imshow(citraOutput, cmap = 'gray')#Menampilkan citra hasil filter (citraOutput) dalam axes kedua (ax[1]) menggunakan imshow() dari matplotlib. Argumen citraOutput digunakan sebagai data citra yang akan ditampilkan, 
ax[1].set_title("Citra Output")#Mengatur judul untuk axes kedua (ax[1]) menjadi "Citra Output" menggunakan set_title() dari matplotlib.

plt.show()#Menampilkan figure yang berisi subplot citra asli dan citra hasil filter.