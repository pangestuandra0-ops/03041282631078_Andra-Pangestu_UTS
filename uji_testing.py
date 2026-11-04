# PENGUJIAN PROGRAM 

def kategori(nilai):
    if nilai < 60:
        return "RENDAH"
    elif nilai < 80:
        return "SEDANG"
    else:
        return "TINGGI"


test_case = [
    (59, "RENDAH"),
    (60, "SEDANG"),
    (61, "SEDANG"),
    (79, "SEDANG"),
    (80, "TINGGI"),
    (81, "TINGGI"),
    (42, "RENDAH"),
    (95, "TINGGI")
]

print("===== HASIL PENGUJIAN =====")

for nomor, (nilai_uji, expected) in enumerate(test_case, start=1):
    actual = kategori(nilai_uji)

    if actual == expected:
        status = "PASS"
    else:
        status = "FAIL"

    print(f"Test {nomor}: Nilai {nilai_uji}")
    print(f"Expected : {expected}")
    print(f"Actual   : {actual}")
    print(f"Status   : {status}")
    print("------------------------")