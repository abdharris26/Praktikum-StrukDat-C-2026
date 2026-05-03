class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None
        
        
class BinarySearchTree:
    def __init__ (self):
        self.root = None
        
    def insert(self, id_buku, judul):
        if self.root is None:
            self.root = Node(id_buku, judul)
            print(f"[INSERT] berhasil memasukkan : ID {id_buku}")
        else:
            self._insert_recursive(self.root, id_buku, judul)
    
    def _insert_recursive(self, current, id_buku, judul):
        if id_buku < current.id_buku:
            if current.left is None:
                current.left = Node(id_buku, judul)
                print(f"[INSERT] berhasil memasukkan: ID {id_buku}")
            else:
                self._insert_recursive(current.left, id_buku, judul)
        elif id_buku > current.id_buku:
            if current.right is None:
                current.right = Node(id_buku, judul)
                print(f"[INSERT] berhasil memasukkan: ID {id_buku}")
            else:
                self._insert_recursive(current.right, id_buku, judul)
                
    def search(self, id_buku):
        return self._search_recursive(self.root, id_buku)
    
    def _search_recursive(self, current, id_buku):
        if current is None or current.id_buku == id_buku:
            return current
        if id_buku < current.id_buku:
            return self._search_recursive(current.left, id_buku)    
        return self._search_recursive(current.right, id_buku)
    
    def traversal_inorder(self):
        print("\n[INFO] Koleksi Buku (In-Order Traversal):")
        self._count = 1
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current):
        if current:
            self._inorder_recursive(current.left)
            print(f"{self._count}. {current.id_buku} - {current.judul}")
            self._count += 1
            self._inorder_recursive(current.right)

    def get_min(self):
        current = self.root
        while current and current.left:
            current = current.left
        return current.id_buku if current else None

    def get_max(self):
        current = self.root
        while current and current.right:
            current = current.right
        return current.id_buku if current else None

    def height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if node is None:
            return -1
        left_h = self._get_height(node.left)
        right_h = self._get_height(node.right)
        return max(left_h, right_h) + 1


katalog = BinarySearchTree()

print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print("=====")

katalog.insert(50, "Dasar Pemrograman")
katalog.insert(30, "Struktur Data")
katalog.insert(70, "Kecerdasan Buatan")
katalog.insert(20, "Matematika Diskrit")
katalog.insert(40, "Basis Data")
katalog.insert(60, "Jaringan Komputer")
katalog.insert(80, "Sistem Operasi")

katalog.traversal_inorder()

print("\n[SEARCH] Mencari ID 60...")
hasil = katalog.search(60)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

print("[SEARCH] Mencari ID 100...")
hasil = katalog.search(100)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

print(f"\n[STATISTIK] ID Terkecil: {katalog.get_min()}")
print(f"[STATISTIK] ID Terbesar: {katalog.get_max()}")

print(f"[INFO] Tinggi (Height) Tree: {katalog.height()}")

print("=====")
print("Simulasi Selesai!")
print("=====")
        
        
        