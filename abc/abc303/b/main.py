import collections
n, m = map(int, input().split())
a = [list(map(int, input().split()))for _ in range(m)]
pair = []
sum = 0

for i in range(n):
  person = [i+1 for i in range(n)] 
  pair.append(person)

for i in range(m): #回数は-1のまま
  for j in range(n): #人は番号と対応
    if j == 0: #a[i][j]が右隣
      #対象の人のpair配列の隣の人の番号の部分にpを代入
      if pair[a[i][j]-1].count(a[i][j+1]) == 1: #pに置き換えられていない時のみpを代入
        index = pair[a[i][j]-1].index(a[i][j+1])
        pair[a[i][j]-1][index] = "p"
    elif j == n-1: #a[i][j-2]が左隣
      if pair[a[i][j]-1].count(a[i][j-1]) == 1:
        index = pair[a[i][j]-1].index(a[i][j-1])
        pair[a[i][j]-1][index] = "p"
    else:
      if pair[a[i][j]-1].count(a[i][j+1]) == 1: 
        index = pair[a[i][j]-1].index(a[i][j+1])
        pair[a[i][j]-1][index] = "p"
      if pair[a[i][j]-1].count(a[i][j-1]) == 1:
        index = pair[a[i][j]-1].index(a[i][j-1])
        pair[a[i][j]-1][index] = "p"
      
for i in range(n):
  st = set(pair[i])
  cnt = len(st) - 2 #1つ残ったpと自分自身を除く
  sum += cnt

print(int(sum/2)) #ペアは重複して数えない

"""
解説AC
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
cnt = 0

for i in range(1, n+1): #iとjはペアかを判定
  for j in range(i+1, n+1): #i<jとすることで、ダブルで数えることを防ぐ
    flag = False
    for k in range(m):
      for l in range(n-1): #l+1は範囲外にならないように
        if a[k][l]==i and a[k][l+1]==j: #右隣
          flag = True 
        if a[k][l]==j and a[k][l+1]==i: #左隣
          flag = True
    if flag != True: #iとjのペアに対して、隣どうしの場合が見つからなければカウント
      cnt += 1
      
print(cnt)
"""