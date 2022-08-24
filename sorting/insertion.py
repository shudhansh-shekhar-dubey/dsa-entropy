def insertionSort(arr): 
  if len(arr) > 1: # only if more than one elemtens
    for i in range(1,len(arr)): # loop ahead from second element
      key = arr[i]
      for j in range(i-1, -1, -1): # loop in reverse till previous element
        if key < arr[j]:  
          arr[j+1] = arr[j] # swap next element with current
          arr[j] = key # swap current element with key
