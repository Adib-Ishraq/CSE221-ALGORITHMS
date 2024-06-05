# task 4
def rail_sort(arr):
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
      if arr[j][0]>arr[j+1][0]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
      elif arr[j][0]==arr[j+1][0]:
        if arr[j][-1]<arr[j+1][-1]:
          arr[j],arr[j+1] = arr[j+1],arr[j]
  for i in range(len(arr)):
    out.write(" ".join(arr[i]))


arr = []
inp = open("input4.txt","r")
out = open("output4.txt","w")
number = int(inp.readline())
for i in range(number):
  arr.append(inp.readline().split(" "))
rail_sort(arr)
inp.close()
out.close()
