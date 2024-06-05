def maximum_tasks(tasks,n,m):
  tasks.sort(key=sort_time)
  
  max_taken = 0
  
  end_time = [0]*m
  
  for i in tasks:
    start = i[0]
    end = i[1]
    for i in range(m):
      if start>=end_time[i]:
        end_time[i] = end
        max_taken+=1
        end_time.sort(reverse = True)
        break
   
  return max_taken
def sort_time(time):
  return time[1]

inp = open("input4.txt","r")
out= open('output4.txt','w')
tasks = []
# input
n,m = [int(i) for i in inp.readline().split(" ")]
for i in range(n):
  start,end = [int(i) for i in inp.readline().split(" ")]
  tasks.append((start,end))
max_taken = maximum_tasks(tasks,n,m)

# output
out.write(f"{str(max_taken)}\n")
  
inp.close()
out.close()