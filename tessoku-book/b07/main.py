t = int(input())
n = int(input())
ex = [0]*t #変化を記録
num = 0

for i in range(n):
  l, r = map(int, input().split()) #入力から直接変化を記録
  ex[l] += 1
  if r < t: #r=tの時にRE出ないように
    ex[r] -= 1

for i in range(t):
  num += ex[i]
  print(num)