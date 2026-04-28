class StackClass:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


# OUTPUT
stack = StackClass()

stack.push("google.com")
stack.push("youtube.com")
stack.push("github.com")

print("=== Stack Class ===")
print("Top:", stack.peek())
print("Pop:", stack.pop())
print("Top:", stack.peek())
print("Size:", stack.size())
print()