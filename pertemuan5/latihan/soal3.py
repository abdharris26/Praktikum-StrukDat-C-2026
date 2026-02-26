ukm_coding = {"Andi", "Budi", "Caca", "Deni"}  
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"} 
#soal 1
ukm_coding_saja = ukm_coding - ukm_robotik
print(ukm_coding_saja)

#soal 2
mahasiswa_unik = ukm_coding | ukm_robotik
print(mahasiswa_unik)

#soal 3
print("Andi" in ukm_robotik)

# method set
# add()
# Menambahkan satu elemen ke dalam set.

# update()
# Menambahkan beberapa elemen dari iterable lain (list, tuple, set) ke dalam set.

# remove()
# Menghapus elemen tertentu dari set.
# ⚠️ Error jika elemen tidak ada.

# discard()
# Menghapus elemen tertentu dari set tanpa menimbulkan error jika elemen tidak ada.

# pop()
# Menghapus dan mengembalikan elemen secara acak dari set.

# clear()
# Menghapus seluruh elemen dalam set sehingga set menjadi kosong.

# copy()
# Membuat salinan set tanpa memengaruhi set asli.

# union()
# Menggabungkan dua set dan mengembalikan set baru.

# intersection()
# Mengembalikan elemen yang sama dari dua set.

# difference()
# Mengembalikan elemen yang ada di set pertama tetapi tidak ada di set kedua.

# symmetric_difference()