# O (nlogn)
def merge(arr,low,mid,high):
  c = [0]*len(arr)
  i = low
  j = mid+1
  k = low
  while i<=mid and j<=high:
    if arr[i]<arr[j]:
      c[k] = arr[i]
      i+=1
    else:
      c[k] = arr[j]
      j+=1
    k+=1
  if i>mid :
    while (j<=high):
      c[k] = arr[j]
      j+=1
      k+=1
  else:
    while (i<=mid):
      c[k] = arr[i]
      i+=1
      k+=1
  for m in range(low,high+1):
    arr[m] = c[m]
  return arr

def mergeSort(arr,l,r):
  if l<r:
    mid = (l+r)//2
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)
  return arr

inp = open('input1.txt','r')
out = open('output1.txt','w')
n = int(inp.readline())
arr = list(map(int,inp.readline().split()))
a=mergeSort(arr,0,n-1)
for i in range(n):
  out.write(str(a[i]))
  out.write(" ")
inp.close()
out.close()