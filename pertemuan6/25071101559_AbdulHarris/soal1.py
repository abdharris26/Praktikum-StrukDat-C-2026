def registrasi_gadget(merk, tipe, harga, sn):
    if harga <= 1000000:
        print("Error: Harga harus di atas 1.000.000")
        return None
    if len(sn) < 5:
        print("Error: Serial Number minimal 5 karakter")
        return None
    
    return {'merk': merk, 'tipe': tipe, 'harga': harga, 'sn': sn, 'status': 'Tersedia'}

# Program Utama
inventaris = []
for i in range(3):
    print(f"\nInput Gadget ke-{i+1}:")
    m = input("Merk: ")
    t = input("Tipe: ")
    h = float(input("Harga: "))
    s = input("Serial Number: ")
    hasil = registrasi_gadget(m, t, h, s)
    if hasil:
        inventaris.append(hasil)

print("\nInventaris Gadget:", inventaris)