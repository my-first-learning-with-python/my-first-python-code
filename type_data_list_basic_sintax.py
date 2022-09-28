list_book = ["Atomic Habbits", "Seven Habbits", "Mindset"]
print('tampilkan variable data buku')
print(list_book)

print('\nproses semua dengan for')
for book in list_book:
    print(book)

print('\nproses semua dengan for')
print(list_book[0])
print(list_book[2])

print("\ntampilkan dgn for in range")
for i in range(0, len(list_book)):
    print(list_book[i])

print("\nTampilkan dgn for in rane, dimana datanya berbeda2")
list_book = [1, 'mariposa', -3.23, 3.14]
for i in range(0, len(list_book)):
    print(list_book[i])

print("\nkembalikan nilai awal list_book")
list_book = ["Atomic Habbits", "Seven Habbits", "Mindset"]
print("\ntambahkan 1 buku baru")
list_book.append("fifty sade of the grey")
for i in range(0, len(list_book)):
    print(list_book[i])

print('\nclear list')
list_book.clear()
for i in range(0, len(list_book)):
    print(list_book[i])

print("\nMengganti element pertama")
list_book = ["Atomic Habbits", "Seven Habbits", "Mindset"]
list_book[0] = "fifty sade of the grey"
for i in range(0, len(list_book)):
    print(list_book[i])

print("\nMengambil element ke-2")
book = list_book.pop(1)
for i in range(0, len(list_book)):
    print(list_book[i])

print("\nBuku yang diambil buku")
print(book)

print("\npop")
list_book.pop()
for i in range(0, len(list_book)):
    print(list_book[i])

print("\npop -1")
list_book = ["Atomic Habbits", "Seven Habbits", "Mindset"]
list_book.pop(-1)
for i in range(0, len(list_book)):
    print(list_book[i])

print("\npop -2")
list_book = ["Atomic Habbits", "Seven Habbits", "Mindset"]
list_book.pop(-2)
for i in range(0, len(list_book)):
    print(list_book[i])