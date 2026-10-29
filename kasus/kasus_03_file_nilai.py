# Kasus 3: Bug File Kosong / Not Found (Runtime Error)
def baca_file(nama_file):
    try:
        with open(nama_file, "r") as f:
            data = f.readlines()
            if not data:
                return "File kosong"
            return data
    except FileNotFoundError:
        return "File tidak ditemukan"

print(baca_file("data_dummy.txt"))