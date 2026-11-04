
# 1. DATA NILAI (15 DATA INTI + 5 DATA TAMBAHAN)

data_nilai = [
    42, 55, 61, 68, 73,
    79, 82, 87, 91, 64,
    58, 76, 84, 49, 95,
    59, 60, 80, 81, 0
]


# 2. FUNCTION UNTUK MENENTUKAN KATEGORI

def kategori(nilai):
    if nilai < 60:
        return "RENDAH"
    elif nilai < 80:
        return "SEDANG"
    else:
        return "TINGGI"


# 3. FUNCTION UNTUK MENGHITUNG RATA-RATA

def rata_rata(data):
    return sum(data) / len(data)


# 4. FUNCTION UNTUK MENGHITUNG JUMLAH KATEGORI

def hitung_kategori(data):
    rendah = 0
    sedang = 0
    tinggi = 0

    for nilai in data:
        hasil = kategori(nilai)

        if hasil == "RENDAH":
            rendah += 1
        elif hasil == "SEDANG":
            sedang += 1
        else:
            tinggi += 1

    return rendah, sedang, tinggi


# 5. PROGRAM UTAMA

print("========================================")
print("       ANALISIS DAN KLASIFIKASI DATA")
print("========================================")

print("\n===== MONITORING =====")

# Memproses setiap data menggunakan perulangan

for nomor, nilai in enumerate(data_nilai, start=1):
    hasil = kategori(nilai)

    print(f"{nomor:02d}. Nilai = {nilai} -> {hasil}")


# 6. MENGHITUNG RINGKASAN DATA

jumlah_rendah, jumlah_sedang, jumlah_tinggi = hitung_kategori(data_nilai)

rata = rata_rata(data_nilai)
maksimum = max(data_nilai)
minimum = min(data_nilai)


# 7. MENAMPILKAN RINGKASAN

print("\n===== RINGKASAN =====")

print("Total data       :", len(data_nilai))
print("Kategori RENDAH  :", jumlah_rendah)
print("Kategori SEDANG  :", jumlah_sedang)
print("Kategori TINGGI  :", jumlah_tinggi)

print("Rata-rata        :", round(rata, 2))
print("Nilai maksimum   :", maksimum)
print("Nilai minimum    :", minimum)

print("========================================")
print("          PROGRAM SELESAI")
print("========================================")
