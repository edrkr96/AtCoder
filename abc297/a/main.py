n, d = map(int, input().split())
t = list(map(int, input().split()))
flag = False

for i in range(n-1):
  if t[i+1] - t[i] <= d:
    flag = True
    print(t[i+1])
    break

if not flag:
  print(-1)
    