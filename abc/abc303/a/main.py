n = int(input())
s = input()
t = input()

for i in range(n):
  sim = False
  if s[i] == t[i]:
    sim = True
  elif (s[i] == "1" and t[i] == "l") or (s[i] == "l" and t[i] == "1"):
    sim = True
  elif (s[i] == "0" and t[i] == "o") or (s[i] == "o" and t[i] == "0"):
    sim = True
  if sim != True:
    break
  

if sim == True:
  print("Yes")
else:
  print("No")


"""
別解
n = int(input())
s = input()
t = input()

s = s.replace("1", "l")
s = s.replace("0", "o")
t = t.replace("1", "l")
t = t.replace("0", "o")

if s == t:
  print("Yes")
else:
  print("No")


"""