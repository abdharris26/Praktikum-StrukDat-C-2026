barang = ("boo1", "laptop Gaming", 15000000)

print("harga barang:", barang[2])

#barang[2] = 14000000
#error karena tuple bersifat tidak dapat di ubah setelah dibuat

kode, nama, harga = barang
print(kode, nama, barang)

buah = ("apple", "banana", "cherry")

print(buah)

print(buah[1])

# buah[1] = "mango"   # akan error karena tuple tidak bisa diubah

a, b, c = buah
print(a)
print(b)
print(c)
