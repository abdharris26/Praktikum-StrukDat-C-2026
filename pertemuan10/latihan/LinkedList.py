class Node:
    def  __init__(self, url):
        self.url = url
        self.next = None
        
class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0
        
    def is_empty(self):
        return self.top is None
    
    def push(self,url):
        new_node = Node(url)
        new_node.next = self.top
        self.top = new_node
        self.count +=1
        
    def pop(self):
        if self.is_empty():
            return "riwayat kosong"
        temp = self.top
        self.top = self.top.next
        self.count -= 1
        return temp.url
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.url

    def size(self):
        return self.count



stack = StackLinkedList()

stack.push("google.com")
stack.push("youtube.com")
stack.push("github.com")

print("=== Stack Linked List ===")
print("Top:", stack.peek())
print("Pop:", stack.pop())
print("Top:", stack.peek())
print("Size:", stack.size())
print()
        
        
        
        
        