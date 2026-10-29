# Kasus 1: Bug Batas Kelulusan (Logical Error)
def status_lulus(nilai):
    if nilai > 60:  # Bug: seharusnya >= 60
        return "Lulus"
    return "Tidak lulus"

print(status_lulus(75))  # Output: Lulus
print(status_lulus(60))  # Output: Tidak lulus (Harusnya Lulus)