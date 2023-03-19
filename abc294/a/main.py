n = int(input())
a = list(map(int, input().split()))
b = []

for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])
print(*b)
