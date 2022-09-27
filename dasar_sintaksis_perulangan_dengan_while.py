"""
program perulangan dengan while
"""
jumlah_buku = 30
print(f"Jumlah buku yang inin dibaca adalah {jumlah_buku} buku")

jumlah_buku_yang_dibaca = 0
print(f"Jumlah buku yang sudah dibaca sebanyak {jumlah_buku_yang_dibaca} buku")

while jumlah_buku_yang_dibaca < jumlah_buku:
    jumlah_buku_yang_dibaca = jumlah_buku_yang_dibaca + 1
    print(f"jumlah buku ke {jumlah_buku_yang_dibaca} telah dibaca")

print("buku yang telah dibaca sejumlah:", jumlah_buku)