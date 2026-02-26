data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)] 

for x in data_aktivitas:
    if x[1] > 80:
        print(x[0], "mendapatkan predikat gold")
    elif x[1] < 80 and x[1] > 50:
        print(x[0],"mendapatkan predikat silver")
    else:
        print(x[0],"mendapatkan bronze")
 
# method tuple
# count()
# Menghitung jumlah kemunculan suatu elemen tertentu di dalam tuple.

# index()
# Mengembalikan posisi (indeks) dari elemen tertentu yang pertama kali ditemukan dalam tuple.

# len()
# Menghitung jumlah elemen yang terdapat di dalam tuple.

# max()
# Mengembalikan nilai terbesar dari elemen-elemen dalam tuple.

# min()
# Mengembalikan nilai terkecil dari elemen-elemen dalam tuple.

# sum()
# Menjumlahkan seluruh elemen numerik di dalam tuple.

# sorted()
# Mengurutkan elemen tuple dan menghasilkan list baru (tuple asli tidak berubah).

# tuple()
# Mengubah iterable (misalnya list) menjadi tuple.