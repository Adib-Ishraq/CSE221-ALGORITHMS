# Kahns algo
def BFS_topo(graph):
    in_deg = {}
    for i in graph:
        in_deg[i]=0
    topo = []
    q= [] # jader in_deg = 0 tader queue te push korbo
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_deg[neighbor]+=1
    for u,count in in_deg.items():
        if count==0:
            q.append(u)
    while q:
        c = q.pop(0)
        topo.append(c)
        for neighbor in graph[c]:
            in_deg[neighbor]-=1
            if in_deg[neighbor]==0:
                q.append(neighbor)
    if len(topo)!=len(graph):
        return "IMPOSSIBLE"
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

inp = open('input1b.txt', 'r')
out = open('output1b.txt', 'w')
v, e = map(int, inp.readline().split())
edges = []

for i in range(e):
    edges.append(list(map(int, inp.readline().split())))

graph=adjacent_list(v, e, edges)

answer= BFS_topo(graph)
if answer=="IMPOSSIBLE":
    out.write("IMPOSSIBLE")
for i in (answer):
    if i!=0:
        out.write(str(i)+" ")

inp.close()
out.close()