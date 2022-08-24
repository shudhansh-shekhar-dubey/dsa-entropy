from bst.minmax import Node

tree = Node()

tree.insert(8)
tree.insert(10)
tree.insert(12)
tree.insert(7)
tree.insert(5)
tree.insert(3)
tree.insert(11)
tree.insert(6)

#print(tree.search(11))

#tree.traverse_in()
#tree.traverse_pre()
#tree.traverse_post()

#print(tree.height())
#print(tree.min())
#print(tree.max())
#print(tree.is_bst())
#print(tree.node_count())

badtree = Node()
badtree.data = 5
badtree.left = Node(1)
badtree.right = Node(8)
badtree.right.left = Node(9)
badtree.right.right = Node(12)
#print(badtree.is_bst())

badtree = Node()
badtree.data = 10
badtree.left = Node(5)
badtree.right = Node(16)
badtree.left.left = Node(4)
badtree.left.left.right = Node(6)
badtree.left.left.right.right = Node(7)
badtree.left.right = Node(7)
badtree.left.right.right = Node(11)
badtree.left.left.left = Node(1)
badtree.right = Node(16)
badtree.right.right = Node(25)
badtree.right.right.left = Node(13)
badtree.right.left = Node(9)
#print(badtree.is_bst())
#print(badtree.height())
