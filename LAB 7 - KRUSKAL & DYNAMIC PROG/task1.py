def find_friend_circle_size(N, queries):
    parent = [-1] * (N + 1)
    sizes = {i: 1 for i in range(1, N + 1)} 

    def find(x):
        if parent[x] == -1:
            return x
        root = find(parent[x])
        parent[x] = root 
        return root

    def union(x, y):
        x_root, y_root = find(x), find(y)

        if x_root == y_root:
            return
        else:
            parent[y_root] = x_root
            sizes[x_root] += sizes[y_root]

    result = []
    for a, b in queries:
        union(a, b)
        result.append(sizes[find(a)]) 
    return result
inp = open('input1.txt', 'r')
out = open('output1.txt', 'w')
N, K = map(int, inp.readline().split())
queries = [list(map(int, line.split())) for line in inp]
friend_circle_sizes = find_friend_circle_size(N, queries)
for size in friend_circle_sizes:
    out.write(str(size) + "\n")
inp.close()
out.close()