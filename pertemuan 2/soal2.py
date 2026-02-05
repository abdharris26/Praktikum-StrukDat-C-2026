
barang = ("boo1", "laptop Gaming", 15000000)

#1. akses dan tampilkan harga barang
print("harga barang:", barang[2])

#2. mencoba mengubah harga barang
#barang[2] = 14000000
#error karena tuple bersifat tidak dapat di ubah setelah dibuat

#3. unpaching tuple
kode, nama, harga = barang
print(kode, nama, barang)

