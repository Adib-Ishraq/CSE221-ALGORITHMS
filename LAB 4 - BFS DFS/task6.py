def flood(edges, r, c, row, col):
    if r < 0 or c < 0 or r >= row or c >= col or edges[r][c] == "#" or edges[r][c] == "Y":
        return 0
    count = 0
    if edges[r][c] == "D":
        count = 1
    edges[r][c] = "Y"
    count += flood(edges, r + 1, c, row, col)
    count += flood(edges, r - 1, c, row, col)
    count += flood(edges, r, c + 1, row, col)
    count += flood(edges, r, c - 1, row, col)
    return count

def max_diamond(edges, row, col):
    max_diamond_collected = 0
    for i in range(row):
        for j in range(col):
            if edges[i][j] == ".":
                diamond_collected = flood(edges, i, j, row, col)
                max_diamond_collected = max(diamond_collected, max_diamond_collected)
    return max_diamond_collected

inp = open('input6.txt', 'r')
out = open('output6.txt', 'w')
edges=[]
row, col = map(int, inp.readline().split())
for i in range(row):
    r = inp.readline().strip()
    lst = []
    for j in r:
        lst.append(j)
    edges.append(lst)

collected = max_diamond(edges, row, col)

out.write(str(collected) + "\n")

inp.close()
out.close()
