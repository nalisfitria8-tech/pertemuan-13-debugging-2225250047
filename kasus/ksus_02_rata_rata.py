# Kasus 2: Bug Rata-rata (Logical Error / Hardcoded Pembagi)
def rata_rata(data):
    total = sum(data)
    return total / 5  # Bug: pembagi di-hardcode 5

print(rata_rata([80, 90, 70]))  # Output salah: 48.0 (seharusnya 80.0)