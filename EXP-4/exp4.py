graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visit_BFS = []
queue = []

def bfs(visit_BFS, graph, node):
  visit_BFS.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for nearNode in graph[s]:
      if nearNode not in visit_BFS:
        visit_BFS.append(nearNode)
        queue.append(nearNode)

visit_DFS = set()

def dfs(visit_DFS, graph, node):
    if node not in visit_DFS:
        print (node, end=" ")
        visit_DFS.add(node)
        for nearNode in graph[node]:
            dfs(visit_DFS, graph, nearNode)

print("BFS:" , end =" ")
bfs(visit_BFS, graph, 'A')
print('\n')
print("DFS:" , end =" ")
dfs(visit_DFS, graph, 'A')