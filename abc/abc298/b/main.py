import copy
n = int(input())
a = [input().split() for _ in range(n)]
b = [input().split() for _ in range(n)]
cnt = 0
count = 0
flag = False
skip = False

for i in range(n):
  for j in range(n):
     if a[i][j] == '1':
      cnt += 1
      if a[i][j] == b[i][j]:
        count += 1
if cnt == 0:
    flag = True
    skip = True
if cnt == count:
    flag = True
    skip = True

if not skip:
  for k in range(3):
    cnt = 0
    count = 0
    tmp = copy.deepcopy(a) # 複合リストはdeepcopy https://qiita.com/Kaz_K/items/a3d619b9e670e689b6db
    for i in range(n):
      for j in range(n):
        a[i][j] = tmp[n-1-j][i] # 添字に変化により違う値に(実際に書いて確かめる)
        if a[i][j] == '1':
          cnt += 1
          if a[i][j] == b[i][j]:
            count += 1
    #print(cnt, count)
    #print(a)
    if cnt == count:
      flag = True
      break
    
if flag:
  print("Yes")
else:
  print("No")