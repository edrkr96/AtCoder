n, q = map(int, input().split())
a = list(map(int, input().split()))
l_r = [list(map(int, input().split())) for _ in range(q)]
cms = []
cms.append(0)
sum = 0

for i in range(n):
    sum += a[i]
    cms.append(sum)

for i in range(q):
    print(cms[l_r[i][1]] - cms[l_r[i][0]-1])