import heapq
from math import inf

def dijkstra(V, graph, Source):
    pq =[]

    distance = [inf] * (V + 1)

    distance[Source] = 0
    heapq.heappush(pq, (0, Source)) # (distance, node)

    while pq:
        dis, node = pq.get()

            
        for v, w in graph[node]:
            if dis + w < distance[v]:
                distance[v] = dis + w

                    # If current distance is smaller,
                    # push it into the queue.
                pq.put((distance[v], v))

        # Return the list containing shortest distances
        # from source to all the nodes.
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

inp = open('input1b.txt', 'r')
out = open('output1b.txt', 'w')
v, e = map(int, inp.readline().split())
edges = []
for i in range(e):
    edges.append(list(map(int, inp.readline().split())))
graph=adjacent_list(v, e, edges)
source = int(inp.readline().strip())
answer=dijkstra(v, graph, source)


inp.close()
out.close()



