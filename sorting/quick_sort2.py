def quick_sort(list, start, end):
  if start < end:
    p = partition(list, start, end)
    quick_sort(list, start, p-1)
    quick_sort(list, p+1, end)

def partition(list, start, end):
  pivot = list[end] #taking last elemtn as pivot
  i = start - 1
  for j in range(start, end - 1):
    if list[j] <= pivot:
      i = i + 1
      list[i], list[j] = list[j], list[i]
  list[i+1],list[end] = list[end],list[i+1]  
  
  return i+1