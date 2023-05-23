# memanggil modul yang diperlukan
import cv2#mengimport cv2
import numpy as np#mengimpor library NumPy,
import matplotlib.pyplot as plt#mengimpor library Matplotlib

# Low-Pass Filtering

# baca gambar dengan tipe data yang sesuai
img = cv2.imread('satoru.jpg', cv2.IMREAD_COLOR)# Membaca gambar 'satoru.jpg' dengan menggunakan fungsi cv2.imread() dan menetapkan hasilnya ke variabel img.

# konversi ke format RGB
satoru = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#Mengkonversi gambar dari format BGR (Blue-Green-Red) ke format RGB (Red-Green-Blue) menggunakan fungsi cv2.cvtColor(). 

# tampilkan gambar awal tanpa filter
plt.imshow(satoru)#: Menampilkan gambar awal (sebelum filtering) menggunakan plt.imshow().
plt.axis('off')#Menghilangkan sumbu pada plot gambar menggunakan plt.axis('off').
plt.show()# Menampilkan plot gambar.

# membuat filter: matriks berukuran 5 x 5 
kernel = np.ones((5, 5), np.float32) / 25#embuat filter berukuran 5x5 dengan nilai 1 di setiap elemennya. Kemudian, nilai setiap elemen dibagi dengan 25 agar jumlah total elemen pada filter menjadi 1. 
print(kernel)#Menampilkan nilai kernel/filter yang telah dibuat.

# lakukan filtering
satoru_filter = cv2.filter2D(satoru, -1, kernel)#Melakukan operasi filtering pada gambar satoru menggunakan filter kernel

# tampilkan gambar setelah filtering
plt.imshow(satoru_filter)#Menampilkan gambar setelah proses filtering menggunakan plt.imshow().
plt.axis('off')#Menghilangkan sumbu pada plot gambar menggunakan plt.axis('off').
plt.show()# Menampilkan plot gambar.

# salt and pepper

# perbesar ukuran hasil plotting jika diperlukan
plt.rcParams["figure.figsize"] = (15, 15)#Mengatur ukuran gambar plot menjadi 15x15 menggunakan plt.rcParams["figure.figsize"].

# plot pertama, gambar asli
plt.subplot(121), plt.imshow(satoru), plt.title('Original')#
plt.xticks([]), plt.yticks([])#Menghilangkan tanda sumbu pada subplot pertama menggunakan plt.xticks([]) dan plt.yticks([]).

# kedua, hasil filter
plt.subplot(122), plt.imshow(satoru_filter)#Membuat subplot pertama dengan nomor 121 menggunakan plt.subplot().
plt.title('Averaging')#memberikan judul 'Original' menggunakan plt.title().
plt.xticks([]), plt.yticks([])#Menghilangkan tanda sumbu pada subplot pertama menggunakan plt.xticks([]) dan plt.yticks([]).

# Plot!
plt.show()# Menampilkan plot gambar.

satoru_blur = cv2.blur(satoru, (5, 5))#Menampilkan gambar hasil penajaman citra (satoru_blur) menggunakan plt.imshow().

plt.imshow(satoru_blur)# Menampilkan gambar hasil blur
plt.axis('off')#Menghilangkan sumbu pada plot gambar menggunakan plt.axis('off').
plt.show()# Menampilkan plot gambar.


# ini adalah cara lain untuk membuat sebuah kernel,
# yaitu dengan menggunakan np.matrix
# kali ini, ukuran matriksnya 3 x 3
kernel = np.matrix([#Membuat kernel dengan menggunakan np.matrix yang merupakan matriks 3x3 dengan nilai elemen [1, 1, 1] di baris pertama, [1, 2, 1] di baris kedua, dan [1, 1, 1] di baris ketiga. Kernel tersebut kemudian dibagi dengan 25 untuk melakukan normalisasi.
          [1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]
          ]) / 25
print(kernel)# Mencetak kernel ke konsol untuk melihat nilainya.

# buat lagi filteringnya
satoru_filter = cv2.filter2D(satoru, -1, kernel)#Melakukan filtering pada gambar satoru menggunakan cv2.filter2D() dengan kernel yang telah dibuat sebelumnya. 

# tampilkan
plt.imshow(satoru_filter)# Menampilkan gambar hasil filtering 
plt.axis('off')#Menghilangkan sumbu pada plot gambar menggunakan plt.axis('off').
plt.show()# Menampilkan plot gambar.

# Highpass Filter

# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('Tsubasa.jpg', 0)# Membaca citra dengan nama file 'Tsubasa.jpg' sebagai citra grayscale. 

# menerapkan algoritma high-pass filtering:
# laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)# Menggunakan algoritma high-pass filtering Laplacian pada citra img menggunakan fungsi cv2.Laplacian(). Hasil filtering disimpan dalam variabel laplacian.

# sobel dengan ukuran kernel 5
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)# Menggunakan algoritma high-pass filtering Sobel pada citra img untuk mendeteksi tepi secara horizontal (sumbu x) menggunakan fungsi cv2.Sobel()
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)# Menggunakan algoritma high-pass filtering Sobel pada citra img untuk mendeteksi tepi secara vertikal (sumbu y) menggunakan fungsi cv2.Sobel(). 

# Catatan:
# CV_64F pada contoh di atas menunjukkan nilai bit dari citra 
# yang dihasilkan serta tipe datanya (F = Float)

# perbesar ukuran hasil plotting 
plt.rcParams["figure.figsize"] = (20, 20)#Mengatur ukuran gambar hasil plotting menjadi 20x20 inci.

# menampilkan hasil filter
plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')#Membuat subplot dengan grid 2x2 dan memilih subplot pertama. Kemudian, menampilkan citra img dengan menggunakan colormap 'gray' menggunakan plt.imshow().
plt.title('Original'), plt.xticks([]), plt.yticks([])#Memberikan judul pada subplot pertama sebagai 'Original' dan menghilangkan penanda sumbu x dan y.
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')#Memilih subplot kedua dan menampilkan citra hasil filtering Laplacian (laplacian) dengan menggunakan colormap 'gray' menggunakan plt.imshow().
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])#Memberikan judul pada subplot kedua sebagai 'Laplacian' dan menghilangkan penanda sumbu x dan y.
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')#Memilih subplot ketiga dan menampilkan citra hasil filtering Sobel horizontal (sobelx) dengan menggunakan colormap 'gray' menggunakan plt.imshow().
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])#Memberikan judul pada subplot ketiga sebagai 'Sobel X' dan menghilangkan penanda sumbu x dan y.
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')#emilih subplot keempat dan menampilkan citra hasil filtering Sobel vertikal (sobely) dengan menggunakan colormap 'gray' menggunakan plt.imshow().
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])#: Memberikan judul pada subplot keempat sebagai 'Sobel Y' dan menghilangkan penanda sumbu x dan y.
plt.show()#Menampilkan plot gambar hasil filtering dengan menggunakan plt.show().

# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('baymax.jpg', 0)# Membaca citra dengan nama file 'baymax.jpg' sebagai citra grayscale. Argument 0

# memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)#
edges = cv2.Canny(img, 100, 200)#Menggunakan algoritma Canny Edges untuk mendeteksi tepi pada citra img dengan nilai ambang bawah 100 dan nilai ambang atas 200. Hasil deteksi tepi disimpan dalam variabel edges.

plt.subplot(121), plt.imshow(img, cmap='gray')#Membuat subplot dengan grid 1x2 dan memilih subplot pertama. Kemudian, menampilkan citra img dengan menggunakan colormap 'gray' menggunakan plt.imshow()..
plt.title('Original Image'), plt.xticks([]), plt.yticks([])# Memberikan judul pada subplot pertama sebagai 'Original Image' dan menghilangkan penanda sumbu x dan y.
plt.subplot(122), plt.imshow(edges, cmap='gray')#Memilih subplot kedua dan menampilkan citra hasil deteksi tepi (edges) dengan menggunakan colormap 'gray' menggunakan plt.imshow().
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])#: Memberikan judul pada subplot kedua sebagai 'Edge Image' dan menghilangkan penanda sumbu x dan y.

plt.show()#: Menampilkan plot gambar dengan menggunakan plt.show().

# membaca gambar baymax 
img = cv2.imread('baymax.jpg',0)#Membaca citra dengan nama file 'baymax.jpg' sebagai citra grayscale.

# Hitungan threshold. 
# Perhatikan nilai ambang batas bawah dan atas dari tiap fungsi 
# yang diberikan
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)# Menggunakan thresholding dengan nilai ambang 127 pada citra img menggunakan fungsi cv2.threshold(). Hasil thresholding dengan metode BINARY disimpan dalam variabel thresh1
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)#Menggunakan thresholding dengan nilai ambang 127 pada citra img menggunakan fungsi cv2.threshold(). 
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)#Menggunakan thresholding dengan nilai ambang 127 pada citra img menggunakan fungsi cv2.threshold(). 
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)#Menggunakan thresholding dengan nilai ambang 127 pada citra img menggunakan fungsi cv2.threshold(). 
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)#Menggunakan thresholding dengan nilai ambang 127 pada citra img menggunakan fungsi cv2.threshold().

# menampilkan hasil
titles = ['Gambar asli','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']#Membuat daftar judul untuk masing-masing citra.
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]#Membuat daftar citra yang akan ditampilkan.

# menampilkan beberapa gambar sekaligus
for i in range(6):#: Melakukan iterasi untuk setiap indeks dalam rentang 0 hingga 5
    # 3 baris, 2 kolom
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')#Membuat subplot dengan grid 3x2 dan memilih subplot sesuai dengan indeks i+1. Kemudian, menampilkan citra dari daftar images 
    plt.title(titles[i])#Memberikan judul pada subplot sesuai dengan indeks i menggunakan judul yang sesuai dari daftar titles.
    plt.xticks([]),plt.yticks([])#Menghilangkan penanda sumbu x dan y pada subplot.
plt.show()#Menampilkan plot gambar dengan menggunakan plt.show().

# digunakan median blur untuk menghaluskan tepi objek pada citra
# ini diperlukan agar thresholding memberikan hasil lebih baik
img = cv2.medianBlur(img,5)#Melakukan proses median blur pada citra img dengan ukuran kernel 5x5. Fungsi cv2.medianBlur() digunakan untuk mengurangi noise pada citra.

# Lakukan Thresholding
# Binary Threshold
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#elakukan thresholding dengan nilai ambang 127 pada citra img menggunakan metode binary thresholding. Hasil thresholding disimpan dalam variabel th1

# Adaptive Threshold dengan Mean
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)#Melakukan thresholding adaptif menggunakan metode mean thresholding pada citra img. Hasil thresholding disimpan dalam variabel th2. Metode ini menggunakan blok 11x11 di sekitar setiap piksel sebagai acuan untuk menghitung ambang batasnya. 

# Adaptive Threshold dengan Gaussian
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)#Melakukan thresholding adaptif menggunakan metode Gaussian thresholding pada citra img. Hasil thresholding disimpan dalam variabel th3. Metode ini juga menggunakan blok 11x11 di sekitar setiap piksel sebagai acuan untuk menghitung ambang batasnya


# Plotting
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']# Membuat daftar judul untuk masing-masing citra yang akan ditampilkan.
images = [img, th1, th2, th3]#Membuat daftar citra yang akan ditampilkan.

# menampilkan hasil
for i in range(4):#Melakukan iterasi untuk setiap indeks dalam rentang 0 hingga 3.
    plt.subplot(2,2,i+1)#: Membuat subplot dengan grid 2x2 dan memilih subplot sesuai dengan indeks i+1.
    plt.imshow(images[i],'gray')#Menampilkan citra dari daftar images pada subplot yang dipilih dengan menggunakan colormap 'gray' menggunakan plt.imshow().
    plt.title(titles[i])# Memberikan judul pada subplot sesuai dengan indeks i menggunakan judul yang sesuai dari daftar titles.
    plt.xticks([]),plt.yticks([])#Menghilangkan penanda sumbu x dan y pada subplot.
plt.show()# Menampilkan plot gambar dengan menggunakan plt.show().