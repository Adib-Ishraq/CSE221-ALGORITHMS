def mergeSort(arr,l,r):
  if l==r:
    return arr[l]
  else:
    if l<r:
        mid = (l+r)//2
        a1 = mergeSort(arr,l,mid)
        a2 = mergeSort(arr,mid+1,r)
        if a1>a2:
          return a1
        else:    
          return a2
 
inp = open('input2.txt','r')
out = open('output2.txt','w')
n = int(inp.readline())
arr = [int(i) for i in inp.readline().split(" ")]
a=mergeSort(arr,0,n-1)

out.write(str(a))
inp.close()
out.close() 