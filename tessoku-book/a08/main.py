h, w = map(int, input().split())
x = [list(map(int, input().split())) for i in range(h)]
q = int(input())
a = [list(map(int, input().split())) for i in range(q)]
cm = [[0 for j in range(w)] for i in range(h)] #累積和計算用
ans = 0

for i in range(h): #横方向に累積和を取る
  sum = 0
  for j in range(w):
    sum += x[i][j]
    cm[i][j] = sum

for j in range(w): #縦方向に累積和を取る
  sum = 0
  for i in range(h):
    sum += cm[i][j]
    cm[i][j] = sum
        
for k in range(q): #マスは(1, 1)スタートなので、デフォルトで-1
  ans = cm[a[k][2]-1][a[k][3]-1] #右下の値のみとる
  if a[k][0] > 1 and a[k][1] > 1: #上も左も余る→4マス全てを計算
    ans = ans + cm[a[k][0]-2][a[k][1]-2] - cm[a[k][0]-2][a[k][3]-1] - cm[a[k][2]-1][a[k][1]-2]
  elif a[k][0] > 1: #左のみ余る→2マスで計算
    ans = ans - cm[a[k][0]-2][a[k][3]-1]
  elif a[k][1] > 1: #上のみ余る→2マスで計算
    ans = ans - cm[a[k][2]-1][a[k][1]-2]
  print(ans)
  
  