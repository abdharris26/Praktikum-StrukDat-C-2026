nilai_siswa = {
    "S01": {"nama": "Dina", "tugas": 80, "uts": 75, "uas": 85},
    "S02": {"nama": "Abdul Harris", "tugas": 90, "uts": 88, "uas": 92},
    "S03": {"nama": "Sheila", "tugas": 70, "uts": 65, "uas": 70}
}

# 1. Tambahkan data siswa baru
nilai_siswa["S04"] = {"nama": "Fafa", "tugas": 85, "uts": 80, "uas": 90}

# 2. Hitung nilai akhir setiap siswa
print("Nilai Akhir Siswa:")
for x in nilai_siswa.values():
    nilai_akhir = (x["tugas"] * 0.2 + x["uts"] * 0.3 + x["uas"] * 0.5 )
    print(x["nama"], ":", nilai_akhir)

# 3. Tampilkan siswa dengan nilai UAS di atas 80
print("\nSiswa dengan nilai UAS di atas 80:")
for x in nilai_siswa.values():
    if x["uas"] > 80:
        print(x["nama"])
