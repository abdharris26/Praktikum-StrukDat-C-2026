#pertemuan 9 belajar double dan circular linked list

# Menghapus node berdasarkan data
class CircularLinkedList:
    def delete(self, data):
        if self.head is None:
            return

        current = self.head
        prev = None

        while True:
            # Jika node ditemukan
            if current.data == data:

                # Jika hanya ada 1 node
                if current == self.head and current.next == self.head:
                    self.head = None

                # Jika menghapus head
                elif current == self.head:
                    last = self.head

                    # Cari node terakhir
                    while last.next != self.head:
                        last = last.next

                    # Head pindah ke node berikutnya
                    self.head = self.head.next

                    # Node terakhir menunjuk ke head baru
                    last.next = self.head

                # Jika menghapus node biasa / terakhir
                else:
                  # 10 (prev) -> 20 (current) -> 30 (current.next)
                    prev.next = current.next

                return

            # Geser ke node berikutnya (prev = None, current = 10) -> (prev = 10, current = 20) -> (prev = 20, current = 30)
            prev = current
            current = current.next

            # Jika sudah kembali ke head, berarti data tidak ada
            if current == self.head:
                break