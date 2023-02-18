from flask import Flask, render_template, request, jsonify
import os
import cv2
import tensorflow as tf
import tensorflow.keras as keras

app = Flask(__name__)

# Muat model pengenalan angka yang telah dilatih sebelumnya
model = keras.models.load_model("static/model/model.h5")

@app.route("/predict", methods=["POST"])
def predict():
    # Ambil citra dari request
    data = request.get_json()
    image = data["image"]

    # Ubah citra ke dalam bentuk tensor
    image = tf.convert_to_tensor(image, dtype=tf.float32)
    image = tf.reshape(image, [1, 28, 28, 1])

    # Gunakan model untuk mengprediksi angka yang terdeteksi di citra
    prediction = model.predict(image)
    angka = int(tf.argmax(prediction, axis=1))

    # Kirim hasil pengenalan angka kembali ke client
    return jsonify({"angka": angka})


# Buat route di Flask untuk menampilkan halaman web
@app.route("/")
def index():
    # Muat kamera real-time
    cap = cv2.VideoCapture(0)

    # Tangkap frame dari kamera dan olah citra menggunakan OpenCV
    image = tangkap_frame(cap)

    # Gunakan model untuk mengprediksi angka yang terdeteksi di citra
    prediction = model.predict(image)
    angka = int(tf.argmax(prediction, axis=1))

    # Tampilkan hasil pengenalan angka di halaman web
    return render_template("index.html", angka=angka)

def tangkap_frame(cap):
    # Ambil frame dari kamera
    ret, frame = cap.read()

    # Olah citra menggunakan OpenCV
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (28, 28))

    # Ubah citra ke dalam bentuk tensor
    image = tf.expand_dims(gray, 0)
    image = tf.expand_dims(image, -1)

    return image


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=2000)