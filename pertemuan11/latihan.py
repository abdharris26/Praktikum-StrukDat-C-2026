class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None 
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        self.total_antrean = 0
        
    def enqueue(self, nama, keluhan):
        self.total_antrean += 1
        new_node = Node(nama, keluhan)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1
        print(f"[DAFTAR] {nama.capitalize()} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.total_antrean})")
        
    def dequeue(self):
        if self.isEmpty():
            return None
        temp = self.front 
        self.front = temp.next
        self.length -= 1
        self.total_antrean -= 1
        if self.front is None:
            self.rear = None
        return temp
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.front
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def clear(self):
        self.front = None
        self.rear = None
        self.length = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")
    
    def printQueue(self):
        print("[ANTRIAN SAAT INI]")
        temp = self.front
        i = 1
        while temp:
            print(f"{i}. {temp.nama.upper()} → {temp.keluhan}")
            temp = temp.next
            i += 1

print("========================================")
print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("========================================\n")

myQueue = Queue()

print(f"[CEK] Apakah antrian kosong? → {'YA, antrian masih kosong.' if myQueue.isEmpty() else 'Tidak'}")

myQueue.enqueue("Budi", "demam tinggi")
myQueue.enqueue("Ani", "batuk pilek")
myQueue.enqueue("Citra", "sakit kepala")

print(f"[INFO] Jumlah pasien menunggu: {myQueue.size()} orang")
p = myQueue.peek()
print(f"[PEEK] Pasien berikutnya: {p.nama.upper()} — {p.keluhan}")
out = myQueue.dequeue()
print(f"[PANGGIL] Dokter memanggil: {out.nama.upper()} (keluhan: {out.keluhan})")
myQueue.enqueue("Dodi", "nyeri perut")
myQueue.printQueue()
out = myQueue.dequeue()
print(f"[PANGGIL] Dokter memanggil: {out.nama.upper()} (keluhan: {out.keluhan})")
print(f"[INFO] Jumlah pasien masih menunggu: {myQueue.size()} orang")
myQueue.clear()
print(f"[CEK] Apakah antrian kosong? → {'YA, antrian sudah kosong.' if myQueue.isEmpty() else 'Tidak'}")
print("\n========================================")
print("Simulasi Selesai!")
print("========================================")