#latihan praktikum 5
stok_barang = [15, 40, 30,10,25]

#soal 1
stok = stok_barang.index(10)
stok_barang[stok]= 50
print(stok_barang)

#soal 2
stok_barang.append(5)
stok_barang.sort(reverse=True)
print(stok_barang)

#soal 3
print (sum(stok_barang))

#soal 4
print("stok aman") if sum(stok_barang)/len(stok_barang) >= 20 else print("stok tidak aman")

# method utama list
# append() 
# Menambahkan satu elemen ke akhir list.

# insert()
# Menyisipkan elemen ke posisi tertentu dalam list.

# extend()
# Menambahkan seluruh elemen dari list lain ke dalam list.

# remove()
# Menghapus elemen berdasarkan nilai yang pertama ditemukan.

# pop()
# Menghapus dan mengembalikan elemen pada indeks tertentu (default: indeks terakhir).

# clear()
# Menghapus seluruh elemen dalam list sehingga list menjadi kosong.

# index()
# Mengembalikan indeks dari elemen tertentu dalam list.

# count()
# Menghitung jumlah kemunculan suatu elemen dalam list.

# sort()
# Mengurutkan elemen list secara menaik atau menurun.

# sort(reverse=True)
# mengurutkan dalam urutan menurun atau terbesar ke terkecil

# reverse()
# Membalik urutan elemen dalam list.

# copy()
# Membuat salinan list tanpa memengaruhi list asli.

# len()
# menghitung jumlah elemen

# sum()
# menjumlahkan elemen (jika numerik)

# max()/ min()
# menemukan nilai terbesar atau terkecil
    



