n = int(input())
a = list(map(int, input().split()))
ans = "No"

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      if a[i] + a[j] + a[k] == 1000:
        ans = "Yes"
        break

print(ans)