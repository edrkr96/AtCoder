#Otoshidama
#多重ループの抜け方　https://note.nkmk.me/python-break-nested-loops/

n, y = map(int, input().split())
flag = False

for i in range(n+1):
  for j in range(n-i+1):
    k = n - i - j
    if 10000*i + 5000*j + 1000*k == y:
      flag = True
      print(i, j, k)
      break
  else:
    continue
  break

if flag == False:
  print(-1, -1, -1)
