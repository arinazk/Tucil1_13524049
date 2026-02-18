# Tucil1_13524049
# Queens LinkedIn Solver  
Implementasi penyelesaian permasalahan Queens LinkedIn menggunakan Brute Force.

---

## Deskripsi Proyek

Queens LinkedIn Solver adalah aplikasi berbasis Python yang dikembangkan untuk menyelesaikan permasalahan logika **Queens LinkedIn**, yaitu variasi dari permasalahan klasik N-Queens dengan tambahan batasan khusus.

Aplikasi ini menyediakan dua pendekatan algoritma utama:

1. Exhaustive Search (Brute Force)
2. Backtracking dengan Pruning (Optimized)

Selain implementasi algoritma, aplikasi ini dilengkapi dengan antarmuka grafis (GUI) modern menggunakan `customtkinter` yang memungkinkan pengguna untuk memvisualisasikan proses pencarian solusi secara real-time serta menganalisis performa algoritma.

Proyek ini dikembangkan untuk keperluan akademik dalam rangka studi algoritma brute force, rekursi, backtracking, dan analisis kompleksitas.

---

## Spesifikasi Permasalahan

Diberikan sebuah papan berukuran N × N yang terdiri dari huruf kapital (A–Z). Setiap huruf merepresentasikan sebuah region warna.

Tujuan: Menempatkan N buah queen pada papan sehingga memenuhi seluruh batasan berikut.
1. Setiap kolom memiliki tepat satu queen.
2. Tidak ada dua queen berada pada baris yang sama.
3. Tidak ada dua queen berada pada region warna yang sama.
4. Queen pada kolom yang bersebelahan tidak boleh berada pada baris yang selisihnya 1 (tidak boleh bersinggungan secara vertikal).

Solusi direpresentasikan sebagai array satu dimensi dengan ketentuan sebagai berikut:

- Indeks array merepresentasikan **kolom** pada papan.
- Nilai pada indeks tersebut merepresentasikan **baris** tempat queen ditempatkan pada kolom tersebut.

---

## Fitur Utama

### 1. Penyelesaian Permasalahan dengan Constraint Lengkap
Aplikasi mampu menyelesaikan papan permainan Queens LinkedIn dengan memperhatikan seluruh batasan berikut:
- Tidak ada dua queen pada baris yang sama.
- Tidak ada dua queen pada region warna yang sama.
- Tidak ada queen yang bersinggungan secara vertikal (adjacent) pada kolom bersebelahan.

Sistem validasi dilakukan secara otomatis selama proses pencarian solusi.

---

### 2. Dua Mode Algoritma

#### a. Exhaustive Search
- Menelusuri seluruh ruang pencarian secara sistematis.
- Tidak melakukan pemangkasan cabang pencarian.
- Validasi solusi dilakukan setelah seluruh queen ditempatkan.
- Digunakan sebagai pembanding performa terhadap metode teroptimasi.

#### b. Backtracking (Optimized)
- Menggunakan teknik pruning untuk menghentikan cabang yang tidak valid sedini mungkin.
- Melakukan pengecekan keamanan pada setiap langkah rekursi.
- Secara signifikan mengurangi jumlah node yang dieksplorasi.
- Memberikan performa yang jauh lebih efisien dalam praktik.

---

### 3. Visualisasi Real-time
Selama proses pencarian berlangsung, aplikasi menampilkan visualisasi papan secara dinamis sehingga pengguna dapat mengamati proses eksplorasi solusi oleh algoritma.

---

### 4. Statistik Eksekusi
Aplikasi menyediakan informasi performa algoritma secara langsung, meliputi:
- Waktu eksekusi (Execution Time)
- Total kasus atau node yang diperiksa selama proses pencarian

Fitur ini memungkinkan analisis dan perbandingan performa antara Exhaustive Search dan Backtracking.

---

### 5. Ekspor Papan
Papan dapat disimpan dalam format gambar `.png`.

---
## Instalasi

### Prasyarat
Pastikan sistem telah terinstal **Python 3.x**.

### Instalasi Dependensi

Jalankan perintah berikut pada terminal:

```bash
pip install customtkinter pillow numpy




