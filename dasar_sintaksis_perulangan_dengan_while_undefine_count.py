"""
program perulangan dengan while sampai paham (Undefined count)
"""
jumlah_buku = 10
print(f"Jumlah buku yang inin dibaca adalah {jumlah_buku} buku")

jumlah_buku_dibaca_dan_dipahami = 0
print(f"Jumlah buku yang sudah dibaca sebanyak {jumlah_buku_dibaca_dan_dipahami} buku\n")

total_jumlah_baca = 0

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_dibaca_dan_dipahami == 9:
        print(f"buku ke {jumlah_buku_dibaca_dan_dipahami + 1} Belum paham")
    else:
        jumlah_buku_dibaca_dan_dipahami = jumlah_buku_dibaca_dan_dipahami +1
        print(f"jumlah buku ke {jumlah_buku_dibaca_dan_dipahami} sudah dibaca dan dipahami")

print("jumlah buku yang sudah dibaca", jumlah_buku_dibaca_dan_dipahami )

if jumlah_buku_dibaca_dan_dipahami == jumlah_buku:
    print("semua buku budi telah baca dan pahami")
else:
    print(f"maaf bu tidak semua buku bisa dipahami, budi hanya bisa memahami {jumlah_buku_dibaca_dan_dipahami} buku")

