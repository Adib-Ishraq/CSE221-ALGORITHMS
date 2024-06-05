import heapq
from math import inf

def dijkstra(V, graph, Source):
    pq =[]

    distance = [inf] * (V + 1)
    
    distance[Source] = 0
    heapq.heappush(pq,(0, Source)) # (distance, node)

    while pq:
        dis,current = heapq.heappop(pq)
        for neighbor,weight in graph[current]:
            if distance[current]+weight<distance[neighbor]:
                distance[neighbor]=distance[current]+weight
                heapq.heappush(pq,(distance[neighbor],neighbor))
    return distance
def adjacent_list(v,e,edges):
    adj_list = {}
    for i in range(v+1):
        adj_list[i] = []
    for edge in edges:
        u= edge[0]
        v= edge[1]
        w= edge[2]
        adj_list[u].append((v,w))
    return adj_list

inp = open('input1.txt', 'r')
out = open('output1.txt', 'w')
v,e= map(int, inp.readline().split())
edges = []
for i in range(e):
    edges.append(list(map(int, inp.readline().split())))
graph=adjacent_list(v, e, edges)
source = int(inp.readline().strip())
answer=dijkstra(v, graph, source)

for i in range(1, v+1):
    if answer[i] == inf:
        out.write(str(-1) + " ")
    else:
        out.write(str(answer[i]) + " ")
inp.close()
out.close()



