n = input()
ans = 0

for i in range(len(n)):
  if n[i] == "1":
    ans += 2**(len(n)-1-i)

print(ans)