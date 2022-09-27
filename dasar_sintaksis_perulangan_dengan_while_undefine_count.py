"""
program perulangan dengan while sampai paham (Undefined count)
"""
jumlah_buku = 10
print(f"Jumlah buku yang inin dibaca adalah {jumlah_buku} buku")

jumlah_baca = 0
print(f"Jumlah buku yang sudah dibaca sebanyak {jumlah_baca} buku\n")

jumlah_paham = 0

while jumlah_paham < jumlah_buku * 2:
    jumlah_paham = jumlah_paham + 1
    if jumlah_baca == 9:
        print(f"buku ke {jumlah_baca + 1} Belum paham")
    else:
        jumlah_baca = jumlah_baca + 1
        print(f"jumlah buku ke {jumlah_baca} sudah dibaca dan dipahami")

print("jumlah buku yang sudah dibaca", jumlah_baca)

if jumlah_baca == jumlah_buku:
    print("semua buku budi telah baca dan pahami")
else:
    print(f"maaf bu tidak semua buku bisa dipahami, budi hanya bisa memahami {jumlah_baca} buku")

