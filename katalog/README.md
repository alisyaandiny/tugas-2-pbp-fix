**Link Heroku**
https://tugas-2-pbp-alisya.herokuapp.com/katalog/

**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;**
![RequestClient](https://user-images.githubusercontent.com/113089408/190290863-74de068c-dd30-44b5-9b87-04ff844ca052.png)
MVT
- Model : interface dari data yang bertanggung jawab untuk menjaga data.
- Views : yang dilihat di browser saat merender situs web.
- Template : untuk menyediakan frontend dan layout ke situs web.

Bagan di atas merupakan alur sebuah permintaan yang diproses di Django. Pertama, setiap request oleh user akan masuk ke dalam server Django melalui urls yang berisikan definisi alamat URL (route) dan fungsi yang akan dieksekusi di setiap rutenya. Lalu, akan dilanjutkan ke views untuk memproses permintaan yang didefinisikan oleh developer. Jika database diperlukan, views akan memanggil query ke models dan hasil dari query tersebut akan dikembalikan dari database ke views. Kemudian, hasil permintaan yang telah selesai diproses akan dipetakan ke dalam HTML yang sudah didefinisikan sebelumnya. HTML tersebut merupakan respons yang akan dikembalikan ke user.

**Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
Virtualenv merupakan tools untuk membuat lingkungan Python virtual yang terisolasi, artinya tertutup dan tidak bisa diakses dari dunia luar. Di dalam virtualenv, Python memiliki modul-modul sendiri dan tidak dapat diakses oleh program dari luar. Misalnya, saat membuat aplikasi menggunakan Django 1.1. Aplikasi akan berjalan menggunakan versi 1.1. Namun setelah rilis versi baru dan melakukan upgrade modul, aplikasi yang sudah dibuat sebelumnya tidak dapat berjalan karena memiliki beberapa perubahan fungsi. Maka dari itu, virtualenv digunakan agar masing-masing dari setiap aplikasi memiliki modulnya sendiri. Jika tanpa virtualenv, aplikasi 1.1 akan menjadi yang berikutnya dan semua modul yang dibutuhkan akan ikut diperbarui setiap menggunakan pip. 

**Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**
Pertama, saya melakukan clone dari template yang diberikan di repositori GitHub. Lalu, saya membuat venv, melakukan install dependensi, dan melakukan migrasi. Kemudian, saya membuat melengkapi views.py dan menggunakan metode di models.py. Saya menuliskan nama dan id siswa yang dimuat dalam kamus yang akan dipetakan pada masing-masing bidang di file HTML dan mengembalikan file tersebut yang dirender dengan kamus. Saya mendefinisikan routing di katalog dan mendaftarkannya ke project_django. Kemudian, saya menghubungkan GitHub saya dengan Heroku.
