Nama: Micguel Katili
NPM: 2506588065
Kelas: PBP D

==========Tugas 2==========
Update: Membuat halaman Project. Di halaman ini, warna tema web berubah. Selain menambahkan card-card project seperti yang diminta tugas 2, ditambahkan juga fitur yang memberikan highlight terhadap card yang sedang ditunjuk oleh cursor. Warna border dari card berubah dan warna blur di sekitar card muncul, serta gambar tambahan di kanan atas halaman.

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