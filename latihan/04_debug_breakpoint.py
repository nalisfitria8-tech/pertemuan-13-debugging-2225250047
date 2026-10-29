# Latihan 4: Praktik Breakpoint VS Code
def hitung_total(daftar_harga):
    total = 0
    for harga in daftar_harga:
        total += harga
    return total

items = [15000, 25000, 50000]
print("Total Belanja:", hitung_total(items))