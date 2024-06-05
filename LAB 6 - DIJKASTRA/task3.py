import heapq
from math import inf

def dijkstra(V, graph, Source):
    pq =[]

    danger = [inf] * (V + 1)
    
    danger[Source] = 0
    heapq.heappush(pq,(0, Source)) # (distance, node)

    while pq:
        current_dis,current_node = heapq.heappop(pq)

        for neighbor,weight in graph[current_node]:

            if max(current_dis,weight)<danger[neighbor]:

                danger[neighbor] = max(current_dis,weight)
                heapq.heappush(pq,(danger[neighbor],neighbor))
    return danger

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

inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')
v,e= map(int, inp.readline().split())
edges = []
for i in range(e):
    edges.append(list(map(int, inp.readline().split())))
graph=adjacent_list(v, e, edges)

answer=dijkstra(v, graph, 1)

out.write(str(answer[v]))
inp.close()
out.close()



