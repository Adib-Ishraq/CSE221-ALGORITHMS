import collections

def shortest_path(graph,start,destination):
    queue = collections.deque()
    state = [0]*(len(graph)+1)
    queue.append(start)
    state[start] = 1
    parent = {}
    while queue :
        current = queue.popleft()
        if current == destination:
            break
        for neighbor in graph[current]:
            if state[neighbor]==0:
                queue.append(neighbor)
                state[neighbor]=1
                parent[neighbor]=current
    s = start
    end = destination
    path = []
    time = 0
    current = end
    while current!=s:
        path.append(current)
        time+=1
        current = parent[current]
    path.append(current)
    path.reverse()
    return time,path


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

inp = open('input5.txt', 'r')
out = open('output5.txt', 'w')
v, e, d = map(int, inp.readline().split())
edges = []
for i in range(e):
    edges.append(list(map(int, inp.readline().split())))

graph=adjacent_list(v, e, edges)
time,path=shortest_path(graph,1,d)

out.write(f"Time taken:{str(time)}\n")
for i in path:
    out.write(str(i)+' ')

inp.close()
out.close()
