# deteksi-ekspresi-wajah
Deteksi ekspresi wajah menggunakan _feature extraction landmark_ dan klasifikasi menggunakan _Support Vector Machines_ (SVM). Program diimplementasikan menggunakan bahasa pemograman Python 3. Untuk deteksi _landmark_ menggunakan pustaka dari [dlib](https://pypi.org/project/dlib/) dan SVM menggunakan pustaka dari [sklearn](http://scikit-learn.org/stable/modules/svm.html).
Untuk file Python ada 4:
* _pengelompokan.py_ : berisi pengelompokan dataset berdasarkan ekspresinya.
* _preprocessing.py_ : untuk melakukan proses preprocessing dengan mengambil bagian wajah.
* _feature_extraction.py_ : melakukan feature extraction dengan _landmark_.
* _klasifikasi.py_ : melakukan proses klasifikasi dengan SVM.
## Pengelompokan
Dataset menggunakan [CK+](http://www.consortium.ri.cmu.edu/ckagree/) dengan mengambil 7 ekspresi. Untuk ekspresi yang diambil antara lain: _angry, disgust, fear, happy, sadness, surprise,_ dan _neutral_. Pada proses pengelompokan ini, untuk mengelompokan data berdasarkan label ekspresinya.
## _Preprocessing_
_Preprocessing_ bertujuan untuk mengambil daerah pada data yang terdeteksi sebagai wajah. Deteksi wajah menggunakan Haar-cascade dari pustaka [OpenCV](https://github.com/opencv/opencv/tree/master/data/haarcascades).
## _Feature Extraction_
Pembentukan _feature_ dengan menggunakan deteksi titik landmark sebanyak 68 titik. Untuk _feature_ yang disimpan pada masing-masing titik adalah nilai koordinat x, nilai koordinat y, jarak titik dengan titik pusat, dan besar sudut. Sehingga jumlah _feature_ yang dihasilkan tiap data sebanyak 272 _feature_.
## Klasifikasi
Klasifikasi menggunakan _Support Vector Machines_ dan kernel yang digunakan adalah linear. Untuk _class_ yang digunakan berjumlah 7 sesuai dengan ekspresi yang digunakan.
