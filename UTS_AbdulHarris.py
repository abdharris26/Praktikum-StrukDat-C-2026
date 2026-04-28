print("*soal nomor 1*")

pengunjung_hari_ini = [ 
{"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi", "kembali": False}, 
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True}, 
{"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi", "kembali": False}, 
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True}, 
{"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains", "kembali": False}, 
{"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum", "kembali": False}, 
] 
 
def tampilkan_pengunjung():
    print("\n==== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("NO | ID  | Nama | Usia | Kategori | Status Kembali")
    print("---+-----+------+------+---------+-------------")
    
    no = 1
    for p in pengunjung_hari_ini:
        status = "Sudah Kembali" if p["kembali"] else "Belum Kembali"
        print(no, "|" ,p["id"] , "|",p["nama"], "|", p["usia"], "|", p["kategori"], "|", status)
        no = +1
                  
def filter_belum_kembali():
    belum = []
    
    for p in pengunjung_hari_ini :
        if p["kembali"] == False:
            belum.append(p["nama"])
    
    belum.sort()
    
    print("\n ===== PENGUNJUNG BELUM KEMBALI =====")
    no = 1
    for nama in belum:
        print(no, ".", nama)
        no += 1
    
    print("\n Total belum kembali: ", len(belum),"pengunjung")
    
tampilkan_pengunjung()
filter_belum_kembali()

print("\n*soal nomor 2*")

def info_perpustakaan():
    perpustakaan = (
        "Perpustakaan Kampus Terpadu",
        "Jl. Pendidikan No. 5, pekanbaru",
        "0761-54321"
    )
    
    print("\ninfo perpustakaan")
    print("Nama   :", perpustakaan[0])
    print("Alamat :", perpustakaan[1])
    print("Telp   :", perpustakaan[2])
    
def rekap_kategori():
    buku_set = set(p["kategori"] for p in pengunjung_hari_ini)
    
    print("\nkategori Buku unik: ",buku_set)
    print("jumlah kategori",len(buku_set))
    
    rekap = {}
    for p in pengunjung_hari_ini:
        pengunjung = p["kategori"]
        rekap[pengunjung] = rekap.get(pengunjung, 0) + 1
        
    print("\nRekap per kategori")
    for k, v in rekap.items():
        print(k,":", v ,pengunjung)
        
    max_jumlah = max(rekap.values())
    terbanyak = [k for k, v in rekap.items() if v == max_jumlah]
    
    print("\nKategori terbanyak:", ",".join(terbanyak), f"({max_jumlah} pengunjung)")

info_perpustakaan()
rekap_kategori()   

print("\n*soal nomor 3*")

class Pengunjung:
    total_pengunjung = 0  # Class variable counter
    
    def __init__(self, id_pengunjung, nama, kategori):
        # Atribut private
        self.__id = id_pengunjung
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.total_pengunjung += 1
        
    # Getters
    def get_id(self):
        return self.__id
        
    def get_nama(self):
        return self.__nama
        
    def get_kategori(self):
        return self.__kategori
        
    def tampilkan_info(self):
        print(f"ID       : {self.__id}")
        print(f"Nama     : {self.__nama}")
        print(f"Kategori : {self.__kategori}")
        
    @staticmethod
    def hitung_pengunjung():
        return Pengunjung.total_pengunjung

class PengunjungPrioritas(Pengunjung):
    def __init__(self, id_pengunjung, nama, kategori, prioritas):
        # Memanggil konstruktor parent class
        super().__init__(id_pengunjung, nama, kategori)
        self.prioritas = prioritas
        
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Prioritas: {self.prioritas}")
        if self.prioritas == "Mendesak":
            print("** Layani segera! **")
        print()


p1 = Pengunjung("M001", "Rina", "Fiksi")
p1.tampilkan_info()
print()
p2 = PengunjungPrioritas("M007", "Gilang", "Referensi", "Mendesak")
p2.tampilkan_info()
print(f"Total pengunjung terdaftar: {Pengunjung.hitung_pengunjung()}\n")


print("\n*soal nomor 4*")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntrianPeminjaman:
    def __init__(self):
        self.head = None
        
    def tambah(self, data):
        """Menambah pengunjung di akhir antrian."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def hitung(self):
        """Mengembalikan jumlah pengunjung dalam antrian."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
        
    def tampilkan(self):
        """Menampilkan seluruh antrian beserta posisinya."""
        print("=== ANTRIAN PEMINJAMAN ===")
        current = self.head
        posisi = 1
        while current:
            d = current.data
            print(f"[{posisi}] {d['id']} | {d['nama']} | {d['kategori']}")
            current = current.next
            posisi += 1
        print(f"Total antrian: {self.hitung()}\n")
        
    def panggil_berikutnya(self):
        """Menghapus dan menampilkan pengunjung paling depan (FIFO)."""
        print("Memanggil pengunjung berikutnya...")
        if not self.head:
            print("Antrian kosong!\n")
            return
            
        dipanggil = self.head
        self.head = self.head.next
        print(f"Silakan masuk: {dipanggil.data['nama']} ({dipanggil.data['id']})\n")
        
    def cari(self, nama):
        """Mencari pengunjung berdasarkan nama dan menampilkan posisinya."""
        print(f"Mencari '{nama}'...")
        current = self.head
        posisi = 1
        while current:
            if current.data['nama'] == nama:
                d = current.data
                print(f"Ditemukan: {d['id']} | {d['nama']} | {d['kategori']} (posisi ke-{posisi})\n")
                return
            current = current.next
            posisi += 1
        print(f"Pengunjung bernama '{nama}' tidak ditemukan dalam antrian.\n")
        
    def hapus_berdasarkan_id(self, id_hapus):
        """Menghapus pengunjung berdasarkan ID dari mana saja posisinya."""
        print(f"Menghapus pengunjung dengan ID {id_hapus}...")
        
        # Jika antrian kosong
        if not self.head:
            print("Gagal: Antrian kosong.\n")
            return
            
        # Kasus 1: Node yang dihapus ada di posisi pertama (head)
        if self.head.data['id'] == id_hapus:
            hapus = self.head
            self.head = self.head.next
            print(f"{hapus.data['nama']} ({hapus.data['id']}) berhasil dihapus dari antrian.\n")
            return
            
        # Kasus 2: Node yang dihapus ada di tengah atau akhir
        current = self.head
        while current.next:
            if current.next.data['id'] == id_hapus:
                hapus = current.next
                current.next = current.next.next
                print(f"{hapus.data['nama']} ({hapus.data['id']}) berhasil dihapus dari antrian.\n")
                return
            current = current.next
            
        # Kasus 3: ID tidak ditemukan
        print(f"Gagal: ID {id_hapus} tidak ditemukan dalam antrian.\n")


antrian = AntrianPeminjaman()
antrian.tambah({"id": "M001", "nama": "Rina", "kategori": "Fiksi"})    
antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"})
antrian.tambah({"id": "M003", "nama": "Siti", "kategori": "Fiksi"})
antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"})
    
antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.hapus_berdasarkan_id("M003")
antrian.tampilkan()
antrian.cari("Taufik")


    
    
        
    
    
    
    
    
    
    
    
    
    
    
    

