import ast    #to process trees.
file=open("cities","r")  #open data file
data=file.read()
graph=ast.literal_eval(data)
print(graph)  #pritn graph
file.close()  #to prevent file errors.

visited = []   #visited nodes list.
queue = []     #Initialize a empty queue.

def bfs(visited, graph, node): #BFS function
  visited.append(node)
  queue.append(node)

  while queue:          # visiting each node by a loop
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("The output of The Breadth-First Search algorithm ")
bfs(visited, graph, '5')    #call The algorithm function