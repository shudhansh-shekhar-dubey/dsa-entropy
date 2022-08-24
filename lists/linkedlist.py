class Node:
    def __init__(self, data: int, next):
        self.data = data
        self.next = next


class List:
    def __init__(self, firstNode: Node):
        self.firstNode = firstNode

    def insertAfter(self, node: Node, newNode: Node):
        newNode.next = node.next  # assign next node of previous node ot new node
        node.next = newNode

    def insertAtStart(self, newNode: Node):
        newNode.next = self.firstNode
        self.firstNode = newNode

    def insertAtEnd(self, newNode: Node):
        node = self.firstNode
        while node.next is not None:
            node = node.next
        node.next = newNode

    def deleteAfter(self, node: Node):
        next = node.next
        furtherNext = next.next
        node.next = furtherNext

    def deleteFromStart(self):
        firstNode = self.firstNode
        secondNode = firstNode.next
        self.firstNode = secondNode

    def deleteFromEnd(self):
        node = self.firstNode
        while node.next is not None and node.next.next is not None:
            node = node.next
        node.next = None

    def search(self, key: int):
        node = self.firstNode
        while node is not None:
          if node.data == key:
            return True
          node = node.next
        return False

    def find_value_at(self, n):
      i = 0
      node = self.firstNode
      while node is not None:
        if i == n:
          return node.data
        node = node.next
        i = i+1
      return None

    def reverse(self): 
      node = self.firstNode  
      temp = Node(node.data, None)
      self.firstNode = temp
      while node.next is not None: 
        node = node.next
        temp = Node(node.data, temp)
        self.firstNode = temp

    def fullTraversal(self):
        l = ''
        node = self.firstNode
        while node is not None:
            l = l + str(node.data) + ' '
            node = node.next
        return l
