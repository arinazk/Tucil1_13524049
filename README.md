# Tucil1_13524049 Queens LinkedIn Solver  

Queens LinkedIn Solver adalah aplikasi berbasis Python yang mengimplementasikan Brute Force untuk menyelesaikan permainan logika **Queens LinkedIn**, yaitu variasi dari permasalahan klasik N-Queens dengan tambahan batasan khusus. Aplikasi ini menyediakan dua pendekatan algoritma utama, yaitu Exhaustive Search dan Backtracking.

Selain implementasi algoritma, aplikasi ini dilengkapi dengan antarmuka grafis (GUI) modern menggunakan `customtkinter` yang memungkinkan pengguna untuk memvisualisasikan proses pencarian solusi secara real-time serta menganalisis performa algoritma.

---

## a. Penjelasan Singkat Program

Program ini merupakan aplikasi berbasis GUI yang dirancang untuk menyelesaikan permasalahan penempatan Ratu (Queens Problem) dengan batasan tambahan berupa wilayah (region/warna) pada papan.

Setiap ratu harus memenuhi ketentuan berikut:

- Tidak berada pada baris yang sama.
- Tidak berada pada kolom yang sama.
- Tidak berada pada daerah yang sama.
- Tidak saling bersinggungan dengan ratu lain, baik secara vertikal, horizontal, ataupun diagonal.

Program menyediakan dua pendekatan algoritma:

1. **Exhaustive Search**  
   Menelusuri seluruh kemungkinan solusi tanpa pemangkasan sejak awal, lalu memvalidasi solusi di akhir.

2. **Backtracking**  
   Menggunakan teknik pruning (pemangkasan cabang) dengan melakukan pengecekan validitas di setiap langkah rekursi sehingga ruang pencarian berkurang secara signifikan.

Aplikasi juga menyediakan visualisasi proses pencarian solusi secara real-timw, statistik eksekusi, serta fitur ekspor hasil ke format gambar.

---

## b. Requirement Program dan Instalasi

### Requirement Sistem

- Python 3.x
- Sistem Operasi: Windows / Linux / macOS

### Library yang Dibutuhkan

Install dependency berikut sebelum menjalankan program:

```bash
pip install customtkinter pillow numpy
```

### Struktur Folder 

Pastikan struktur direktori sebagai berikut:

```
Tucil1_13524049/
│
├── bin/
├── doc/
├── src/
│   ├── assets/
│   │   └── queen.png
│   ├── modules/
│   │   └── file_processing.py
│   │   └── queen_linkedin.py
│   └── main.py
├── test/
└── README.md
```

Folder `assets/` wajib berisi file gambar `queen.png`.

---

## c. Cara Mengkompilasi Program 

Program dapat dijalankan langsung menggunakan Python.  
Namun, jika ingin membuat file executable (.exe), gunakan PyInstaller.

### Install PyInstaller

```bash
pip install pyinstaller
```

### Build Executable

Dari root folder project, jalankan:

```bash
python -m PyInstaller --onefile --windowed --distpath bin --add-data "src/assets;assets" src/main.py
```

Setelah proses selesai, file executable akan berada di:

```
bin/main.exe
```

File tersebut dapat dijalankan tanpa perlu menginstal Python kembali.

---

## d. Cara Menjalankan dan Menggunakan Program

### Menjalankan Program

Dari root folder project, jalankan:

```bash
python src/main.py
```

Atau jika sudah dibuat executable:

```
bin/main.exe
```

### Cara Menggunakan Program

1. Klik tombol **Import File** untuk mengunggah file konfigurasi papan dalam format `.txt`.
2. Pilih mode algoritma:
   - Nonaktifkan optimasi → Exhaustive Search
   - Aktifkan optimasi → Backtracking
3. Klik **Solve** untuk memulai pencarian solusi.
4. Tunggu hingga proses selesai.
5. Klik **Save Board as Image** untuk menyimpan hasil solusi dalam format `.png`.

### Format File Input

File input harus berupa matriks karakter (A–Z) yang merepresentasikan daerah warna.

Contoh:

```
AAAB
BCCC
BBDD
EEED
```

Ketentuan:
- Papan harus berbentuk persegi (n × n).
- Jumlah wilayah unik harus sama dengan ukuran papan (n).

---

## e. Author / Identitas Pembuat

**Nama**: Arina Azka  
**NIM**: 13524049 
**Program Studi**: Teknik Informatika  

---
