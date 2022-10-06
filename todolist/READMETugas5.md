# Link Heroku : #


# Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style? #

Cascading Style Sheets atau CSS merupakan bahasa pemrograman yang umum digunakan untuk mendesain tampilan website yang memiliki tiga metode penulisan kode berbeda, yaitu Inline CSS, Internal CSS, dan External CSS.

1. Inline CSS

Inline CSS merupakan kode CSS yang ditulis langsung pada atribut elemen HTML yang dituliskan pada atribut style pada setiap elemen HTML.

Kelebihan: Sangat membantu ketika ingin melihat perubahan pada satu elemen, berfungsi saat ingin memperbaiki kode dengan cepat, dam proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.

Kekurangan: Kurang efisien karena setiap tag HTML yang diberikan harus memiliki style masing-masing sehingga akan lebih sulit dalam mengatur website karena digunakan hanya untuk mengubah satu elemen saja.


2. Internal CSS

Internal CSS merupakan kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS bisa digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.

Kelebihan: Perubahan pada Internal CSS hanya berlaku pada satu halaman saja sehingga tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file. Class dan ID dapat digunakan oleh internal stylesheet.

Kekurangan: Tidak efisien saat ingin menggunakan CSS yang sama dalam beberapa file dan membuat performa website lebih lambat karena CSS yang berbeda-beda akan mengakibatkan loading ulang setiap mengganti halaman website.


3. External CSS

Eksternal CSS merupakan kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. Pada umumnya, file eksternal CSS diletakkan setelah bagian <head> pada halaman.

Kelebihan: Ukuran file HTML menjadi lebih kecil dan struktur dari kode HTML lebih rapi, loading website menjadi lebih cepat, dan file CSS dapat digunakan di beberapa halaman website sekaligus.

Kekurangan: Halaman akan menjadi berantakan ketika file CSS gagal dipanggil oleh file HTML, misalnya karena koneksi internet yang lambat.


# Jelaskan tag HTML5 yang kamu ketahui. #
<head> : mendefinisikan head dari document
'''<body>''' : mendefinisikan body dari document
<title> : mengatur judul halaman
<button> : membuat button yang dapat diklik
<table> : membuat tabel
<h1> hingga <h6> : mencetak tulisan sebagai header (semakin kecil angka, semakin besar ukuran yang dicetak)
<a> : me-refer pada link web tujuan
<p> : mencetak teks dalam bentuk paragraf
<hr> : menampilkan garis horizontal
<br> : memberikan line break atau jeda kosong
<tr> : mendefinisikan baris pada tabel
<td> : mendefinisikan kolom pada tabel
 
 
# Jelaskan tipe-tipe CSS selector yang kamu ketahui. #
  
1. Tag Selector
  
Selector yang akan memilih elemen berdasarkan nama tagnya.
  
p {
    color: blue;
}
  
  
2. ID Selector
  
Selector yang akan memilih elemen berdasarkan nama class yang diberikan dan hanya dapat digunakan pada tepat satu inisiasi elemen. ID Selector diawali dengan tanda pagar (#).
  
#header {
    background: teal;
    color: white;
    height: 100px;
    padding: 50px;
}

  
3. Class Selector
  
Hampir serupa dengan ID Selector, namun dapat digunakan oleh beberapa elemen. Class Selector diawali dengan tanda titik (.).
  
.pink {
  color: white;
  background: pink;
  padding: 5px;
}


# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. #

