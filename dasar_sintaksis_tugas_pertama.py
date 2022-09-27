"""
Dasar sintaksis bahasa pemrograman:
1. sekuensial
2. percabanyan
3. pengulangan
"""

# Sekuensial
print('Ibu berkata, "Beli 1 botol susu dan jika ada beli 6 buah telur"')
print('budi menjawab, "baik"')
print("maka budi berangkat ketoko")
print("dan mulai berbelanja")

# Percabangan
milkBottleCount = 234
eggCount = 2342
print(f"Jumlah Botol Susu {milkBottleCount} botol")
print(f"Jumlah telur {eggCount} buah")

if milkBottleCount > 0:
    print("budi mengecheck harga dan ternyata uangnya cukup")
    if eggCount == 0:
        print("Budi Membeli 1 botol susu")
    elif eggCount > 6:
        print("Budi membeli 6 butir telur")
else:
    print("Budi tidak membeli 1 botol susu")

# Perulangan

