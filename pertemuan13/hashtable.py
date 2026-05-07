class ManualHashTable:
    def __init__(self, ukuran_table=5):
        self.ukuran = ukuran_table
        # Membuat array kosong dengan ukuran tetap berisi list kosong [] untuk Chaining
        # Struktur di dalam: [ [], [], [], [], [] ]
        self.table = [[] for _ in range(self.ukuran)]

    def _fungsi_hash(self, key):
        """Mengubah string key menjadi indeks angka berdasarkan ukuran table."""
        # hash() adalah fungsi bawaan Python untuk mengubah objek menjadi angka unik
        return abs(hash(key)) % self.ukuran

    def insert_atau_update(self, key, value):
        """Fungsi untuk memasukkan data baru atau memperbarui (update) data jika key sudah ada."""
        indeks = self._fungsi_hash(key)
        bucket = self.table[indeks]  # Mengambil list (rantai/chain) pada indeks tersebut

        # Gunakan ENUMERATE untuk mencari tahu apakah key sudah pernah terdaftar di bucket ini
        # i = nomor urut/indeks di dalam list kecil, (k, v) = pasangan key & value lama
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # [PROSES UPDATE] Jika key ditemukan, perbarui nilainya
                bucket[i] = (key, value)
                print(f"🔄 [UPDATE] Key '{key}' diperbarui menjadi '{value}' di indeks [{indeks}] slot ke-{i}")
                return

        # [PROSES INSERT] Jika perulangan selesai dan key TIDAK ditemukan, tambahkan data baru
        bucket.append((key, value))
        print(f"📥 [INSERT] Key '{key}' berhasil dimasukkan ke indeks [{indeks}]")

    def cari_data(self, key):
        """Mencari data berdasarkan key di dalam table."""
        indeks = self._fungsi_hash(key)
        bucket = self.table[indeks]

        # Menggunakan enumerate untuk mencari kecocokan key di dalam bucket/chain
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return f"🔍 [KETEMU] Key '{key}' bernilai '{v}' (Ditemukan di indeks [{indeks}] posisi ke-{i})"
        
        return f"❌ [TIDAK KETEMU] Key '{key}' tidak ada di dalam table."

    def tampilkan_table(self):
        """Menampilkan struktur visual dari internal Hash Table kita."""
        print("\n=== STRUKTUR INTERNAL HASH TABLE (CHAINING) ===")
        # Enumerate digunakan di sini untuk menampilkan nomor indeks luar dari tabel memori
        for indeks, bucket in enumerate(self.table):
            print(f"Indeks [{indeks}]: {bucket}")
        print("===============================================\n")


# ==========================================
# UJI COBA PROGRAM
# ==========================================

# Kita buat ukuran tabel sengaja kecil (hanya 5 slot) agar memicu tabrakan (Collision)
hash_ku = ManualHashTable(ukuran_table=5)

print("--- 1. PROSES INSERT DATA ---")
hash_ku.insert_atau_update("Alice", "0812-AAA")
hash_ku.insert_atau_update("Budi", "0821-BBB")
hash_ku.insert_atau_update("Charlie", "0853-CCC")  # Kemungkinan masuk ke indeks yang sama dengan yang lain

# Menampilkan kondisi tabel setelah di-insert
hash_ku.tampilkan_table()

print("--- 2. PROSES UPDATE DATA ---")
# Menggunakan key yang sama ("Budi"), otomatis mendeteksi update lewat fungsi enumerate
hash_ku.insert_atau_update("Budi", "0899-NOMOR-BARU")

# Menampilkan kondisi tabel setelah di-update
hash_ku.tampilkan_table()

print("--- 3. PROSES PENCARIAN DATA ---")
print(hash_ku.cari_data("Budi"))
print(hash_ku.cari_data("Siti"))