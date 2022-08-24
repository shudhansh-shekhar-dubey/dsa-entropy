from lists.linkedlist import Node, List


class QueueLL:
    def __init__(self, tail: Node):
        self.list = List(tail)
        self.tail = tail

    def enqueue(self, node: Node):
        self.list.insertAfter(self.tail, node)
        self.tail = node

    def dequeue(self): 
        firstNode = self.list.firstNode
        self.list.firstNode = firstNode.next
        return firstNode

class QueueArr: 
    def __init__(self, capacity: int):
        self.list = [None] * capacity 
        self.size = 0
        self.front = 0
        self.rear = self.size + self.front
        
    def enqueue(self, key: int):
        if not self.isFull():  
          self.list[self.rear] = key
          self.size = self.size + 1
          self.rear = self.size + self.front 
          
    def dequeue(self):
        if not self.isEmpty():
          front = self.list[self.front]
          self.list[self.front] = None
          self.size = self.size - 1
          self.front = self.front + 1 
          return front
        
    def isEmpty(self):
        return self.size == 0
  
    def isFull(self):
        return self.size == (len(self.list) - 1)