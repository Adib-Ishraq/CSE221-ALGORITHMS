# O(N) time complexity
def target_sum(arr,l,target):
  left = 0
  right = l-1
  while left<right:
    if arr[left]+arr[right]>target:
      right-=1
    elif arr[left]+arr[right]<target:
      left+=1
    elif arr[left]+arr[right]==target:
      return f"{str(left+1)} {str(right+1)}"
  return "IMPOSSIBLE"




inp = open("input1b.txt","r")
out= open('output1b.txt','w')
l,target = [int(i) for i in inp.readline().split(" ")]
arr = [int(i) for i in inp.readline().split(" ")]
v = target_sum(arr,l,target)
out.write(v)
out.close()