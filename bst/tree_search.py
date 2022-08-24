class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:  # Root is null, so returned node will be based on key
        return Node(key)
    else:
        if root.val == key:  # Root value is equal to the search key
            return root
        elif root.val < key:  # Root value is less than search key
            root.right = insert(root.right, key)
        else:  # Root value is greater than search key
            root.left = insert(root.left, key)
    return root


def tree_search(root, key):
    if root is None or key == root.val:
        return root
    if key < root.val:
        return tree_search(root.left, key)
    else: 
        return tree_search(root.right, key)


