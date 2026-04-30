stok_gadget = [
    {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},
    {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},
    {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}
]

def filter_harga(data, min_harga, max_harga):
    return [g for g in data if min_harga <= g['harga'] <= max_harga]

# Program Utama
bawah = float(input("Batas bawah harga: "))
atas = float(input("Batas atas harga: "))
hasil = filter_harga(stok_gadget, bawah, atas)

if not hasil:
    print("Tidak ada gadget dalam rentang harga tersebut.")
else:
    for g in hasil:
        print(g)