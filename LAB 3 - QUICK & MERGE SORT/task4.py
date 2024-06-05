def merge(arr1, arr2):
    m=len(arr1)-1
    max=arr1[m]+(arr2[0]**2)
    for n in range(len(arr2)):
        if arr1[m]+(arr2[n]**2)>max:
            max=arr1[m]+(arr2[n]**2)
    i=0
    j=0
    k=0
    arr3=([0]*(len(arr1)+len(arr2)))
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            arr3[k]=arr1[i]
            i+=1
            k+=1
        else:
            arr3[k]=arr2[j]
            j+=1
            k+=1
    while i<len(arr1):
        arr3[k]=arr1[i]
        i+=1
        k+=1

    while j<len(arr2):
        arr3[k]=arr2[j]
        j+=1
        k+=1

    return arr3, max


def merge_sort(arr):
    if len(arr)==1:
        return arr, arr[0]

    mid_idx=len(arr)//2

    arr1=arr[0: mid_idx]
    arr2=arr[mid_idx:len(arr)]

    arr1, max1=merge_sort(arr1)
    arr2, max2=merge_sort(arr2)

    arr3, max3 = merge(arr1, arr2)

    if max3>=max1 and max3>=max2:
        return arr3, max3
    elif max2>=max1 and max2>=max3:
        return arr3, max2
    else:
        return arr3, max1


inp = open('input4.txt','r')
out = open('output4.txt','w')
n = int(inp.readline())
arr = [int(i) for i in inp.readline().split(" ")]
x,maxval = merge_sort(arr)
out.write(str(maxval))
inp.close()
out.close()
