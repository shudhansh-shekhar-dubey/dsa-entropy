from collections import deque

def bfs(hashTable, letter, person):
  search_row = deque()
  search_row += hashTable[person]
  searched = []
  while search_row:
    neighbour = search_row.popleft()
    if neighbour not in searched:
      if neighbour[0] is letter:
        print(neighbour + ' is the one!')
        break 
      else:
        search_row += hashTable[neighbour]
        searched.append(neighbour)
        print(neighbour + ' match failed')
