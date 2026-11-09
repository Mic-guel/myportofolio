Nama: Micguel Katili
NPM: 2506588065
Kelas: PBP D

==========Tugas 6==========
Update: Mengimplementasikan Django REST Framework (DRF) pada model Achievement dengan role-based permissions (IsPortfolioOwnerOrEditorOrReadOnly), modal Edit interaktif untuk Superuser & Editor via PATCH API, serta fitur ekstra interaktif berupa filter "Show Starred" dan live counter badge pada antarmuka AJAX.

1. REST tidak hanya berupa format respons. Mengembalikan JSON tidak berarti API tersebut RESTful jika belum memenuhi prinsip seperti Uniform Interface.
PUT: Mengganti suatu data keseluruhan, misalnya mengganti seluruh informasi/atribut pada data
PATCH: Mengganti salah satu informasi data, misalnya hanya mengganti nomor telfon pada suatu tuple of data

2. Peran Serializer pada Django REST Framework
Serializer bertugas menerjemahkan tipe data kompleks (seperti QuerySet atau model instance Django) menjadi tipe data native Python agar mudah dirender menjadi JSON/XML. Serializer juga menangani deserialisasi (mengubah JSON kembali menjadi objek Python) sekaligus melakukan validasi data secara otomatis.
Keuntungannya dibandingkan merakit dictionary secara manual untuk JsonResponse:
-Efisiensi kode.
Serializer otomatis memetakan field model, menghilangkan kebutuhan menulis konversi dictionary secara berulang (boilerplate code).
-Validasi otomatis: Serializer langsung memvalidasi tipe data, batas panjang karakter, dan konstrain lainnya sebelum data disimpan ke database.
-Relasi data: Menangani nested relationship antar tabel/model (seperti Foreign Key) jauh lebih rapi.

3. Autentikasi vs Otorisasi dan Keamanan API

Autentikasi: Proses memverifikasi identitas pengguna (memastikan siapa yang mengakses aplikasi, biasanya lewat mekanisme login).

Otorisasi: Proses menentukan hak akses (memastikan apa yang boleh diakses atau diubah oleh pengguna tersebut).

Menyembunyikan tombol di template atau HTML hanyalah manipulasi antarmuka klien. Pengguna yang mengetahui URL endpoint dapat dengan mudah melewati antarmuka tersebut dan mengirim request modifikasi data secara langsung menggunakan tools seperti Postman, cURL, atau script otomatis. Permission class memastikan otorisasi diterapkan pada level server, menolak request secara absolut jika tidak memiliki hak akses.

4. Saat API menggunakan SessionAuthentication, kredensial pengguna disimpan dalam cookie. Browser secara otomatis melampirkan cookie ini ke setiap request yang mengarah ke domain server, terlepas dari mana asal request tersebut. Token CSRF diwajibkan untuk memastikan bahwa request modifikasi (POST, PUT, DELETE) benar-benar berasal dari frontend aplikasi yang sah, bukan dari situs pihak ketiga yang mencoba memanfaatkan cookie sesi yang sedang aktif.

Penggunaan force_authenticate dalam testing DRF dirancang untuk memotong (bypass) lapisan middleware dan proses evaluasi autentikasi reguler, dengan cara menyuntikkan objek user langsung ke dalam request. Akibat jalan pintas ini, mekanisme pengecekan CSRF ikut terlewati, sehingga pengujian tersebut tidak dapat memvalidasi apakah perlindungan CSRF di aplikasi berfungsi dengan benar di kondisi nyata.

Saya mengakui jawaban saya dibantu oleh AI
==========Tugas 6==========

==========Tugas 5==========
Update: Mengaplikasikan tutorial 5 pada page lain

Link percakapan dengan AI: https://share.gemini.google/VoFaQJvRabLe

1. Debouncing pada Fitur Pencarian AJAX   Pengertian: Debouncing adalah teknik pemrograman yang menunda eksekusi sebuah fungsi sampai ada jeda waktu tertentu (misalnya 300ms) sejak pemicu fungsi tersebut terakhir kali dipanggil.Urgensi pada AJAX: Saat pengguna mengetik di kolom pencarian, pengetikan sering terjadi dengan sangat cepat. Tanpa debouncing, setiap ketikan tombol (keystroke) akan langsung memicu pengiriman request HTTP ke server. Hal ini menyebabkan server kelebihan beban akibat spam request, pemborosan bandwidth, dan potensi terjadinya race condition (respons dari request yang lama datang terlambat dan menimpa hasil dari request yang lebih baru). Debouncing memastikan request hanya dikirim saat pengguna sudah berhenti mengetik sejenak.

2. Penggunaan await pada fetch()   Fungsi await: Fungsi fetch() bersifat asinkron dan secara bawaan mengembalikan sebuah Promise. Keyword await digunakan untuk menjeda eksekusi kode di baris tersebut sampai Promise dari fetch() selesai diproses (resolved) oleh jaringan dan mengembalikan objek Response dari server.Jika await tidak digunakan: Eksekusi kode tidak akan menunggu proses pengambilan data selesai. JavaScript akan langsung mengeksekusi baris kode berikutnya. Variabel yang menampung hasil fetch() hanya akan berisi objek Promise dengan status pending, bukan data aktual dari server. Ini akan menyebabkan error saat kode selanjutnya mencoba membaca atau merender data (seperti JSON) karena datanya belum benar-benar tiba.

3. Serangan XSS (Cross-Site Scripting)   Pengertian: XSS adalah kerentanan keamanan di mana penyerang berhasil menyisipkan skrip klien (client-side script, biasanya JavaScript) berbahaya ke dalam situs web yang sah. Saat pengguna lain membuka halaman tersebut, browser mereka akan mengeksekusi skrip tersebut, yang dapat berujung pada pencurian cookie, token sesi, atau pembajakan akun.Kerentanan pada AJAX/JavaScript vs Django Template: Saat menampilkan data melalui JavaScript (misalnya DOM manipulation menggunakan innerHTML), browser akan membaca dan mengeksekusi tag HTML atau skrip apa pun yang ada di dalam string data tersebut secara mentah-mentah jika pengembang tidak melakukan pembersihan (sanitization) secara manual. Sebaliknya, template bawaan Django memiliki mekanisme perlindungan auto-escaping. Sebelum dikirim ke browser, Django secara otomatis mendeteksi dan mengubah karakter berbahaya (seperti mengubah <script> menjadi &lt;script&gt;). Ini menetralkan skrip sehingga browser hanya membacanya sebagai teks biasa dan tidak mengeksekusinya.

Saya mengakui jawaban saya dibuat oleh AI
==========Tugas 5==========

==========Tugas 4==========

Update: Membuat role editor yang memiliki hak lebih dari pengguna biasa, yaitu bisa mengubah informasi dari proyek-proyek yang sudah ada. Menambahkan fitur yang memberikan warna berbeda untuk kotak nama pengguna yang terletak di kanan atas bagi pengguna yang memiliki role spesial. Saat teks ini dibuat, hanya tersedia role editor dan super user.

Link percakapan dengan AI: https://share.gemini.google/EXAz8Jqw2naM
Penggunaan AI tidak semata-mata untuk meminta kode dan menyalinnya. Seandainya ada bagian yang tidak saya ketahui, saya meminta kode yang diperlukan ke AI, meminta penjelasannya, format syntax, dan variasi yang mungkin dari function/kode tersebut. Kode yang diberikan AI juga umumnya tidak bisa langsung bekerja karena kurangnya pengetahuan akan struktur file dan kode secara keseluruhan. Saya tetap harus mengintegrasikannya sendiri.
==========Tugas 4==========

==========Tugas 3==========
Update: Membuat halaman achievement yang memiliki fitur untuk emnambahkan dan menghapus achievement.

1. Menggunakan ModelForm mempermudah penambahan elemen tanpa harus menulis ulang kode. csrf_token digunakan untuk mencegah instruksi-instruksi/request-request yang dikirim dari aplikasi lain masuk dan mengubah data yang ada.
2. JSON lebih mudah untuk dimengerti.
3. Klien->Request URL->Django->Serializer function->Response. Mentranslasikan kompleksitas struktur data menjadi format string yang bersifat universal

Link percakapan dengan AI: https://share.gemini.google/lb6XXToHRoVX
==========Tugas 3==========

==========Tugas 2==========
Update: Membuat halaman Project. Di halaman ini, warna tema web berubah. Selain menambahkan card-card project seperti yang diminta tugas 2, ditambahkan juga fitur yang memberikan highlight terhadap card yang sedang ditunjuk oleh cursor. Warna border dari card berubah dan warna blur di sekitar card muncul, serta gambar tambahan di kanan atas halaman.

Link percakapan dengan AI: https://share.gemini.google/fjsAFK7jmQG8

1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.
->urls.py di portofolio berfungsi untuk menyimpan url utama web, sedangkan urls.py main berfungsi untuk menyimpan url halaman-halaman lain, seperti /experience dan /projects. View itu tempat untuk menyimpan fungsi-fungsi yang menerima request dan mengembalikan sebuah tampilan. Model berisikan objek-objek yang nantinya akan ditampilkan. Template merupakan kerangka utama sebuah tampilan/web.

2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.
Setelah bertanya ke AI, ternyata tidak melakukan hard-code itu lebih mudah untuk pengembangan. Misal datanya ada banyak, berarti semakin banyak line di file -> semakin sulit untuk diubah. Bisa juga memunculkan inkonsistensi karena kelupaan atribut misalnya. Mengandalkannya ke database juga sebuah kebiasaan yang baik, terutama jika data bisa berubah-ubah (bertambah/berkurang) atau skalanya besar.

3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.
makemigrations = Membuat persiapan untuk migrasi, misalnya membuat tabel berdasarkan entity/class dan atributnya. Sedangkan, migrate itu untuk mengintegrasikan hasil persiapan yang telah dilakukan oleh makemigrations ke database.
==========Tugas 2==========

==========Tugas 1==========
1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

1. Ya, saya menggunakan <section> karena elemen ini membantu saya saat saya ingin membuat button yang langsung mengarah ke section yang saya buat

2. Tantangan yang paling sering saya hadapi adalah memahami dan menentukan cara untuk mengatur posisi, batas, ataupun jarak elemen di web. Saya mengevaluasinya dengan mengaturnya terlebih dahulu dalam tampilan desktop, lalu saya ubah ke tampilan mobile dan mencari elemen yang tampilannya tidak sesuai harapan

3. Untuk sekarang, saya belum merasakan batasan apapun dalam menyajikan informasi pada portofolio.

https://share.gemini.google/mNCS0YnQKRVS

Saya menggunakan Gemini untuk membantu saya dalam pengerjaan tugas. Saya menggunakannya untuk memahami dan memeriksa kebenaran pengerjaan tugas saya. Contoh penggunaan AI dalam pengerjaan:
1. Mengirimkan screenshot untuk memeriksa kebenaran struktur file
2. Mencari kode warna dari gambar yang saya inginkan
3. Menanyakan fungsi, format, atau penggunaan kode HTMl ataupun CSS
4. Menanyakan cara melakukan sesuatu yang saya inginkan (membuat gap antarelemen)
5. Menanyakan alasan dan cara menyelesaikan error