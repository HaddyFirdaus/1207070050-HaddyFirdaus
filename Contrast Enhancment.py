
import numpy as np#mengimpor library NumPy,
import matplotlib.pyplot as plt#mengimpor library Matplotlib
#%matplotlib inline
import cv2#mengimpor library OpenCV 
import matplotlib.image as mpimg#mengimpor modul image dari library Matplotlib
from skimage import data#mengimpor modul data dari library scikit-image (skimage)
#Read Image

image = cv2.imread("Saitama.jpg",cv2.IMREAD_GRAYSCALE)#membaca gambar dengan nama file "Saitama.jpg" menggunakan fungsi cv2.imread,dan membaca gambar dalam skala abu-abu (grayscale).
#Penerapan Histogram Equalization (HE)
image_equalized = cv2.equalizeHist(image)#enerapkan Histogram Equalization (HE) pada gambar yang telah dibaca sebelumnya menggunakan fungsi cv2.equalizeHist
#Penerapan Metode Contrast Limited Adaptive Histogram Equalization (CLAHE)
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))#membuat objek CLAHE (Contrast Limited Adaptive Histogram Equalization) menggunakan fungsi cv2.createCLAHE
#Apply CLAHE to the original image
image_clahe = clahe.apply(image)#menerapkan metode CLAHE pada gambar asli dengan menggunakan objek CLAHE yang telah dibuat sebelumnya. 
#Penerapan metode Contrast Stretching (CS)
image_cs = np.zeros((image.shape[0],image.shape[1]),dtype = 'uint8')#membuat array kosong dengan ukuran yang sama dengan gambar asli menggunakan fungsi np.zeros dari NumPy. 

# Apply Min-Max Contrasting
min = np.min(image)# menghitung nilai minimum dari array image menggunakan fungsi np.min
max = np.max(image)#menghitung nilai maksimum dari array image menggunakan fungsi np.max

for i in range(image.shape[0]):# memulai loop for yang akan berjalan sebanyak jumlah baris dalam gambar image.
    for j in range(image.shape[1]):#memulai loop for di dalam loop for sebelumnya yang akan berjalan sebanyak jumlah kolom dalam gambar image.
        image_cs[i,j] = 255*(image[i,j]-min)/(max-min)#menghitung nilai pixel baru untuk metode Contrast Stretching dan menyimpannya di dalam array image_cs
#Penerapan Metode Perkalian Konstanta
copyCamera = image.copy().astype(float)#membuat salinan dari gambar image dan mengubah tipe datanya menjadi float.

m1,n1 = copyCamera.shape#mengambil dimensi gambar copyCamera dan menetapkan nilai masing-masing dimensi ke variabel m1 dan n1.
output1 = np.empty([m1, n1])#membuat array kosong dengan ukuran [m1, n1] menggunakan fungsi np.empty 

for baris in range(0, m1-1):#memulai loop for yang akan berjalan sebanyak jumlah baris dalam gambar copyCamera.
    for kolom in range(0, n1-1):#memulai loop for di dalam loop for sebelumnya yang akan berjalan sebanyak jumlah kolom dalam gambar copyCamera
        a1 = baris#menyalin nilai dari variabel baris ke variabel a1
        b1 = kolom#menyalin nilai dari variabel kolom ke variabel b1.
        output1[a1, b1] = copyCamera[baris, kolom] * 1.9#mengalikan nilai pixel dalam gambar copyCamera dengan konstanta 1.9 dan menyimpan hasilnya di dalam array output1
#Plot Image
fig, axes = plt.subplots(5, 2, figsize=(20, 20))#membuat subplot untuk menampilkan beberapa gambar secara bersamaan
ax = axes.ravel()#meratakan array axes menjadi array 1 dimensi menggunakan fungsi ravel()

ax[0].imshow(image, cmap=plt.cm.gray)#menampilkan gambar asli menggunakan fungsi imshow dari Matplotlib dan tampilkan di subplot pertama (ax[0]) dengan menggunakan skema warna abu-abu
ax[0].set_title("Citra Input")#menetapkan judul "Citra Input" untuk subplot pertama ax[0]
ax[1].hist(image.ravel(), bins=256)#menghitung histogram gambar asli menggunakan fungsi hist dari Matplotlib. 
ax[1].set_title('Histogram Input')#menetapkan judul "Histogram Input" untuk subplot kedua (ax[1]).

ax[2].imshow(image_equalized, cmap=plt.cm.gray)#menampilkan gambar hasil pengolahan dengan metode Histogram Equalization (HE) menggunakan fungsi imshow dari Matplotlib.
ax[2].set_title("Citra Output HE")#enetapkan judul "Citra Output HE" untuk subplot ketiga (ax[2]).
ax[3].hist(image_equalized.ravel(), bins=256)#menghitung histogram gambar hasil pengolahan dengan metode HE menggunakan fungsi hist dari Matplotlib.
ax[3].set_title('Histogram Output HE Method')#menetapkan judul "Histogram Output HE Method" untuk subplot keempat (ax[3])

ax[4].imshow(image_cs, cmap=plt.cm.gray)#menampilkan gambar hasil pengolahan dengan metode Contrast Stretching (CS) menggunakan fungsi imshow dari Matplotlib
ax[4].set_title("Citra Output CS")#enetapkan judul "Citra Output CS" untuk subplot kelima (ax[4]).
ax[5].hist(image_cs.ravel(), bins=256)#menghitung histogram gambar hasil pengolahan dengan metode CS menggunakan fungsi hist dari Matplotlib. 
ax[5].set_title('Histogram Output CS Method')#menetapkan judul "Histogram Output CS Method" untuk subplot keenam (ax[5]).

ax[6].imshow(image_clahe, cmap=plt.cm.gray)#menampilkan gambar hasil pengolahan dengan metode Contrast Limited Adaptive Histogram Equalization (CLAHE) menggunakan fungsi imshow
ax[6].set_title("Citra Grayscale CLAHE")#menetapkan judul "Citra Grayscale CLAHE" untuk subplot ketujuh (ax[6]).
ax[7].hist(image_clahe.ravel(), bins=256)#menghitung histogram gambar hasil pengolahan dengan metode CLAHE menggunakan fungsi hist dari Matplotlib. 
ax[7].set_title('Histogram Output CLAHE Method')#menetapkan judul "Histogram Output CLAHE Method" untuk subplot kedelapan (ax[7]).

ax[8].imshow(output1, cmap=plt.cm.gray)#menampilkan gambar hasil pengolahan dengan metode Perkalian Konstanta menggunakan fungsi imshow dari Matplotlib.
ax[8].set_title("Citra Grayscale Perkalian Konstanta")#menetapkan judul "Citra Grayscale Perkalian Konstanta" untuk subplot kesembilan (ax[8]).
ax[9].hist(output1.ravel(), bins=256)#menghitung histogram gambar hasil pengolahan dengan metode Perkalian Konstanta menggunakan fungsi hist dari Matplotlib
ax[9].set_title('Histogram Output Perkalian Konstanta Method')#menetapkan judul "Histogram Output Perkalian Konstanta Method" untuk subplot kesepuluh (ax[9]).

fig.tight_layout()#menyesuaikan tata letak subplot secara otomatis untuk menghindari tumpang tindih antara subplot
plt.show()#menampilkan semua subplot yang telah ditentukan sebelumnya.