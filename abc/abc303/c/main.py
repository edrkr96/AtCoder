#解説AC
n, m, h, k = map(int, input().split())
s = input()
xy = set() #要素が含まれているかの判別にはset
for _ in range(m):
  x, y = map(int, input().split())
  xy.add((x, y))

pl = [0, 0]
fail = False

for i in range(n):
  if s[i] == "R":
    pl[0] += 1
  elif s[i] == "L":
    pl[0] -= 1
  elif s[i] == "U":
    pl[1] += 1
  elif s[i] == "D":
    pl[1] -= 1
    
  h -= 1 
  
  if h < 0:
    fail = True
    break

  if h < k and tuple(pl) in xy: #タプルに変換して含まれているかを判別
    h = k
    xy.remove(tuple(pl)) 
  
if fail:
  print("No")
else:
  print("Yes")