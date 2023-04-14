n, k = map(int, input().split())
cnt = 0

#2つを決めれば自動でもう1つは決まる(n**3 → n**2)
for i in range(1, n+1):
  for j in range(1, n+1):
    if 1 <= (k - i - j) <= n:
        cnt += 1

print(cnt)