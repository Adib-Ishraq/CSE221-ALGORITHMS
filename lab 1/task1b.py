# task 1b
inp = open("input1b.txt","r")
out = open("output1b.txt","w")
n= int(inp.readline())
for i in range(n):
  m = inp.readline()[10:].split(" ")
  if m[1]=="+":
    out.write(f"The result of {int(m[0])}+{int(m[2])} is {int(m[0])+int(m[2])} \n")
  elif m[1]=="-":
    out.write(f"The result of {int(m[0])}-{int(m[2])} is {int(m[0])-int(m[2])} \n")
  elif m[1]=="*":
    out.write(f"The result of {int(m[0])}*{int(m[2])} is {int(m[0])*int(m[2])} \n")
  elif m[1]=="/":
    out.write(f"The result of {int(m[0])}/{int(m[2])} is {int(m[0])/int(m[2])} \n")
inp.close()
out.close()