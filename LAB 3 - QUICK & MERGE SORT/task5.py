# quick SORT

def quicksort(arr,lb,ub):
    if lb<ub:
        q = partition(arr,lb,ub)
        quicksort(arr,lb,q-1)
        quicksort(arr,q+1,ub)
    return arr
def partition(arr,lb,ub):
    pivot = arr[lb]
    start = lb
    end = ub
    while start<end:
        while arr[start]<= pivot and  start < ub:
            start +=1
        while arr[end] > pivot:
            end -=1
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
    arr[lb],arr[end]=arr[end],arr[lb]
    return end



inp = open('input5.txt','r')
out = open("output5.txt","w")
n = int(inp.readline())
arr = []

arr = [int(i) for i in inp.readline().split(" ")]
a=quicksort(arr,0,n-1)
print(a)

for i in range(n):
    out.write(str(a[i])+" ")
inp.close()
out.close()