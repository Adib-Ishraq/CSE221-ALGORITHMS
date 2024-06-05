# time complexity O(n^2)

def target_sum(arr,l,target):
  for i in range(l):
    for j in range(i+1,l):
      if arr[i]+arr[j]==target:
        return f"{str(i+1)} {str(j+1)}"
  return "IMPOSSIBLE"
inp = open("input1a.txt","r")
out= open('output1a.txt','w')
l,target = [int(i) for i in inp.readline().split(" ")]
arr = [int(i) for i in inp.readline().split(" ")]
v = target_sum(arr,l,target)
out.write(v)
out.close()