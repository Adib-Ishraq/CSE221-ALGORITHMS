# def dfs(graph,start):
#      stack = []
#      state = [0]*(len(graph)+1)
#      stack.append(start)
#      state[start] = 1
#      dfs_ans = []
#      while stack:
#          c = stack.pop()
#          if c not in dfs_ans:
#             dfs_ans.append(c)
#          for n in graph[c]:
#             if state[n]==0:
#                 stack.append(n)
#                 state[n] = 1
#             elif n not in dfs_ans:
#                 dfs_ans.append(n)
#      return dfs_ans

def dfs(graph,start,visited,dfs_ans):
    visited[start] = 1
    dfs_ans.append(start)
    for neighbor in graph[start]:
        if visited[neighbor]==0:
            dfs(graph,neighbor,visited,dfs_ans)
    return dfs_ans

def adjacent_list(v,e,edges):
    adj_list = {}
    for i in range(v+1):
        adj_list[i] = []
    for edge in edges: # creating a bidirectional graph
        u= edge[0]
        v= edge[1]
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')
v, e = map(int, inp.readline().split())
edges = []
for i in range(e):
    edges.append(list(map(int, inp.readline().split())))
graph=adjacent_list(v, e, edges)
visited = [0]*(len(graph)+1)
dfs_ans = []
answer=dfs(graph,1,visited,dfs_ans)
for i in answer:
    out.write(str(i)+" ")

inp.close()
out.close()