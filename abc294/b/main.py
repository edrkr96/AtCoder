h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
#print(a)
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp = list(alp)

for i in range(h):
  s = []
  for j in range(w):
    if a[i][j] == 0:
      s.append('.') 
    else:
      s.append(alp[a[i][j]-1])
  print(('').join(s))