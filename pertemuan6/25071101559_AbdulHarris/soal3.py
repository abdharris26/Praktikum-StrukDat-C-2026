katalog = [
    {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 2},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5}
]

def update_stok(katalog, sn_target, jumlah_tambah):
    for item in katalog:
        if item['sn'] == sn_target:
            item['stok'] = item.get('stok', 0) + jumlah_tambah
            return True
    return False

# Program Utama
daftar_merk = {item['merk'] for item in katalog}

for _ in range(3):
    sn = input("Masukkan SN untuk update stok: ")
    jml = int(input("Jumlah penambahan: "))
    update_stok(katalog, sn, jml)

print("Daftar Merk Unik:", daftar_merk)