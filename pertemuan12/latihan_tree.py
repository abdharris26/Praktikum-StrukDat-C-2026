class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert_manual(self):
        self.root = Node("A")
        self.root.left= Node("B")
        self.root.right = Node("C" )
        self.root.left.left = Node("D")
        self.root.left.right = Node("E")
        self.root.right.right = Node("F")   
        
    def traverse_preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)
            
    def traverse_inorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            print(node.data, end=" ")
            self.traverse_inorder(node.right)
            
    def traverse_postorder(self, node):
        if node is not None:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.data, end=" ")
            
    def get_leaf_nodes(self, node, leaf_list):
        if node:
            if node.left and not node.right:
                leaf_list.append(node.data)
            self.get_leaf_nodes(node.left, leaf_list)
            self.get_leaf_nodes(node.right, leaf_list)

print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print("[INFO] Membangun Struktur Gudang...")

tree = BinaryTree()
tree.insert_manual()

print("[INFO] Struktur berhasil dibuat.")
print("====")

print("HASIL AUDIT:")

print("1. Pre-Order  :", end=" ")
tree.traverse_preorder(tree.root)
print()

print("2. In-Order   :", end=" ")
tree.traverse_inorder(tree.root)
print()

print("3. Post-Order :", end=" ")
tree.traverse_postorder(tree.root)
print()

leaf_nodes = []
tree.get_leaf_nodes(tree.root, leaf_nodes)
print(f"[DATA] Gudang Ujung (Leaf Nodes): {', '.join(leaf_nodes)}")

print("====")
print("Audit Selesai!")

