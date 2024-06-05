# Merge sort
# O (nlogn)
def count_inverse(arr,low,mid,high):
  c = [0]*len(arr)
  i = low
  j = mid+1
  k = low
  count = 0
  while i<=mid and j<=high:
    if arr[i]<arr[j]:
      c[k] = arr[i]
      i+=1
    else:
      c[k] = arr[j]
      count+=mid-i+1
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
  return count
def mergeSort(arr,l,r):
  count = 0
  if l<r:
    mid = (l+r)//2
    count+=mergeSort(arr,l,mid)
    count+=mergeSort(arr,mid+1,r)
    count+=count_inverse(arr,l,mid,r)
  return count
inp = open('input3.txt','r')
out = open('output3.txt','w')
n = int(inp.readline())
arr = list(map(int,inp.readline().split()))
out.write(str(mergeSort(arr,0,n-1)))
inp.close()
out.close()