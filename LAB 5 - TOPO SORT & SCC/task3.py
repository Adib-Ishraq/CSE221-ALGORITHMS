def dfs(graph, visited, vertex, stack):
  
  visited[vertex] = 1
  for neighbor in graph[vertex]:
    if visited[neighbor]==0:
      dfs(graph, visited, neighbor, stack)
  stack.append(vertex)
  return stack

def kosaraju(rev,stack):
   
   visited = [0]*(len(rev)+1)
   scc = []
   while stack:
    current = stack.pop()
    if visited[current]==0:
       component = []
       dfs(rev,visited,current,component)
       scc.append(component)
   return scc

def adjacent_list(v,e,edges):
    adj_list = {}
    for i in range(v+1):
        adj_list[i] = []
    for edge in edges: 
        u= edge[0]
        v= edge[1]
        adj_list[u].append(v)
        
    return adj_list

def reverse_graph(v,e,edges):
    rev_adj_list = {}
    for i in range(v+1):
        rev_adj_list[i] = []
    for edge in edges: 
        u= edge[0]
        v= edge[1]
        rev_adj_list[v].append(u)
        
    return rev_adj_list

inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')
v, e = map(int, inp.readline().split())
edges = []
for i in range(e):
    edges.append(list(map(int, inp.readline().split())))

graph=adjacent_list(v, e, edges)
reversed = reverse_graph(v,e,edges)

visited = [0]*(len(graph)+1)
stack = []

normal_dfs = dfs(graph, visited, 1, stack)
scc_result = kosaraju(reversed,normal_dfs)
print(scc_result)

for i in scc_result:
    out.write(str(i)+"\n")

inp.close()
out.close()