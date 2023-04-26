n = int(input())
a = list(map(int, input().split()))
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]
cm_sum = [0]
sum = 0

for i in range(n):
  sum += a[i] 
  cm_sum.append(sum)
  
for i in range(q):
  sub = cm_sum[lr[i][1]] - cm_sum[lr[i][0]-1]
  if sub == lr[i][1] - lr[i][0] + 1 - sub:
    print("draw")
  elif sub > lr[i][1] - lr[i][0] + 1 - sub:
    print("win")
  else:
    print("lose")