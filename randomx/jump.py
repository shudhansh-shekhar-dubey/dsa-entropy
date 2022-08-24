def jump_count(arr):
  jump = 0
  index = 0
  register = []
  while index >= 0 and index < len(arr):
    if index not in register:
      register.append(index)
      index = arr[index]
      jump += 1
    else:
      index = -1
  return jump
