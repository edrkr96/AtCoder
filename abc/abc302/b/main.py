h, w = map(int, input().split())
s = []
s_p = []
flag = False
import collections

for i in range(h):
  el = input().split()
  #print(el[0])
  new = []
  for j in range(w):
    new.append(el[0][j])
  s.append(new)

for i in range(h):
  c = collections.Counter(s[i])
  if c["s"] > 0:
    for j in range(w):
      if s[i][j] == "s":
        s_p = s_p + [[i, j]]
#print(s_p)

for k in range(len(s_p)):
  i = s_p[k][0]
  j = s_p[k][1]
  #print(i, j)
  
  #左上
  if i>=4 and j>=4:
    if s[i-1][j-1] == "n":
      if s[i-2][j-2] == "u":
        if s[i-3][j-3] == "k":
          if s[i-4][j-4] == "e":
            print(i+1, j+1)
            print(i, j)
            print(i-1, j-1)
            print(i-2, j-2)
            print(i-3, j-3)
            break
  #上
  if i>=4:
    if s[i-1][j] == "n":
      if s[i-2][j] == "u":
        if s[i-3][j] == "k":
          if s[i-4][j] == "e":
            print(i+1, j+1)
            print(i, j+1)
            print(i-1, j+1)
            print(i-2, j+1)
            print(i-3, j+1)
            break
            
  #右上
  if i>=4 and w-j>=5:
    if s[i-1][j+1] == "n":
      if s[i-2][j+2] == "u":
        if s[i-3][j+3] == "k":
          if s[i-4][j+4] == "e":
            print(i+1, j+1)
            print(i, j+2)
            print(i-1, j+3)
            print(i-2, j+4)
            print(i-3, j+5)
            break
  #左
  if j>=4:
    if s[i][j-1] == "n":
      if s[i][j-2] == "u":
        if s[i][j-3] == "k":
          if s[i][j-4] == "e":
            print(i+1, j+1)
            print(i+1, j)
            print(i+1, j-1)
            print(i+1, j-2)
            print(i+1, j-3)
            break
  #右
  if w-j>=5:
    if s[i][j+1] == "n":
      if s[i][j+2] == "u":
        if s[i][j+3] == "k":
          if s[i][j+4] == "e":
            print(i+1, j+1)
            print(i+1, j+2)
            print(i+1, j+3)
            print(i+1, j+4)
            print(i+1, j+5)
            break

  #左下
  if h-i>=5 and j>=4:
    if s[i+1][j-1] == "n":
      if s[i+2][j-2] == "u":
        if s[i+3][j-3] == "k":
          if s[i+4][j-4] == "e":
            print(i+1, j+1)
            print(i+2, j)
            print(i+3, j-1)
            print(i+4, j-2)
            print(i+5, j-3)
            break
  #下
  if h-i>=5:
    if s[i+1][j] == "n":
      if s[i+2][j] == "u":
        if s[i+3][j] == "k":
          if s[i+4][j] == "e":
            print(i+1, j+1)
            print(i+2, j+1)
            print(i+3, j+1)
            print(i+4, j+1)
            print(i+5, j+1)
            break
            
  #右下
  if h-i>=5 and w-j>=5:
    if s[i+1][j+1] == "n":
      if s[i+2][j+2] == "u":
        if s[i+3][j+3] == "k":
          if s[i+4][j+4] == "e":
            print(i+1, j+1)
            print(i+2, j+2)
            print(i+3, j+3)
            print(i+4, j+4)
            print(i+5, j+5)
            break
