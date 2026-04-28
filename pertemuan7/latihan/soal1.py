
def pisahkan_plat(plat_list):
    ganjil = []
    genap = []

    for plat in plat_list:
        for huruf in reversed(plat):
            if huruf.isdigit():
                angka = int(huruf)

                if angka % 2 == 0:
                    genap.append(plat)
                else:
                    ganjil.append(plat)
                break


    print("Plat Ganjil:")
    for p in ganjil:
        print(p)

    print("\nPlat Genap:")
    for p in genap:
        print(p)

data_plat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
pisahkan_plat(data_plat)
