from collections import Counter

n = int(input())
a = list(map(int, input().split()))
ans = 0

c = Counter(a) #要素を一括取得

for value in c.values(): #辞書型と同じメソッド
  ans += value // 2 
print(ans)