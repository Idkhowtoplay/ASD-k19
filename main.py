class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
    
    def nigga(self):
        self.name += "lele"

nama = Node("Kirakira")
print(nama.name)
nama.nigga()
print(nama.name)