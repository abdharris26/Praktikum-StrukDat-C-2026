skema_komisi = (
    (100000000, 10),
    (50000000, 5),
    (20000000, 2),
    (0, 0)
)

def hitung_komisi(total_penjualan, skema, index=0):
    if total_penjualan >= skema[index][0]:
        return skema[index][1]
    return hitung_komisi(total_penjualan, skema, index + 1)

# Program Utama
nama = input("Nama Sales: ")
total = float(input("Total Penjualan: "))
persen = hitung_komisi(total, skema_komisi)
nominal = total * persen / 100

print(f"Sales: {nama}, Komisi: {persen}%, Nominal: {nominal}")