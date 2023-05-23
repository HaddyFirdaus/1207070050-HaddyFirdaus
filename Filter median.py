import matplotlib.pyplot as plt#mengimpor library Matplotlib
#%matplotlib inline

from skimage import data#mengimpor modul data dari library scikit-image (skimage)
from skimage.io import imread#mengimpor fungsi imread dari modul skimage.io dalam paket scikit-image
from skimage.color import rgb2gray #engimpor fungsi rgb2gray dari modul skimage.color dalam paket scikit-image. 
import numpy as np#mengimpor library NumPy,

citra1 = imread(fname="mobil.tif")#menggunakan fungsi imread untuk membaca gambar dengan nama file "mobil.tif" dan menyimpannya ke dalam variabel citra1.
citra2 = imread(fname="boneka2.tif")#menggunakan fungsi imread untuk membaca gambar dengan nama file "boneka2.jpg" dan menyimpannya ke dalam variabel citra2.

print('Shape citra 1 : ', citra1.shape)#mencetak dimensi citra 1 (jumlah baris, jumlah kolom, dan jumlah saluran warna jika citra berwarna) dengan menggunakan atribut shape dari matriks citra1.
print('Shape citra 2 : ', citra2.shape)#mencetak dimensi citra 2 (jumlah baris, jumlah kolom, dan jumlah saluran warna jika citra berwarna) dengan menggunakan atribut shape dari matriks citra2.

fig, axes = plt.subplots(1, 2, figsize=(10, 10))# membuat objek figure dan array dari subplots dengan ukuran 1x2 (2 subplots dalam total). 
ax = axes.ravel()#meratakan array dari subplots menjadi satu dimensi menggunakan fungsi ravel() dari NumPy. 

ax[0].imshow(citra1, cmap = 'gray')#menampilkan citra 1 (citra1) dalam subplot pertama (ax[0]) menggunakan fungsi imshow dari Matplotlib. 
ax[0].set_title("Citra 1")#menetapkan judul "Citra 1" untuk subplot pertama (ax[0]).
ax[1].imshow(citra2, cmap = 'gray')#menampilkan citra 2 (citra2) dalam subplot kedua (ax[1]).
ax[1].set_title("Citra 2")#menetapkan judul "Citra 2" untuk subplot kedua (ax[1]).

copyCitra1 = citra1.copy()# untuk melakukan operasi pada citra tanpa mempengaruhi citra asli. Dengan menyimpan salinan, Anda dapat memodifikasi atau menerapkan transformasi pada citra tersebut tanpa mengubah citra asli yang disimpan dalam variabel citra1
copyCitra2 = citra2.copy()#untuk melakukan operasi pada citra tanpa mempengaruhi citra asli. Dengan menyimpan salinan, Anda dapat memodifikasi atau menerapkan transformasi pada citra tersebut tanpa mengubah citra asli yang disimpan dalam variabel citra2.

m1,n1 = copyCitra1.shape[:2]#endapatkan dimensi citra 1 (copyCitra1) dengan menggunakan atribut shape dari matriks dan mengambil elemen pertama dan kedua (jumlah baris dan kolom)
output1 = np.empty([m1, n1])#membuat matriks kosong dengan ukuran [m1, n1] menggunakan fungsi empty() dari NumPy

m2, n2 = copyCitra2.shape[:2]#melakukan hal yang sama seperti baris sebelumnya, tetapi untuk citra 2 (copyCitra2). Dimensi citra 2 disimpan dalam variabel m2 dan n2.
output2 = np.empty([m2, n2])#membuat matriks kosong dengan ukuran [m2, n2] menggunakan fungsi empty() dari NumPy
print('Shape copy citra 1 : ', copyCitra1.shape)#mencetak dimensi citra 1 yang telah diubah tipe datanya (copyCitra1) dengan menggunakan atribut shape dari matriks.
print('Shape output citra 1 : ', output1.shape)#mencetak dimensi matriks kosong yang akan digunakan untuk hasil pengolahan citra 1 (output1).

print('m1 : ',m1)# mencetak nilai m1, yaitu jumlah baris citra 1.
print('n1 : ',n1)# mencetak nilai n1, yaitu jumlah kolom citra 1.
print()#memberikan baris kosong dalam output konsol agar lebih terorganisir.

print('Shape copy citra 2 : ', copyCitra2.shape)#mencetak dimensi citra 2 yang telah diubah tipe datanya (copyCitra2).
print('Shape output citra 3 : ', output2.shape)# mencetak dimensi matriks kosong yang akan digunakan untuk hasil pengolahan citra 2 (output2).
print('m2 : ',m2)#mencetak nilai m2, yaitu jumlah baris citra 2.
print('n2 : ',n2)#mencetak nilai n2, yaitu jumlah kolom citra 2.
print()#memberikan baris kosong dalam output konsol agar lebih terorganisir.

for baris in range(1, m1-1):#memulai loop untuk iterasi melalui baris dari 0 hingga m1-1 (jumlah baris citra 1 dikurangi 1).
    for kolom in range(1, n1-1):##memulai loop untuk iterasi melalui kolom dari 1 hingga n1-1 (jumlah kolom citra 1 dikurangi 1).
        a1 = baris#menginisialisasi variabel a1 dengan nilai baris, yang merupakan indeks baris saat ini dalam iterasi.
        b1 = kolom#menginisialisasi variabel b1 dengan nilai kolom, yang merupakan indeks kolom saat ini dalam iterasi.
        dataA = np.array([copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1-1, b1+1],
              copyCitra1[a1, b1-1], copyCitra1[a1, b1], copyCitra1[a1, b1+1],
              copyCitra1[a1+1, b1-1], copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]])## menghitung jumlah dari elemen tetangga pada citra 1 untuk setiap piksel pada baris dan kolom saat ini. Pengambilan nilai tetangga dilakukan dengan menggunakan indeks yang diubah sesuai dengan aturan perhitungan. 
        
        # Urutkan
        for i in range(1, 8):#loop pertama yang akan berjalan dari 1 hingga 7. Variabel i akan memiliki nilai 1, 2, 3, 4, 5, 6, dan 7.
            for j in range(i, 9):# loop kedua yang akan berjalan dari i hingga 8. Variabel j akan memiliki nilai yang berbeda pada setiap iterasi tergantung pada nilai i. Pada iterasi pertama, j akan memiliki nilai 1, 2, 3, 4, 5, 6, 7, dan 8.
                if np.greater(dataA[i], dataA[j]).any():#kondisi yang membandingkan elemen-elemen dataA pada indeks i dan j. np.greater adalah fungsi numpy yang membandingkan elemen-elemen dua array dan mengembalikan array boolean yang menunjukkan apakah elemen-elemen pertama lebih besar daripada elemen-elemen kedua. 
                    tmpA = dataA[i];#Variabel sementara tmpA digunakan untuk menyimpan nilai dataA pada indeks i.
                    dataA[i] = dataA[j];#Nilai dataA pada indeks i diganti dengan nilai dataA pada indeks j.
                    dataA[j]= tmpA;#Nilai dataA pada indeks j diganti dengan nilai yang disimpan di variabel sementara tmpA.
        
        median_value = int(np.median(dataA))# Nilai median dari array dataA dihitung menggunakan fungsi np.median dari NumPy, dan nilai median tersebut disimpan dalam variabel median_value
        output1[a1, b1] = median_value# Nilai median (median_value) disimpan dalam matriks output1 pada indeks baris a1 dan kolom b1.

for baris in range(1, m2-1):#memulai loop untuk iterasi melalui baris dari 0 hingga m2-1 (jumlah baris citra 2 dikurangi 1).
    for kolom in range(1, n2-1):# memulai loop untuk iterasi melalui kolom dari 0 hingga n2-1 (jumlah kolom citra 2 dikurangi 1).
        a2 = baris# menginisialisasi variabel a1 dengan nilai baris1, yang merupakan indeks baris saat ini dalam iterasi.
        b2 = kolom#menginisialisasi variabel b1 dengan nilai kolom1, yang merupakan indeks kolom saat ini dalam iterasi.
        dataA = np.array([copyCitra2[a2-1, b2-1], copyCitra2[a2-1, b2], copyCitra2[a2-1, b2+1],
                         copyCitra2[a2, b2-1], copyCitra2[a2, b2], copyCitra2[a2, b2+1],
                         copyCitra2[a2+1, b2-1], copyCitra2[a2+1, b2], copyCitra2[a2+1, b2+1]])##menghitung jumlah dari elemen tetangga pada citra 2 untuk setiap piksel pada baris dan kolom saat ini. Pengambilan nilai tetangga dilakukan dengan menggunakan indeks yang diubah sesuai dengan aturan perhitungan.
        
        # Urutkan
        for i in range(1, 8):#loop pertama yang akan berjalan dari 1 hingga 7. Variabel i akan memiliki nilai 1, 2, 3, 4, 5, 6, dan 7.
            for j in range(i, 9):# loop kedua yang akan berjalan dari i hingga 8. Variabel j akan memiliki nilai yang berbeda pada setiap iterasi tergantung pada nilai i. Pada iterasi pertama, j akan memiliki nilai 1, 2, 3, 4, 5, 6, 7, dan 8.
                if np.greater(dataA[i], dataA[j]).any():#kondisi yang membandingkan elemen-elemen dataA pada indeks i dan j. np.greater adalah fungsi numpy yang membandingkan elemen-elemen dua array dan mengembalikan array boolean yang menunjukkan apakah elemen-elemen pertama lebih besar daripada elemen-elemen kedua. 
                    tmpA = dataA[i];#Variabel sementara tmpA digunakan untuk menyimpan nilai dataA pada indeks i.
                    dataA[i] = dataA[j];#Nilai dataA pada indeks i diganti dengan nilai dataA pada indeks j.
                    dataA[j]= tmpA;#Nilai dataA pada indeks j diganti dengan nilai yang disimpan di variabel sementara tmpA.
        
        median_value = int(np.median(dataA))# Nilai median dari array dataA dihitung menggunakan fungsi np.median dari NumPy, dan nilai median tersebut disimpan dalam variabel median_value
        output2[a2, b2] = median_value# Nilai median (median_value) disimpan dalam matriks output1 pada indeks baris a1 dan kolom b1.


fig, axes = plt.subplots(2, 2, figsize=(10, 10))#untuk membuat grid subplot dengan ukuran 2x2 dan mengatur ukuran total gambar menjadi 10x10 inci.
ax = axes.ravel()#meratakan array dari subplots menjadi satu dimensi menggunakan fungsi ravel() dari NumPy

ax[0].imshow(citra1, cmap = 'gray')#ntuk menampilkan citra input pertama (citra1) dalam ax[0] menggunakan colormap 'gray'.
ax[0].set_title("Input Citra 1")#mengatur judul subplot pertama menjadi "Input Citra 1".

ax[1].imshow(citra2, cmap = 'gray')# untuk menampilkan citra input kedua (citra2) dalam ax[1] menggunakan colormap 'gray'.
ax[1].set_title("Input Citra 1")#mengatur judul subplot kedua menjadi "Input Citra 2".

ax[2].imshow(output1, cmap = 'gray')#untuk menampilkan citra output pertama (output1) dalam ax[2] menggunakan colormap 'gray'.
ax[2].set_title("Output Citra 1")# mengatur judul subplot ketiga menjadi "Output Citra 1".

ax[3].imshow(output2, cmap = 'gray')#untuk menampilkan citra output kedua (output2) dalam ax[3] menggunakan colormap 'gray'.
ax[3].set_title("Output Citra 2")# mengatur judul subplot keempat menjadi "Output Citra 2".

plt.show()# menampilkan gambar dengan keempat subplot yang telah dikonfigurasi.