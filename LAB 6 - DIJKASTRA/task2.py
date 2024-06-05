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

def meet(graph,p1,p2):
    alice_time = dijkstra(v,graph,p1)
    
    bob_time = dijkstra(v,graph,p2)
    min_time = inf
    meetingnode = -1
    
    for i in range(1,len(graph)):
        if i!=p1 and i!=p2 and alice_time[i]!=inf and bob_time[i]!=inf:
            time = max(alice_time[i],bob_time[i])
            if min_time>time:
                min_time=time
                meetingnode = i 
    return min_time, meetingnode

inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')
v,e= map(int, inp.readline().split())
edges = []
for i in range(e):
    edges.append(list(map(int, inp.readline().split())))
graph=adjacent_list(v, e, edges)

sources = list(map(int, inp.readline().split()))

time,node = meet(graph,sources[0],sources[1])
if time == inf:
    out.write("Impossible\n")
else:
    out.write(f"Time {time}\n")
    out.write(f"Node {node}\n")

inp.close()
out.close()



