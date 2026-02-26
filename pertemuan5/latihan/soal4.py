gudang_pc = [ 
{"item": "Monitor", "harga": 1500000, "stok": 5}, 
{"item": "Keyboard", "harga": 400000, "stok": 12}, 
{"item": "Mouse", "harga": 250000, "stok": 20} 
] 
#soal 1
for x in gudang_pc:
    if x["item"]== "keyboard":
        x["kategori"] == "aksesoris"
        
print(gudang_pc)

#soal 2
gudang_pc.append({
    "item" : "Headset", "harga": 350000, "stok": 8 
})

#soal 3
for x in gudang_pc:
    print(f"Item: {x["item"]} | Total Aset: Rp {x["harga"] * x["stok"]}")
    
# method dictionary
# clear()
# Menghapus seluruh pasangan key–value dalam dictionary.

# copy()
# Membuat salinan dictionary tanpa memengaruhi dictionary asli.

# fromkeys()
# Membuat dictionary baru dari sekumpulan key dengan nilai yang sama.

# get()
# Mengambil nilai dari key tertentu.
# Tidak menimbulkan error jika key tidak ditemukan.

# items()
# Mengembalikan pasangan key dan value dalam bentuk tuple.

# keys()
# Mengembalikan semua key dalam dictionary.

# values()
# Mengembalikan semua value dalam dictionary.

# pop()
# Menghapus elemen berdasarkan key dan mengembalikan nilainya.

# popitem()
# Menghapus dan mengembalikan pasangan key–value terakhir.

# setdefault()
# Mengambil nilai dari key tertentu, atau menambahkan key dengan nilai default jika belum ada.

# update()
# Memperbarui dictionary dengan pasangan key–value dari dictionary lain atau iterable.