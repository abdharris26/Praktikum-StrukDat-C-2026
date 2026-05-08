class HashTablePerpustakaan:
    def __init__(self):
        self.size = 10 
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, kode):
        total_unicode = 0
        for char in str(kode):
            total_unicode += ord(char) 
        return total_unicode % self.size

    def insert(self, kode, judul): 
        index = self.hash_function(kode)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == kode:
                bucket[i] = (kode, judul)
                return

        bucket.append((kode, judul))

    def search(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]

        for k, v in bucket:
            if k == kode:
                return v
        # Jika tidak ditemukan
        return "Buku tidak ditemukan" 

    def delete(self, kode): 
        index = self.hash_function(kode)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == kode:
                del bucket[i]
                return True
        return False

    def display(self): 
        print("\n===== ISI HASH TABLE PERPUSTAKAAN =====")
        for index, bucket in enumerate(self.table):
            print(f"Bucket {index}: {bucket}")
        print("========================================\n")


perpustakaan = HashTablePerpustakaan()


perpustakaan.insert("BK111", "Mahir C++ Dalam Satu Jam")
perpustakaan.insert("BK222", "Python Dasar")
perpustakaan.insert("BK333", "Matematika Diskrit")
perpustakaan.insert("BK444", "Atomic Habits")

perpustakaan.display()

perpustakaan.insert("BK045", "Mein Kampf")
perpustakaan.insert("BK111", "Bumi Manusia")

perpustakaan.display()

print("Cari BK222:", perpustakaan.search("BK222"))
print("Cari BK999:", perpustakaan.search("BK999")) 

perpustakaan.delete("BK333")
perpustakaan.display()