def mergeSort(heap):
  count = len(heap)
  if count > 1:
    mid = count//2
    
    left = heap[:mid]
    right = heap[mid:]

    mergeSort(left) 
    mergeSort(right)

    i = j = k =0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
          heap[k] = left[i]
          i += 1
      else:
          heap[k] = right[j]
          j += 1
      k += 1

    # Checking if any element was left
    while i < len(left):
        heap[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        heap[k] = right[j]
        j += 1
        k += 1


def merge(left, right):
  result = []
  i = j = 0
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  while i < len(left):
    result.append(left[i])
    i += 1
  while j < len(right):
      result.append(right[j])
      j += 1 

  return result

  
def mergeSort2(arr):
  if len(arr) < 2:
    return arr[:]
  else:
    mid = len(arr)//2
    return merge(mergeSort2(arr[:mid]), mergeSort2(arr[mid:])) 