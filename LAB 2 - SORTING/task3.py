# task 3
def maximum_tasks(tasks):
  tasks.sort(key=sort_time)
  
  max_taken = 0
  selected_time = []
  prev_end_time = -99
  for i in tasks:
    if i[0]>=prev_end_time:
      selected_time.append(i)
      prev_end_time = i[1]
      max_taken+=1
  return max_taken,selected_time
def sort_time(time):
  return time[1]

inp = open("input3.txt","r")
out= open('output3.txt','w')
tasks = []
# input
n =  int(inp.readline())
for i in range(n):
  start,end = [int(i) for i in inp.readline().split(" ")]
  tasks.append((start,end))
max_taken,selected_time = maximum_tasks(tasks)

# output
out.write(f"{str(max_taken)}\n")

for i in range(len(selected_time)):
  out.write(f"{str(selected_time[i][0])} {str(selected_time[i][1])} \n")
  
inp.close()
out.close()