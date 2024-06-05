import numpy as np
def weighted_adj_matrix(v, e,edges):
    matrix = np.zeros((v+1, v+1))
    for i in range(e):
        u = int(edges[i][0]) #start node
        v = int(edges[i][1]) # end node
        w = int(edges[i][2]) # weight
        matrix[u][v] = w
       
    return matrix

inp = open('input1a.txt', 'r')
out = open('output1a.txt', 'w')
v, e = map(int, inp.readline().split())
edges = []
for i in range(e):
    edges.append(list(map(int, inp.readline().split())))
mat=weighted_adj_matrix(v, e, edges)
for i in range(v+1):
    for j in range(v+1):
        out.write(str(int(mat[i][j])) + " ")
    out.write("\n")
inp.close()
out.close()
