Link Heroku
https://tugas-2-pbp-alisya.herokuapp.com/todolist


Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Cross-Site Request Forgery (CSRF) merupakan salah satu serangan tertua dan paling sederhana dalam sebuah web berupa tindakan dimana website diberikan tautan, formulir, atau beberapa permintaan lainnya yang dibuat oleh malicious user (penipu). {% csrf_token %} digunakan untuk melindungi website dari serangan berbahaya. Apabila tidak ada potongan kode tersebut pada elemen form, maka website tidak terlindungi dan berpotensi mendapatkan serangan siber.


Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Ya, kita dapat membuat elemen <form> secara manual dengan {{ form.name_of_field }}. Kita juga dapat membuat form secara manual dengan < form > pada file HTML yang datanya diambil menggunakan method request.POST.get('nama') yang digunakan untuk mengakses input dari user.


Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Pada saat user memasukkan input, browser akan memberi respons POST requesti. Kemudian, data tersebut akan dibersihkan dan divalidasi apakah sudah sesuai aturan atau tidak. Apabila tidak sesuai, browser akan memberi informasi ke user mengenai data yang tidak valid untuk melakukan prompt ulang. Apabila sudah sesuai, data dari user akan disimpan dan dijalankan untuk di-deliver melalui context serta di-render ke dalam templates (html).


Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Membuat aplikasi todolist dengan perintah python manage.py startapp todolist
1. Menambahkan aplikasi todolist ke dalam list INSTALLED_APPS yang ada pada settings.py
2. Mendaftarkan path aplikasi todolist pada urls.py di project django
3. Membuat class TaskItem yang meliputi user, date, title, dan description pada models.py
4. Membuat fungsi login, register, dan logout pada views.py serta menambahkan route fungsi tersebut pada urls.py dan dilanjutkan ke membuat template HTML nya
5. Membuat todolist.html, menampilkan user melalui ({{username}}) yang ada di context, membuat button create new task dan logout, membuat tabel yang berisikan date, title, dan description
6. Membuat createtask.html agar user dapat menambahkan to do dengan memasukkan title dan description
7. Membuat route agar terhubung pada fungsi-fungsi yang ada di views.py
8. Melakukan git push dan commit sehingga akan terdeploy pada Heroku
9. Membuat 2 user dan dan 3 dummy data di Heroku

2 user : alsyiii, anotheralsyi
