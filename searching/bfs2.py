from collections import deque

def bfs2(graph):
  list = []
  for node in graph:  
    if ndde not in list: 
      list.append(node) 
      if graph[node]:
        graph += graph[node] 
        
  return list     
      
def bfs(hashTable, search_row, person):
  search_row = deque()
  search_row += hashTable[person]
  searched = []
  while search_row:
    neighbour = search_row.popleft()
    if hashTable[neighbour]:
      search_row += hashTable[neighbour]
      searched.append(neighbour) 
    else:
      break
      
        