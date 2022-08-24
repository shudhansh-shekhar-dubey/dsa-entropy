def bubbleSort(arr):
  n = len(arr)
  
  sorted = False # We have to evaluate an unsorted array
  while not sorted: # It will iterate the loop over all data untill it is sorted
    sorted = True  # Suppose it is sorted
    for i in range(1,n):
      if arr[i] < arr[i-1]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        sorted = False  # Nope. These couplets were not sorted