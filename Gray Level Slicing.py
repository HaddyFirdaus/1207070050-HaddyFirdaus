import cv2#mengimpor library OpenCV 
import numpy as np#mengimpor library NumPy,
import matplotlib.pyplot as plt#mengimpor library Matplotlib

img = cv2.imread("Saitama.jpg",cv2.IMREAD_GRAYSCALE)#membaca gambar "Saitama.jpg" dalam mode grayscale menggunakan fungsi imread dari OpenCV.dan membaca gambar dalam skala abu-abu (grayscale).

row, column = img.shape#mengambil dimensi gambar img dan menetapkan nilai masing-masing dimensi ke variabel row dan column

img1 = np.zeros((row, column), dtype='uint8')# membuat array kosong dengan ukuran yang sama seperti gambar img menggunakan fungsi np.zeros dari NumPy. 

min_range = 10#menentukan rentang intensitas piksel yang akan dipertahankan dalam hasil pengolahan.
max_range = 60#menentukan rentang intensitas piksel yang akan dipertahankan dalam hasil pengolahan.

for i in range(row):#loop yang mengiterasi melalui setiap baris dalam gambar. Variabel i akan berubah nilainya dari 0 hingga row-1, 
    for j in range(column):# loop yang mengiterasi melalui setiap kolom dalam gambar. Variabel j akan berubah nilainya dari 0 hingga column-1
        intensity = img[i, j]# mengambil nilai intensitas piksel pada posisi (i, j) dari gambar img dan menyimpannya dalam variabel intensity.
        if intensity > min_range and intensity < max_range:#memeriksa apakah nilai intensitas piksel berada di antara min_range dan max_range.
            img1[i, j] = 255#nilai intensitas piksel memenuhi kondisi di atas, maka piksel pada posisi (i, j) pada gambar img1 akan diatur menjadi 255 (putih).
        else:
            img1[i, j] = 0#Jika nilai intensitas piksel tidak memenuhi kondisi di atas, maka piksel pada posisi (i, j) pada gambar img1 akan diatur menjadi 0 (hitam).

fig, axes = plt.subplots(2, 2, figsize=(12, 12))#untuk membuat grid subplot dengan ukuran 2x2 dan mengatur ukuran total gambar menjadi 12x12 inci.
ax = axes.ravel()#meratakan array dari subplots menjadi satu dimensi menggunakan fungsi ravel() dari NumPy

ax[0].imshow(img, cmap=plt.cm.gray)# menampilkan gambar asli (img) dalam subplot pertama (ax[0]) menggunakan fungsi imshow dari Matplotlib
ax[0].set_title("Citra Input")#menetapkan judul "Citra Input" untuk subplot pertama (ax[0]).
ax[1].hist(img.ravel(), bins=256)#menghitung dan menampilkan histogram gambar asli (img) dalam subplot kedua (ax[1]) menggunakan fungsi hist dari Matplotlib. 
ax[1].set_title('Histogram Input')# menetapkan judul "Histogram Input" untuk subplot kedua (ax[1]).

ax[2].imshow(img1, cmap=plt.cm.gray)#menampilkan gambar hasil pengolahan (img1) dalam subplot ketiga (ax[2]) menggunakan fungsi imshow dari Matplotlib
ax[2].set_title("Citra Output")# menetapkan judul "Citra Output" untuk subplot ketiga (ax[2]).
ax[3].hist(img1.ravel(), bins=256)#menghitung dan menampilkan histogram gambar hasil pengolahan (img1) dalam subplot keempat (ax[3]) menggunakan fungsi hist dari Matplotlib.
ax[3].set_title('Histogram Output')# menetapkan judul "Histogram Output" untuk subplot keempat (ax[3]).
plt.show()#menampilkan semua subplot yang telah ditentukan sebelumnya.
