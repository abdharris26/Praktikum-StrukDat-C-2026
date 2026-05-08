class Graph:
    def __init__(self):
        self.nodes = {}

    def tambah_kota(self, nama):
        if nama not in self.nodes:
            self.nodes[nama] = []


    def tambah_jalan(self, u, v, jarak):
        # Pastikan kota sudah terdaftar di graph
        if u not in self.nodes:
            self.tambah_kota(u)
        if v not in self.nodes:
            self.tambah_kota(v)

        self.nodes[u].append((v, jarak))
        self.nodes[v].append((u, jarak))
        print(f"[INPUT] Menambahkan jalan: {u} <=> {v} ({jarak} km) ")

    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi: ")
        for kota in self.nodes:
            tetangga = self.nodes[kota]
            list_tetangga = [f"{t[0]} ({t[1]})" for t in tetangga]
            print(f"{kota} terhubung ke: {', '.join(list_tetangga)} ")

    def dijkstra(self, kota_asal):
        jarak = {kota: float('inf') for kota in self.nodes}
        jarak[kota_asal] = 0
        
        sudah_dikunjungi = set()
        
        print(f"\n[PROSES] Menghitung rute terpendek dari: {kota_asal}...")

        while len(sudah_dikunjungi) < len(self.nodes):
            kota_sekarang = None
            jarak_minimal = float('inf')

            for kota in self.nodes:
                if kota not in sudah_dikunjungi and jarak[kota] < jarak_minimal:
                    jarak_minimal = jarak[kota]
                    kota_sekarang = kota
            if kota_sekarang is None:
                break
            sudah_dikunjungi.add(kota_sekarang)

            for tetangga, bobot_jalan in self.nodes[kota_sekarang]:
                total_jarak_baru = jarak[kota_sekarang] + bobot_jalan
                if total_jarak_baru < jarak[tetangga]:
                    jarak[tetangga] = total_jarak_baru
        return jarak


sistem = Graph()

print("SISTEM NAVIGASI LOGISTIK \"KILAT MAJU\" [cite: 303]")
print("========================================")

# 1. Input Jaringan Sesuai Skenario
sistem.tambah_jalan("Jakarta", "Bandung", 150)
sistem.tambah_jalan("Jakarta", "Cirebon", 200)
sistem.tambah_jalan("Bandung", "Tasikmalaya", 100)
sistem.tambah_jalan("Bandung", "Cirebon", 130)
sistem.tambah_jalan("Cirebon", "Semarang", 250)
sistem.tambah_jalan("Tasikmalaya", "Semarang", 200)

# 2. Visualisasi Struktur Jaringan
sistem.tampilkan_graph()

# 3. Jalankan Optimasi Rute (Dijkstra) dari Jakarta
hasil_rute = sistem.dijkstra("Jakarta")

# 4. Tampilkan Hasil Akhir
print("\n[HASIL] Jarak Terpendek dari Jakarta:")
nomor = 1
for kota in sorted(hasil_rute, key=hasil_rute.get):
    if kota != "Jakarta":
        print(f"{nomor}. Ke {kota}: {hasil_rute[kota]} km")
        nomor += 1

print("\nSimulasi Navigasi Selesai!")