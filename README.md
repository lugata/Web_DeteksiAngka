# Web_DeteksiAngka

Install :

pip install Flask opencv-python tensorflow keras

Anda dapat menggunakan kode ini untuk mendeteksi angka dari gambar yang diambil dengan kamera real-time atau yang Anda pilih dari direktori.

Pertama, kita melatih model yang telah dilatih sebelumnya sebelum menggunakan TensorFlow Keras. Lalu ada rute di Flask yang mengambil gambar dari POST dan mengubahnya menjadi tensor, lalu menggunakan model tersebut untuk memprediksi angka yang terdeteksi di gambar.
