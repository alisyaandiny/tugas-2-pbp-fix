# Link Heroku: #

https://tugas-2-pbp-alisya.herokuapp.com/todolist/

# Jelaskan perbedaan antara asynchronous programming dengan synchronous programming. #

Asynchronous web communication adalah komunikasi web yang memiliki tipe komunikasi parsial. Penerimaan request dari user kepada server akan diterima lalu dikirimkan respons yang bersifat parsial dan tidak merubah keseluruhan isi dari aplikasi. Jadi user hanya akan menerima respons berupa page (untuk web) yang bersifat hanya untuk dia saja. User juga tetap bisa berinteraksi dengan aplikasi tanpa menunggu response dari server.

Berbeda dengan synchronous web communication yang memiliki tipe komunikasi permanen. Permintaan user akan diterima dan berikan response yang akan meng-update isi aplikasi, lalu baru memberikannya kepada user. Pada synchronous web communication juga dia akan membuat user menunggu response dari server dan membuat user tidak bisa berinteraksi selama proses menunggu response dari server.


# Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini. #

Sesuai dengan namanya, event-driven programming merupakan sebuah paradigma yang menyatakan bahwa setiap response yang diberikan oleh program dipicu oleh oleh suatu event, perilaku, atau aksi yang dilakukan antara user dan server. Event - event ini dapat berupa sebuah klik tombol, hover dari elemen, bahkan koordinat dari kursor mouse. Salah satu contoh event-driven programming, yaitu implementasi AJAX GET maupun POST yang secara asinkronus dilakukan pada background setelah sebuah button ditekan.

# Jelaskan penerapan asynchronous programming pada AJAX. #

AJAX menerapkan asynchronous programming sehingga developer tidak perlu me-reload browser jika ada perubahan data yang kecil. AJAX secara otomatis akan melakukan update semua perubahan-perubahan yang dibuat developer ke websitenya. Hal ini disebut asynchronous programming karena AJAX tidak perlu menunggu respon dari server terkait request yang diajukan pada saat mengeksekusi program.


# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. #

1. Menambahkan beberapa fungsi baru pada views.py untuk mengambil data yang direpresentasikan dengan JSON
2. Menambahkan path di urls.py untuk function yang sudah ditambahkan pada views.py
3. Membuat fungsi GET pada todolist.py untuk mengambil data yang akan ditampilkan
4. Mengganti href atau link pemetaan
5. Membuat fungsi POST pada todolist.html untuk menambahkan data dari user
6. Fitur add akan dilakukan secara asynchronous
