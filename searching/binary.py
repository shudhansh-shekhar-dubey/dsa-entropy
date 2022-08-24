"""
BINARY SEARCH

Search for a key in a sorted list 
Find out the mid value and recurse the same procedure till you find the value

In a binary search, values left from the pivot are always lower than the pivot
while values to thr right of pivot are always higher than pivot

L < P < R
"""


class random_list:
    def __init__(self, list):
        self.list = list
  
    def binary_search(self, key, low, high):
        if low <= high:
            mid = (low + high) // 2
            if arr[mid] == item:
                return mid
            elif arr[mid] < item:
                return binary_search(arr, item, mid + 1, high)
            else:
                return binary_search(arr, item, low, mid - 1)
        else:
            return None

# Data Structure: Binary Search Tree
# On a sorted list of integers
class binary_search_tree:
    def __init__(self, list):
      self.list = []
    
    def build(self):
      mid = len(self.list) // 2
      while 