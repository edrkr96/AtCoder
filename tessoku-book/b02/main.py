a, b = map(int, input().split())
ans = "No"

for i in range(a, b+1):
    if 100 % i == 0:
        ans = "Yes"
        break

print(ans)
