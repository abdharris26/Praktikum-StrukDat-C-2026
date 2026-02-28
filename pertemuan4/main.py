from tabulate import tabulate
from kurs import kurs
from konverter import konversi

print("=== KONVERTER MATA UANG ===")

tabel = []
for k, v, in kurs.items():
    tabel.append([k, f"{v:,}".replace(",",".")])
    
print(tabulate(tabel, headers=["kode", "kurs"], tablefmt="grid"))

dari = input("dari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("ke (IDR/USD/EUR/SGD/JYP): ").upper()
jumlah = float(input("jumlah:"))

hasil = konversi(jumlah, dari, ke, kurs)

print(f"\nHasil: {jumlah:,.0f}{dari} = {hasil:.2f} {ke}")
