# 0 (n)
def sortedMerge(size1,size2,n,m):
  newSize = size1+size2
  c = [0]*newSize
  i = 0
  j = 0
  k = 0
  while (i <size1) and (j <size2):
    if n[i]<m[j]:
      c[k] = n[i]
      i+=1
    else:
      c[k] = m[j]
      j+=1
    k+=1
  while i <size1:
    c[k] = n[i]
    i+= 1
    k+= 1
  while j <size2:
    c[k] = m[j]
    j+= 1
    k+= 1
  return c


inp = open("input2b.txt","r")
out= open('output2b.txt','w')
size1 = int(inp.readline())
n = [int(i) for i in inp.readline().split(" ")]
size2 = int(inp.readline())
m = [int(i) for i in inp.readline().split(" ")]
newSize = size1+size2
v=sortedMerge(size1,size2,n,m)

for i in range(newSize):
  out.write(str(v[i])+" ")

inp.close()
out.close()