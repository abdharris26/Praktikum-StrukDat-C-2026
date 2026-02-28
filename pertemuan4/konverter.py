# berisi fungsi konversi

def konversi(jumlah, dari, ke, kurs):
    jumlah_idr = jumlah * kurs[dari]
    hasil = jumlah_idr /kurs[ke]
    return hasil