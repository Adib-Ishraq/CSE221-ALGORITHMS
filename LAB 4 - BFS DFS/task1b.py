def adjacent_list(v,e,edges):
    adj_list = {}
    for i in range(v+1):
        adj_list[i] = []
    for edge in edges:
        #u,v,w = edge
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
mat=adjacent_list(v, e, edges)
for key in mat:
    out.write(f"{str(key)}: {str(mat[key])}")
    out.write("\n")
inp.close()
out.close()



