class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return
        else:
            self.parent[y_root] = x_root

def minimum_maintenance_cost(n, m, edges):
    edges.sort(key=lambda x: x[2])  
    uf = UnionFind(n)  
    mst_cost = 0
    mst_edges = []
    for u, v, w in edges:
        if uf.find(u - 1) != uf.find(v - 1):
            mst_cost += w
            uf.union(u - 1, v - 1)
            mst_edges.append((u, v, w))
    return mst_cost, mst_edges

inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')
n, m = map(int, inp.readline().split())
edges = [list(map(int, line.split())) for line in inp.readlines()]
result, _ = minimum_maintenance_cost(n, m, edges)
out.write(str(result))
inp.close()
out.close()