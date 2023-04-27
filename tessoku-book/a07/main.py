d = int(input())
n = int(input())
ch = [0]*d #前日からの変化を記録
num = 0

for i in range(n):
  l, r = map(int, input().split())
  ch[l-1] += 1 
  if r < d:
    ch[r] -= 1 #rがd+1日目になった時を除外

for i in range(d):
  num += ch[i]
  print(num)