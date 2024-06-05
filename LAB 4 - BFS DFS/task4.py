# def cycle(graph,start):
#     state = [0]*(len(graph)+1)
#     stack = []
#     stack.append(start)
#     while stack:
#         c = stack[-1] # peeking the top element
#         state[c] = 1 
#         flag = False
#         for n in graph[c]:
#             if state[n]==0:
#                 stack.append(n)
#                 flag = True
#                 break
#             elif state[n]==1:
#                 if n in stack:
#                     state[n]=2
#                     return "YES"
#         if not flag:
#             stack.pop()
#             state[c]=2
#     return "NO"

def cycle(graph,start,visited):
    visited[start] = 1
    flag = False

    for neighbor in graph[start]:
        if visited[neighbor]==1:
            return True
        elif visited[neighbor]==0:
            flag = cycle(graph,neighbor,visited)
            visited[neighbor]+=1
    return flag

def adjacent_list(v,e,edges):
    adj_list = {}
    for i in range(v+1):
        adj_list[i] = []
    for edge in edges:
        u= edge[0]
        v= edge[1]
        adj_list[u].append(v)
        
    return adj_list

inp = open('input4.txt', 'r')
out = open('output4.txt', 'w')
v, e = map(int, inp.readline().split())
edges = []
for i in range(e):
    edges.append(list(map(int, inp.readline().split())))
graph=adjacent_list(v, e, edges)
# answer=cycle(graph,1)
visited = [0]*(len(graph)+1)

answer=cycle(graph,1,visited)
if answer:
    out.write("YES")
else:
    out.write("NO")
inp.close()
out.close()