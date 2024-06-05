def dfs_smallest_lexicographical_order(graph, visited, course, stack):
  visited[course] = 1
  neighbor = sorted(graph[course])
  for neighbor in graph[course]:
    if visited[neighbor]==0:
       dfs_smallest_lexicographical_order(graph, visited, neighbor, stack)
  stack.append(course)

def DFS_topo(graph, N):
  visited = [0] * (N+1)
  stack = []
  for course in range(1, N + 1):
    if visited[course]==0:
       dfs_smallest_lexicographical_order(graph, visited, course, stack)
  topo = []
  while stack:
     topo.append(stack.pop())
  return topo 

def adjacent_list(v,e,edges):
    adj_list = {}
    for i in range(v+1):
        adj_list[i] = []
    for edge in edges: 
        u= edge[0]
        v= edge[1]
        adj_list[u].append(v)
        
    return adj_list
def cycle(graph,start):
    state = [0]*(len(graph)+1)
    stack = []
    stack.append(start)
    while stack:
        c = stack[-1] # peeking the top element
        state[c] = 1 
        flag = False
        for n in graph[c]:
            if state[n]==0:
                stack.append(n)
                flag = True
                break
            elif state[n]==1:
                if n in stack:
                    state[n]=2
                    return "YES"
        if not flag:
            stack.pop()
            state[c]=2
    return "NO"

inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')
v, e = map(int, inp.readline().split())
edges = []
for i in range(e):
    edges.append(list(map(int, inp.readline().split())))
graph=adjacent_list(v, e, edges)
cycle_check = cycle(graph,v)

if cycle_check=="YES":
   out.write("IMPOSSIBLE")
else:
  answer= DFS_topo(graph,v)
  for i in answer:
      out.write(str(i)+" ")

inp.close()
out.close()