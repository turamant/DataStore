class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find_value(self, value):
        if value < self.data:
            if self.left is None:
                return str(value) + " not found"
            return self.left.find_value(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " not found"
            return self.right.find_value(value)
        else:
            return str(value) + " is found"

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

node = Node(5)
node.insert(8)
node.insert(14)
node.insert(3)
res = node.find_value(3)
print(res)
node.print_tree()
