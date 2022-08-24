def selectionSort(arr): 
  count = len(arr)
  for i in range(0, count): 
    min = arr[i]
    minIndex = i
    for j in range(i, count):  
      if arr[j] < min: 
        min = arr[j]
        minIndex = j
        
    arr[minIndex] = arr[i]
    arr[i] = min

def selectionSort2(heap): 
  count = len(heap)
  for i in range(0, count): 
    for j in range(i, count):  
      if heap[j] < heap[i]: 
        heap[j],heap[i] = heap[i],heap[j]