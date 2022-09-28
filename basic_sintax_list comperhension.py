print("\nPerintah del dengan list comperhensive")
list_book = ["Atomic Habbits", "Seven Habbits", "Mindset","harr potter", "How wo to Influence People"]
del list_book[:]
for i in range(0, len(list_book)):
    print(list_book[i])

print("\nPerintah del untuk buku 1 dan 2 dengan comperhensive list")
list_book = ["Atomic Habbits", "Seven Habbits", "Mindset","Harry potter", "How wo to Influence People"]
del list_book[0:2]
for i in range(0, len(list_book)):
    print(list_book[i])

print("\nPerintah del dengan comperhensive list")
list_book = ["Atomic Habbits", "Seven Habbits", "Mindset","Harry potter", "How wo to Influence People"]
del list_book[0::2]
for i in range(0, len(list_book)):
    print(list_book[i])

print("\nMembuat list baru")
list_book = ["Atomic Habbits", "Seven Habbits", "Mindset","Harry potter", "How wo to Influence People"]
list_new_book = list_book[:]
for i in range(0, len(list_book)):
    print(list_book[i])

print("\nMembuat list baru dengan comprehension: Genap")
list_book = ["1. Atomic Habbits", "2. Seven Habbits", "3. Mindset","4. Harry potter", "5. How wo to Influence People"]
list_new_book = list_book[0::2]
for i in range(0, len(list_book)):
    print(list_book[i])

print("\nMembuat list baru dengan comprehension: ganjil")
list_book = ["1. Atomic Habbits", "2. Seven Habbits", "3. Mindset","4. Harry potter", "5. How wo to Influence People"]
list_new_book = list_book[1::2]
for i in range(0, len(list_book)):
    print(list_book[i])

print("\nMembuat list baru dengan comprehension: buat diujung")
list_book = ["1. Atomic Habbits", "2. Seven Habbits", "3. Mindset","4. Harry potter", "5. How wo to Influence People"]
list_new_book = list_book[0:-1]
for i in range(0, len(list_book)):
    print(list_book[i])

print("\nMembuat list baru dengan comprehension: buat diujung dengan cara lain")
list_book = ["1. Atomic Habbits", "2. Seven Habbits", "3. Mindset","4. Harry potter", "5. How wo to Influence People"]
print(list_book[0:-1])
