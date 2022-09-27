"""
program perulangan dengan while sampai paham (Undefined count)
"""
book_count = 10
print(f"Jumlah buku yang inin dibaca adalah {book_count} buku")

read_count = 0
print(f"Jumlah buku yang sudah dibaca sebanyak {read_count} buku\n")

understood_count = 0

while understood_count < book_count * 2:
    understood_count = understood_count + 1
    if read_count == 9:
        print(f"buku ke {read_count + 1} Belum paham")
    else:
        read_count = read_count + 1
        print(f"jumlah buku ke {read_count} sudah dibaca dan dipahami")

print("jumlah buku yang sudah dibaca", read_count)

if read_count == book_count:
    print("semua buku budi telah baca dan pahami")
else:
    print(f"maaf bu tidak semua buku bisa dipahami, budi hanya bisa memahami {read_count} buku")

