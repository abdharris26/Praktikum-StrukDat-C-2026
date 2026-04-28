class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def sisipkan_vip(head, plat_baru, plat_target):
    if plat_target.next == None:
        plat_target.next = plat_baru
        return head
    
    plat_baru.next = plat_target.next
    plat_target.next = plat_baru
    return head

node1 = Node("mobil1")
node2 = Node("mobil2")
node3 = Node("mobil3")
node4 = Node("mobil4")
node5 = Node("mobil5")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node6 = Node("mobil6")

node1 = sisipkan_vip(node1,node6,node2)
traverseAndPrint(node1)
