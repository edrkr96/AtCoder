n = int(input())
s = input()
s = list(s)
sub = 0
ans = 0

idx = [i+1 for i, x in enumerate(s) if x == "-"]

if ("-" in s) and ("o" in s):
  if idx[0] == 1:
    for i in range(1, len(idx)):
      sub = idx[i] - idx[i-1]
      if sub > ans:
        ans = sub
  else:
    ans = idx[0]
    for i in range(1, len(idx)):
      sub = idx[i] - idx[i-1]
      if sub > ans:
        ans = sub
  if len(s) - (idx[-1]-1) > ans:
    ans = len(s) - (idx[-1]-1)
  print(ans-1)

else: 
  print(-1)