"""

Binary Tree
Depth First Search Tree

Node: parent, left, right, self
Tree: sequences of nodes

Inorder: Order: ( LEFT -> ROOT -> RIGHT ) 

"""
class Node:
    def __init__(self, data, left = None, right = None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

class Tree:
    def __init__(self, node: Node):
        self.root = node

    def traversal(self):
        node = self.root
        self._inorder(node)

    def _inorder(self, node: Node):
        if node is not None:
            self._inorder(node.left)
            print(node.data)
            self._inorder(node.right)