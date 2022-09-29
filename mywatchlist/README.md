**Link Heroku :**
https://tugas-2-pbp-alisya.herokuapp.com/mywatchlist/json/
https://tugas-2-pbp-alisya.herokuapp.com/mywatchlist/xml/
https://tugas-2-pbp-alisya.herokuapp.com/mywatchlist/html/


**Jelaskan perbedaan antara JSON, XML, dan HTML!**
JavaScript Object Notation (JSON) adalah format data yang biasa digunakan dalam pembuatan website untuk membaca, menyimpan, dan menukar informasi dari web server agar dapat dibaca user.
Extensible Markup Language (XML) adalah bahasa yang dibuat oleh World Wide Web Consortium (W3C) untuk menyederhanakan proses pertukaran dan penyimpanan data.
Hypertext Markup Language (HTML) adalah bahasa markup standar yang digunakan untuk membuat dan menyusun halaman serta aplikasi web.

Perbedaan:
1. Cara menyimpan elemen
JSON dapat menyimpan elemen secara efisien tetapi kurang rapi dilihat. XML menyimpan elemen secara terstruktur, mudah dibaca oleh manusia dan mesin, tetapi kurang efisien. HTML tidak terdiri dari data struktural.

2. Ekstensi file
Nama file JSON diakhiri dengan ekstensi .json. Nama file XML diakhiri dengan ekstensi .xml. Nama file HTML diakhiri dengan ekstensi .html.


3. Penerapan
JSON digunakan untuk mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet. XML memiliki data yang lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan, bersifat case sensitive, dan memerlukan tag penutup. HTML memiliki fokus pada penyajian data, bersifat case insensitive, dan tidak memerlukan tag penutup.


4. Kecepatan
JSON memiliki ukuran  file sangat kecil dan penguraian lebih cepat oleh mesin JavaScript sehingga dapat mentransfer data lebih cepat. XML memiliki ukuran file yang besar dan cenderung lambat dalam proses penguraian sehingga menyebabkan transmisi data lebih lambat. 


**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Data delivery perlu digunakan dalam pengimplementasian sebuah platform karena dapat memudahkan user untuk menghubungkan kode dan menampilkan output ke berbagai platform dengan satu source code saja.


**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
Pertama, saya membuat aplikasi mywatchlist dengan perintah python manage.py startapp mywatchlist. Lalu, saya menambahkan aplikasi mywatchlist di INSTALLED_APPS yang ada pada settings.py. Saya juga menyesuaikan isi dalam urls.py. Kemudian, saya menambahkan atribut watched, title, rating, release_date, dan review pada models.py. Saya membuat folder fixtures yang berisi file JSON pada aplikasi mywatchlist untuk memasukkan data-data. Setelah itu, saya melengkapi fungsi show_mywatchlist, show_xml, show_json, show_json_by_id, dan show_xml_by_id pada views.py. Saya juga menambahkan path sesuai fungsi yang ada pada views.py ke dalam urls.py. Terakhir, saya melakukan push ke GitHub dan menghubungkan ke Heroku.


**Mengakses tiga URL di poin 6 menggunakan Postman, menangkap screenshot, dan menambahkannya ke dalam README.md**
https://tugas-2-pbp-alisya.herokuapp.com/mywatchlist/json/
Screenshot: https://drive.google.com/file/d/11jryYySIyy9Vh5_JLgJB4oZ_Sk2ciAbF/view?usp=sharing


https://tugas-2-pbp-alisya.herokuapp.com/mywatchlist/xml/
Screenshot: https://drive.google.com/file/d/1Ko2RbiotJ6Jb27ilfi3pONdJiBNgZnkh/view?usp=sharing


https://tugas-2-pbp-alisya.herokuapp.com/mywatchlist/html/
Screenshot: https://drive.google.com/file/d/1Ts9EXRD4_2rcd0G2NIDzO2Gcn5_oOeND/view?usp=sharing
