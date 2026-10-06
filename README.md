# MINI PROGRAM KASIR

Mini Program Kasir merupakan program sederhana berbasis Python yang digunakan untuk melakukan transaksi penjualan.

Project ini dibuat sebagai tugas Software Testing dengan menerapkan Functional Testing, Root Cause Analysis (RCA), Regression Testing, serta Git dan GitHub sebagai version control.

## Struktur Project

    mini-program-kasir/
    ├── versi-fault/
    │   └── kasir.py
    ├── versi-benar/
    │   └── kasir.py
    ├── dokumentasi/
    │   ├── test-case.md
    │   ├── rca.md
    │   └── regression-testing.md
    └── README.md

## Versi Program

### Versi Fault

Folder `versi-fault` berisi kode program sebelum dilakukan perbaikan.

Pada versi ini terdapat beberapa kesalahan:

1. Perhitungan diskon salah.
2. Perhitungan kembalian salah.
3. Tidak terdapat validasi uang pelanggan.

### Versi Benar

Folder `versi-benar` berisi kode program setelah dilakukan perbaikan.

Perbaikan yang dilakukan:

1. Memperbaiki perhitungan diskon.
2. Memperbaiki perhitungan kembalian.
3. Menambahkan validasi uang pelanggan.

## Dokumentasi

- `dokumentasi/test-case.md` berisi test case sebelum dan sesudah perbaikan.
- `dokumentasi/rca.md` berisi Root Cause Analysis.
- `dokumentasi/regression-testing.md` berisi hasil regression testing.

## Hasil Pengujian

| Tahap | PASS | FAIL |
|---|---:|---:|
| Sebelum Perbaikan | 0 | 4 |
| Setelah Perbaikan | 4 | 0 |

## Teknologi

- Python
- Git
- GitHub

## Kesimpulan

Setelah dilakukan perbaikan dan regression testing, seluruh test case berhasil menghasilkan status PASS.