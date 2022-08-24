def counting(list, max):
    output = [0] * len(list)
    count = [0] * (max+1)

    #iterate in list array to update count of element appearance
    for j in range(len(list)):
      element = list[j]
      count[element] = count[element] + 1
   
    #add count of each element with previous element count to make it position
    for k in range(1,max+1):
      count[k] = count[k] + count[k-1]
 
    #iterate in list in reverse order to update output array
    for l in range(len(list)-1, -1, -1):
      element = list[l]
      position = count[element] - 1
      output[position] = element
      count[element] = position

    return output
        