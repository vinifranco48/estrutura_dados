class Node:
    def __init__(self, data):
        self.data =data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data):
        node = Node(data)
        self.root = node
    
    def simetric_transversal(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end = "")
            self.simetric_transversal(node.left)
        print(node, end='')

        if node.right:
            self.simetric_transversal(node.right)
            print(')', end = "")

if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.root.left = Node(20)
    tree.root.right = Node(30)


    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)
