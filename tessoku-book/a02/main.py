n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = "No"

for i in range(n):
    if a[i] == x:
        ans = "Yes"
        break

print(ans)