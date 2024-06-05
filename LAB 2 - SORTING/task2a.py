# task 2
# O (n logn)
def sortedMerge(s1,s2,n,m):
  newSize = s1+s2
  arr = [0]*newSize
  for i in range(s1):
    arr[i] = n[i]
  for i in range(s1,newSize):
    arr[i] = m[i-s1]
  arr.sort()

  return arr
inp = open("input2a.txt","r")
out= open('output2a.txt','w')
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