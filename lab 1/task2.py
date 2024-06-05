# task 2
inp = open("input2.txt","r")
out = open("output2.txt","w")
n = int(inp.readline())
def bubbleSort(arr):
  for i in range(len(arr)-1):
    flag = True
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        flag = False
    if flag == True:
      break
lst = inp.readline().split(" ")
for i in range(len(lst)):
  lst[i] = int(lst[i])
bubbleSort(lst)
for i in range(len(lst)):
  out.write(str(lst[i])+" ")
inp.close()
out.close()