def dijkstra(graph, start, end):
  distance = {}
  parent = {}
  path = {}
  traces = ''
  
  for node in graph.keys():
    distance[node] = float("inf")
    parent[node] = None
    path[node] = True
  distance[start] = 0
  
  while path:
    nearest_node = find_nearest_node(distance, path)
    del path[nearest_node]
    
    for neighbour in graph[nearest_node].keys():
      alt = distance[nearest_node] + graph[nearest_node][neighbour]
      if alt < distance[neighbour] and distance[nearest_node] is not float("inf"):
        distance[neighbour] = alt
        parent[neighbour] = nearest_node

  if parent[end]:
    traces = end + ' -> ' + traces 
    while parent[end] is not None:
      end = parent[end]
      traces = end + ' -> ' + traces 
  
  return parent,distance,traces

def find_nearest_node(distance, path):
  nearest_node = None
  nearest_dist = float("inf")
  for node in distance:
    if nearest_dist > distance[node] and node in path:
      nearest_dist = distance[node]
      nearest_node = node
  return nearest_node
  
    

    
  
  