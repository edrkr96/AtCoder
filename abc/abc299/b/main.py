n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))
winner = 0
ans = 0

flag = t in c
fst = c[0]

if flag:
  for i in range(len(c)):
    if c[i] == t:
      if winner == 0:
        winner = r[i]
        ans = i+1
      elif winner < r[i]:
        winner = r[i]
        ans = i+1
    
else:
  winner = r[0]
  ans = 1
  for i in range(1, len(c)):
    if c[i] == fst:
      if winner < r[i]:
        winner = r[i]
        ans = i+1

print(ans)