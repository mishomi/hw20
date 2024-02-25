class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def printLeafNodes(self, node):
        if node is None:
            return
        elif node.left is None and node.right is None:
            print(node.value)
        else:
            self.printLeafNodes(node.left)
            self.printLeafNodes(node.right)

    def countEdges(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 0
        else:
            return 1 + self.countEdges(node.left) + self.countEdges(node.right)



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Leaf nodes:")
tree.printLeafNodes(tree.root)

print("Number of edges:", tree.countEdges(tree.root))
