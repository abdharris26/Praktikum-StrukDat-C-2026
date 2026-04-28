class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self, plat):
        new_node = Node(plat)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def tampilkan_maju(self):
        curr = self.head
        while curr:
            print(curr.plat)
            curr = curr.next

    def hapus_kendaraan(self, plat):
        # Mencari node berdasarkan plat 
        curr = self.head
        while curr:
            if curr.plat == plat:
                
                # Kasus Head (paling depan) 
                if curr == self.head:
                    self.head = curr.next
                    if self.head:
                        self.head.prev = None
                
                # Kasus Tail (paling belakang) 
                elif curr == self.tail:
                    self.tail = curr.prev
                    if self.tail:
                        self.tail.next = None
                
                # Kasus Tengah
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                return
            curr = curr.next

parkir = DoubleLinkedList()
parkir.tambah_kendaraan("B 1111 AA") 
parkir.tambah_kendaraan("D 2222 BB") 
parkir.tambah_kendaraan("A 3333 CC") 
parkir.tambah_kendaraan("B 4444 DD") 

print("Sebelum:") 
parkir.tampilkan_maju() 

parkir.hapus_kendaraan("A 3333 CC") 

print("\nSesudah:") 
parkir.tampilkan_maju() 