# Latihan 3: Pengujian Test Case Nilai Batas
def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

# Pengujian dengan test case
test_cases = [
    (75, "Lulus"),
    (60, "Lulus"),
    (59, "Tidak lulus")
]

for nilai, expected in test_cases:
    actual = status_lulus(nilai)
    status_test = "PASS" if actual == expected else "FAIL"
    print(f"Input: {nilai} | Expected: {expected} | Actual: {actual} | Status: {status_test}")