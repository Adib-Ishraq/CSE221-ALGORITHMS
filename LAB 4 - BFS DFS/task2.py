import collections

def bfs(graph,start):
    queue = collections.deque() # this is another method if import queue library
    #queue = []
    state = [0]*(len(graph)+1)
    queue.append(start)
    state[start] = 1
    bfs_ans = []
    while queue :
        #current = queue.pop(0)
        current = queue.popleft()
        bfs_ans.append(current)
        for neighbor in graph[current]:
            if state[neighbor]==0:
                queue.append(neighbor)
                state[neighbor]=1
    return bfs_ans

def adjacent_list(v,e,edges):
    adj_list = {}
    for i in range(v+1):
        adj_list[i] = []
    for edge in edges:
        u= edge[0]
        v= edge[1]
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')
v, e = map(int, inp.readline().split())
edges = []
for i in range(e):
    edges.append(list(map(int, inp.readline().split())))
graph=adjacent_list(v, e, edges)
answer=bfs(graph,1)

for i in answer:
    out.write(str(i)+' ')
inp.close()
out.close()