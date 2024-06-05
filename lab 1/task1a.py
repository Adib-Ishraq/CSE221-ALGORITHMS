# TASK 1a
inp = open("input1a.txt","r")
out = open("output1a.txt","w")
n = int(inp.readline())
for i in range(n):
  number = int(inp.readline())
  if number%2==0:
    out.write(f"{number} is an Even number\n")
  else:
    out.write(f"{number} is an odd number\n")
out.close()