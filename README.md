# Pertemuan 13 Debugging dan Testing
Nama: Nalis fitria
NIM: 2225250047
Kelas: 3f

## Kasus
Program yang diuji adalah program pengolah data nilai mahasiswa yang memiliki 3 fungsi utama: `hitung_rata_rata`, `status` (kelulusan), dan `nilai_tertinggi`[cite: 9]. Program awal memuat beberapa *logical error* pada pembagi nilai rata-rata, operator kelulusan batas, dan logika pencarian nilai tertinggi[cite: 9].

## Test Case
| ID | Target | Input | Expected | Actual Awal | Status Awal |
|----|--------|-------|----------|-------------|-------------|
| T1 | rata-rata | [80, 60, 90, 70] | 75.0 | 60.0 | FAIL |
| T2 | rata-rata | [100, 80] | 90.0 | 36.0 | FAIL |
| T3 | status | 60 | Lulus | Tidak lulus | FAIL |
| T4 | status | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | tertinggi | [80, 60, 90, 70] | 90 | 0 | FAIL |

## Bug Report
- **B01 (hitung_rata_rata)**:
  - *Gejala*: Hasil rata-rata salah ketika jumlah elemen list bukan 5[cite: 9].
  - *Lokasi*: Fungsi `hitung_rata_rata`[cite: 9].
  - *Akar Penyebab*: Pembagi di-hardcode menggunakan angka `5`[cite: 9].
  - *Perbaikan*: Mengganti angka `5` dengan `len(nilai)` dan menambahkan penanganan list kosong[cite: 13, 14].
- **B02 (status)**:
  - *Gejala*: Nilai 60 dinyatakan "Tidak lulus"[cite: 9].
  - *Lokasi*: Fungsi `status`[cite: 9].
  - *Akar Penyebab*: Penggunaan operator kondisi `>` yang mengecualikan nilai batas[cite: 9].
  - *Perbaikan*: Mengubah operator menjadi `>=`[cite: 13, 14].
- **B03 (nilai_tertinggi)**:
  - *Gejala*: Fungsi mengembalikan `0` padahal ada nilai yang lebih besar[cite: 9].
  - *Lokasi*: Fungsi `nilai_tertinggi`[cite: 9].
  - *Akar Penyebab*: Logika pembanding salah arah (`x < tertinggi`)[cite: 9].
  - *Perbaikan*: Menginisialisasi `tertinggi = nilai[0]` dan memperbaikinya menjadi `x > tertinggi`[cite: 13, 14].

## Retest
| ID | Target | Input | Expected | Actual Akhir | Status Akhir |
|----|--------|-------|----------|--------------|--------------|
| T1 | rata-rata | [80, 60, 90, 70] | 75.0 | 75.0 | PASS |
| T2 | rata-rata | [100, 80] | 90.0 | 90.0 | PASS |
| T3 | status | 60 | Lulus | Lulus | PASS |
| T4 | status | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | tertinggi | [80, 60, 90, 70] | 90 | 90 | PASS |

## Cara Menjalankan
```bash
python3 praktik/praktik_4_debugging.py