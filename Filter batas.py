import matplotlib.pyplot as plt#mengimpor library Matplotlib
#%matplotlib inline

from skimage import data#mengimpor modul data dari library scikit-image (skimage)
from skimage.io import imread#mengimpor fungsi imread dari modul skimage.io dalam paket scikit-image
from skimage.color import rgb2gray #engimpor fungsi rgb2gray dari modul skimage.color dalam paket scikit-image. 
import numpy as np#mengimpor library NumPy,


citra1 = imread(fname="mobil.tif")#menggunakan fungsi imread untuk membaca gambar dengan nama file "Tsubasa.jpg" dan menyimpannya ke dalam variabel citra1.
citra2 = imread(fname="boneka2.tif")#menggunakan fungsi imread untuk membaca gambar dengan nama file "Saitama.jpg" dan menyimpannya ke dalam variabel citra2.

print('Shape citra 1 : ', citra1.shape)#mencetak dimensi citra 1 (jumlah baris, jumlah kolom, dan jumlah saluran warna jika citra berwarna) dengan menggunakan atribut shape dari matriks citra1.
print('Shape citra 2 : ', citra2.shape)#mencetak dimensi citra 2 (jumlah baris, jumlah kolom, dan jumlah saluran warna jika citra berwarna) dengan menggunakan atribut shape dari matriks citra2.

fig, axes = plt.subplots(1, 2, figsize=(10, 10))# membuat objek figure dan array dari subplots dengan ukuran 1x2 (2 subplots dalam total). 
ax = axes.ravel()#meratakan array dari subplots menjadi satu dimensi menggunakan fungsi ravel() dari NumPy. 

ax[0].imshow(citra1, cmap = 'gray')#menampilkan citra 1 (citra1) dalam subplot pertama (ax[0]) menggunakan fungsi imshow dari Matplotlib. 
ax[0].set_title("Citra 1")#menetapkan judul "Citra 1" untuk subplot pertama (ax[0]).
ax[1].imshow(citra2, cmap = 'gray')#menampilkan citra 2 (citra2) dalam subplot kedua (ax[1]).
ax[1].set_title("Citra 2")#menetapkan judul "Citra 2" untuk subplot kedua (ax[1]).

copyCitra1 = citra1.copy().astype(float)#membuat salinan citra 1 (citra1) dengan menggunakan metode copy() dari objek matriks.
copyCitra2 = citra2.copy().astype(float)#melakukan hal yang sama seperti baris sebelumnya,untuk citra 2 (citra2). 

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
for baris in range(0, m1-1):#digunakan untuk mengiterasi melalui baris dalam matriks citra. Nilai m1 adalah jumlah baris dalam matriks citra. 
    for kolom in range(0, n1-1):#digunakan untuk mengiterasi melalui kolom dalam matriks citra. Nilai n1 adalah jumlah kolom dalam matriks citra.
        
        a1 = baris#digunakan untuk mengakses piksel tertentu dalam matriks citra.
        b1 = kolom#digunakan untuk mengakses piksel tertentu dalam matriks citra.
        
        arr = np.array([copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1, b1+1], \
            copyCitra1[a1, b1-1], copyCitra1[a1, b1+1], copyCitra1[a1+1, b1-1],  \
            copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]])# dibuat dengan mengambil nilai piksel dari tujuh posisi sekitar piksel saat ini dalam matriks citra. Nilai piksel diambil menggunakan indeks
        
        minPiksel = np.amin(arr);#Nilai minimum dalam array arr dihitung menggunakan fungsi np.amin() dan disimpan dalam variabel minPiksel.  
        maksPiksel = np.amax(arr);# Nilai maksimum dalam array arr dihitung menggunakan fungsi np.amax() dan disimpan dalam variabel maksPiksel.
            
        if (copyCitra1[baris, kolom] < minPiksel):#untuk membandingkan nilai piksel saat ini dalam matriks citra (copyCitra1[baris, kolom]) dengan nilai minimum (minPiksel). 
            output1[baris, kolom] = minPiksel#nilai piksel saat ini lebih kecil dari nilai minimum, maka nilai piksel di posisi saat ini dalam matriks output1 diatur menjadi nilai minimum (minPiksel).
        else :
            if copyCitra1[baris, kolom] > maksPiksel :#Pemeriksaan kondisional dilakukan untuk membandingkan nilai piksel saat ini dalam matriks citra (copyCitra1[baris, kolom]) dengan nilai maksimum (maksPiksel).
                output1[baris, kolom] = maksPiksel#Jika nilai piksel saat ini lebih besar dari nilai maksimum, maka nilai piksel di posisi saat ini dalam matriks output1 diatur menjadi nilai maksimum (maksPiksel).
            else :
                output1[baris, kolom] = copyCitra1[baris, kolom]#jika nilai piksel saat ini tidak lebih kecil dari nilai minimum dan tidak lebih besar dari nilai maksimum, maka nilai piksel di posisi saat ini dalam matriks output1
for baris1 in range(0, m2-1):#digunakan untuk mengiterasi melalui baris dalam matriks citra. Nilai m2 adalah jumlah baris dalam matriks citra. 
    for kolom1 in range(0, n2-1):#digunakan untuk mengiterasi melalui kolom dalam matriks citra. Nilain2 adalah jumlah kolom dalam matriks citra.
        
        a1 = baris1#digunakan untuk mengakses piksel tertentu dalam matriks citra.
        b1 = kolom1#digunakan untuk mengakses piksel tertentu dalam matriks citra.
        
        arr = np.array([copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1, b1+1], \
            copyCitra2[a1, b1-1], copyCitra2[a1, b1+1], copyCitra2[a1+1, b1-1],  \
            copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]])#dibuat dengan mengambil nilai piksel dari tujuh posisi sekitar piksel saat ini dalam matriks citra. Nilai piksel diambil menggunakan indeks
        
        minPiksel = np.amin(arr);#Nilai minimum dalam array arr dihitung menggunakan fungsi np.amin() dan disimpan dalam variabel minPiksel.     
        maksPiksel = np.amax(arr);# Nilai maksimum dalam array arr dihitung menggunakan fungsi np.amax() dan disimpan dalam variabel maksPiksel.  
            
        if copyCitra1[baris, kolom] < minPiksel:#untuk membandingkan nilai piksel saat ini dalam matriks citra (copyCitra1[baris, kolom]) dengan nilai minimum (minPiksel). 
            output2[baris1, kolom1] = minPiksel#nilai piksel saat ini lebih kecil dari nilai minimum, maka nilai piksel di posisi saat ini dalam matriks output1 diatur menjadi nilai minimum (minPiksel).
        else :
            if copyCitra2[baris1, kolom1] > maksPiksel :#Pemeriksaan kondisional dilakukan untuk membandingkan nilai piksel saat ini dalam matriks citra (copyCitra1[baris, kolom]) dengan nilai maksimum (maksPiksel).
                output2[baris1, kolom1] = maksPiksel#Jika nilai piksel saat ini lebih besar dari nilai maksimum, maka nilai piksel di posisi saat ini dalam matriks output1 diatur menjadi nilai maksimum (maksPiksel).
            else :
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]#jika nilai piksel saat ini tidak lebih kecil dari nilai minimum dan tidak lebih besar dari nilai maksimum, maka nilai piksel di posisi saat ini dalam matriks output2


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