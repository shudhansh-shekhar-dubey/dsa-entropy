def quick_sort(arr):
  if len(arr) < 2:
    return arr
  else:
    mid = (len(arr))//2
    left = []
    right = []
    for i in range(0,mid):
      segregate(arr, i, mid, left, right)
    for j in range(mid+1, len(arr)):
      segregate(arr, j, mid, left, right)
    
    return quick_sort(left) + [arr[mid]] + quick_sort(right)

def segregate(arr, i, mid, left, right):
  if arr[mid] > arr[i]:
    left.append(arr[i])
  else:
    right.append(arr[i])
    
    
  
        
        