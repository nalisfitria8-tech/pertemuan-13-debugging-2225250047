# ==============================================================================
# PROGRAM PERBAIKAN PRAKTIK 4: DEBUGGING DAN TESTING
# ==============================================================================

def hitung_rata_rata(nilai):
    """
    Menghitung rata-rata nilai dari sebuah list.
    Akar Bug Awal: Pembagi di-hardcode dengan angka 5 dan tidak menangani list kosong.
    Perbaikan: Menggunakan len(nilai) sebagai pembagi dinamis dan penanganan list kosong.
    """
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)

def status(nilai):
    """
    Menentukan status kelulusan berdasarkan nilai.
    Akar Bug Awal: Operator '>' menyebabkan nilai 60 dianggap 'Tidak lulus'.
    Perbaikan: Mengubah operator menjadi '>=' agar nilai tepat 60 terhitung 'Lulus'.
    """
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    """
    Mencari nilai tertinggi dalam list.
    Akar Bug Awal: Variabel 'tertinggi' diinisialisasi 0 dan kondisi 'x < tertinggi'
                   salah arah dalam mencari nilai terbesar.
    Perbaikan: Inisialisasi 'tertinggi' dengan elemen pertama (nilai[0]),
               memeriksa list kosong, dan mengubah kondisi menjadi 'x > tertinggi'.
    """
    if len(nilai) == 0:
        return None
    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi

# --- EKSEKUSI PENGUJIAN ---
if __name__ == "__main__":
    nilai_sample = [80, 60, 90, 70]
    
    print("--- HASIL EKSEKUSI PROGRAM SETELAH PERBAIKAN ---")
    print("Rata-rata:", hitung_rata_rata(nilai_sample))
    print("Status 60:", status(60))
    print("Status 59:", status(59))
    print("Tertinggi:", nilai_tertinggi(nilai_sample))