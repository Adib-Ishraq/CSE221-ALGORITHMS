def quickSelect(arr,k,l,r):
    pivot = arr[r] #righmost value pivot
    p = l
    for i in range(l,r):
      if arr[i]<=pivot:
        arr[p],arr[i]=arr[i],arr[p]
        p+=1
    arr[p],arr[r]=arr[r],arr[p]

    if p>k-1:
        return quickSelect(arr,k,l,p-1)
    elif p<k-1:
        return quickSelect(arr,k,p+1,r)
    else:
        return arr[p]
    
inp = open('input6.txt','r')
out = open('output6.txt','w')
n = int(inp.readline())
arr = [int(i) for i in inp.readline().split(" ")]
k = int(inp.readline())
for i in range(k):
    m = int(inp.readline())
    a=quickSelect(arr,m,0,n-1)
    out.write(str(a))
    out.write("\n")
inp.close()
out.close()
