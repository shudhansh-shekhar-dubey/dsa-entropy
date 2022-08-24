class Node:
    def __init__(self, key=None):
        self.left = None
        self.right = None
        self.data = key

    def insert(self, data: int):
        if self.data is None:
            self.data = data
        else:
            if self.data == data:
                raise Exception(
                    'Cannot add the data into tree. Duplicate found.')
            elif self.data < data:
                if self.right is not None:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
            else:
                if self.left is not None:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
                  
    def search(self, key: int):
        if self.data == key:
            return True
        else:
            if self.data < key:
                if self.right is not None:
                    return self.right.search(key)
                else:
                    return False
            else:
                if self.left is not None:
                    return self.left.search(key)
                else:
                    return False

    def traverse_in(self):
        if self.left is not None:
            self.left.traverse_in()

        if self.data is not None:
            print(self.data)

        if self.right is not None:
            self.right.traverse_in()

    def traverse_pre(self):
        if self.data is not None:
            print(self.data)

        if self.left is not None:
            self.left.traverse_pre()

        if self.right is not None:
            self.right.traverse_pre()

    def traverse_post(self):
        if self.left is not None:
            self.left.traverse_post()

        if self.right is not None:
            self.right.traverse_post()

        if self.data is not None:
            print(self.data)
    
    def height(self):
        lh = 0
        if self.left is not None:
            lh = lh + self.left.height()
        else:
            lh = lh - 1
          
        rh = 0
        if self.right is not None:
            rh = rh + self.right.height()
        else:
            rh = rh - 1
          
        if lh > rh or lh == rh:
            return lh + 1
        else:
            return rh + 1

    def min(self):
        min = self.data
        if self.left is not None:
            min = self.left.min()
        return min
    
    def max(self):
        max = self.data
        if self.right is not None:
            max = self.right.max()
        return max
    
    def is_bst(self):
        result = True
        if self.left is not None:
            if self.left.max() < self.data:
                result = result and self.left.is_bst()
            else:
                result = False
        if self.right is not None:
            if self.right.min() > self.data:
                result = result and self.right.is_bst()
            else:
                result = False
        return result

    def node_count(self):
        count = 0
      
        if self.left is not None:
            count = count + self.left.node_count()

        if self.data is not None:
            count = count + 1

        if self.right is not None:
            count = count + self.right.node_count()
          
        return count

    def height(self):
        height1 = height2 = 0
      
        if self.left is not None:
            height1 = self.left.height() + 1

        if self.right is not None:
            height2 = self.right.height() + 1

        if height1 > height2 or height1 == height2:
            return height1
        else:
            return height2
            