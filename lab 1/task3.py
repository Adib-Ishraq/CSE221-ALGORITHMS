# task 3

def rankStudents(length,id,marks):

  for i in range(0,length):
    max_idx = i
    for j in range(i+1,length):
      if marks[j]>marks[max_idx] or (marks[j]==marks[max_idx] and id[j]<id[max_idx]):
        max_idx = j
    marks[i],marks[max_idx] = marks[max_idx],marks[i]
    id[i],id[max_idx] = id[max_idx],id[i]
  for i in range(length):
      out.write(f"ID: {id[i]} Mark: {marks[i]}\n")

inp = open("input3.txt","r")

length = int(inp.readline())
id = inp.readline().split(" ")
marks = inp.readline().split(" ")
for i in range(len(id)):
  id[i]=int(id[i])
for i in range(len(marks)):
  marks[i] = int(marks[i])

out = open("output3.txt","w")
rankStudents(length,id,marks)

inp.close()
out.close()